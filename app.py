from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/books", methods=["GET"])
def get_books():
    # Route to fetch books
    pass

@app.route("/rate", methods=["POST"])
def rate_book():
    # Route to submit ratings
    pass

if __name__ == "__main__":
    app.run(debug=True)
