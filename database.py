import sqlite3
from flask import g, Flask

app = Flask(__name__)

def get_db():
    """
    Gets database else creates it
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("users.db")
        return db

@app.teardown_appcontext
def close_connection(exception):
    """
    Closes connection
    """
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    return users
