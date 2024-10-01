# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Library(db.Model):
    __tablename__ = 'libraries'
    library_id = db.Column(db.Integer, primary_key=True)
    library_name = db.Column(db.String(100), nullable=False)
    books = db.relationship('Book', backref='library', lazy=True)
    librarians = db.relationship('Librarian', backref='library', lazy=True)

class Librarian(db.Model):
    __tablename__ = 'librarians'
    librarian_id = db.Column(db.Integer, primary_key=True)
    librarian_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.library_id'), nullable=False)
    loans_issued = db.relationship('Loan', foreign_keys='Loan.librarian_loan_id', backref='librarian_loan', lazy=True)  # Bibliotecarios que emiten préstamos
    loans_received = db.relationship('Loan', foreign_keys='Loan.librarian_return_id', backref='librarian_return', lazy=True)  # Bibliotecarios que reciben devoluciones

class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    publication_year = db.Column(db.Integer, nullable=True)
    isbn = db.Column(db.String(13), nullable=True)
    library_id = db.Column(db.Integer, db.ForeignKey('libraries.library_id'), nullable=False)
    loans = db.relationship('Loan', backref='book', lazy=True)

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    loans = db.relationship('Loan', backref='user', lazy=True)

class Loan(db.Model):
    __tablename__ = 'loans'
    loan_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id'), nullable=False)
    librarian_loan_id = db.Column(db.Integer, db.ForeignKey('librarians.librarian_id'), nullable=False)  # Bibliotecario que emite el préstamo
    librarian_return_id = db.Column(db.Integer, db.ForeignKey('librarians.librarian_id'), nullable=True)  # Bibliotecario que recibe la devolución
    loan_timestamp = db.Column(db.DateTime, nullable=False)  # Fecha y hora del préstamo
    return_timestamp = db.Column(db.DateTime, nullable=True)  # Fecha y hora de la devolución
    due_date = db.Column(db.Date, nullable=False)  # Fecha de vencimiento para devolver el libro
