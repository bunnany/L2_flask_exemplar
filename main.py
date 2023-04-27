from flask import Flask, render_template

# Create a Flask app
app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

names = ["Marilyn", "Manson"]

# Index page
@app.route('/')
def index():
    return render_template('index.html', names=names)

if __name__ == '__main__':
    # Run the Flask app
    app.run(
        host='0.0.0.0',
        debug=True,
        port=8080
    )