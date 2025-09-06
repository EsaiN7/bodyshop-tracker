from app import create_app, objDB
from flask.cli import with_appcontext
import click
import webbrowser


app = create_app()


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")  # auto-opens browser
    app.run(debug=True)

#custom commands to init the db
@app.cli.command("init-db")
@with_appcontext
def init_db():
    """Create all database tables."""
    objDB.create_all()
    click.echo("Initialized the database.")
