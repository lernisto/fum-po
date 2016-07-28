import click
import datetime
import couchdb
from urllib.parse import urlsplit,urlunsplit

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def catch(db,dream):
    now = datetime.datetime.utcnow()
    doc = {"dream":dream,"date":now.isoformat()+"Z","status":"new"}
    return db.save(doc)

def getdb(database):
    p = urlsplit(database)
    server = urlunsplit((p.scheme,p.netloc,"","",""))
    dbname = p.path[1:]
    couch = couchdb.Server(server)
    if dbname in couch:
        db = couch[dbname]
    else:
        db = couch.create(dbname)
    return db

@click.command()
@click.option("--database",default="http://localhost:5984/dreams")
@click.argument('input', type=click.File('rb'), default="-")
def cli(database,input):
    """dream INPUT
        read yaml from INPUT (defaults to standard input) and add it to the local CouchDB database `dreams`
    """
    dream = load(input,Loader=Loader)
    dreamid = catch(getdb(database),dream)
    click.echo(dreamid)
