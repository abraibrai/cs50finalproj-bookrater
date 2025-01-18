from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = '20815ea66562e8d6425cec6f1d7fd551'  # for encryption / decryption
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/abbybraiman/cs50finalproj-bookrater/instance/bookrater.db'
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
    username = db.Column(db.String, nullable=False, unique=True)
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
    print("Route '/' is being called")
    print("Rendering index.html extended from layout.html")
    # Get top 100 highest rated books from books table
    top_books = Book.query.order_by(Book.average_rating.desc()).limit(100).all()
    if not top_books:
        print("No books found in the database.")
    return render_template("index.html", top_books = top_books)

@app.route("/register", methods=["GET","POST"])
def register():
    # User reached via POST (submitted a form)
    if request.method=="POST":
        # Confirm a username provided
        username = request.form.get("username")
        if not username:
            flash("Username is required", "error")
            return redirect(url_for("register"))
        
        # Confirm a password provided
        password = request.form.get("password")
        if not password:
            flash("Password is required", "error")
            return redirect(url_for("register"))
        
        # Confirm password confirmation provided
        confirmation = request.form.get("confirmation")
        if not confirmation:
            flash("Password confirmation is required", "error")
            return redirect(url_for("register"))
        
        # Confirm username is not taken
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username is already taken", "error")
            return redirect(url_for("register"))
        
        # Confirm password confirmation matches provided password
        if password != confirmation:
            flash("Passwords do not match", "error")
            return redirect(url_for("register"))
        
        # Hash password
        hashed_password = generate_password_hash(password)
        
        # Register user
        new_user = User(username=username, hash = hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("User registered successfully!", "success")
        
        # Return to main
        return redirect(url_for("index"))

    # User reached via GET (clicking a link / redirect)
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    # Clear any existing session
    session.clear()
    # User reached via POST (submitted a form)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Ensure username submitted
        if not username:
            flash("Username is required", "error")
            return redirect(url_for("login"))
        
        # Ensure password submitted
        if not password:
            flash("Password is required", "error")
            return redirect(url_for("login"))

        # Query database for username
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.hash, password):
            flash("Invalid username or password", "error")
            return redirect(url_for("login"))
        
        # Remember which user has logged in
        session["user_id"] = user.id

        # Return to main
        return redirect(url_for("index"))

    # User reached via GET (clicking a link / redirect)
    else:
        return render_template("login.html")

@app.route("/logout", methods=["GET"])
def logout():
    # Automatically clear the session upon click
    session.clear()
    flash("You've successfully logged out", "success")
    # Return to index.html
    return redirect(url_for("index"))

@app.route("/books", methods=["GET"])
def get_books():
    # Get books read by a user from user_books table
    user_books = db.session.query(
        Book.isbn,
        Book.title,
        Book.author,
        User_Books.user_rating
    ).join(
        Book, Book.isbn == User_Books.isbn
    ).filter(
        User_Books.user_id == session["user_id"]
    ).order_by(
        User_Books.user_rating.desc()
    ).all()
    
    if not user_books:
        print("No books for the user found in the database.")
    
    return render_template("books.html", user_books = user_books)

@app.route("/rate", methods=["POST"])
def rate_book():
    # Route to submit ratings
    pass

if __name__ == "__main__":
    app.run(debug=True)