from flask import Flask, render_template, g
import sqlite3

# Create a Flask app
app = Flask(__name__, template_folder="templates", static_folder="static")


def get_db():
    """
    Gets database else creates it
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("users.db")
        # Create table in here db.execute("CREATE")
        db.execute("""CREATE TABLE IF NOT EXISTS Users (
                    PersonID int,
                    LastName varchar(255),
                    FirstName varchar(255))""")
        db.execute("""INSERT INTO Users (
                    PersonID, LastName, FirstName)
                    VALUES (0, 'Manson', 'Marilyn'),
                    (1, 'Amos', 'Tori'),
                    (2, 'Styles', 'Harry');""")
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
    c.execute("SELECT * FROM Users")
    users = c.fetchall()
    #return users
    return render_template('index.html', users=users)


# names = ["Marilyn", "Manson"]

# names = names
# print(names)

# Index page
"""
@app.route('/')
def index():
    return render_template('index.html', names=names)
    """

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", debug=True, port=8080)
