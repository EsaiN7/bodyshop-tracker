from app import create_app, objDB
from flask.cli import with_appcontext
import click


app = create_app()

#custom commands to init the db
@app.cli.command("init-db")
@with_appcontext
def init_db():
    """Create all database tables."""
    objDB.create_all()
    click.echo("Initialized the database.")