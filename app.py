from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '20815ea66562e8d6425cec6f1d7fd551'  # for encryption / decryption
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookrater.db'
db = SQLAlchemy(app)

# Define the data model
class Book(db.Model):
    isbn = db.Column(db.String(13), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    average_rating = db.Column(db.Float, default=0.0)
    # Relationship to user books
    user_books = db.relationship('User_Books', backref='book')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hash = db.Column(db.String(100), nullable=False)
    # Relationship to user_books
    books = db.relationship('User_Books', backref='user')

class User_Books(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    isbn = db.Column(db.String(13), db.ForeignKey('book.isbn'), primary_key=True)
    user_rating = db.Column(db.Float, db.CheckConstraint('user_rating >= 1 AND user_rating <= 10'), default=0.0)

# Create the database and tables (only creates if doesn't already exist)
with app.app_context():
    db.create_all()

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
