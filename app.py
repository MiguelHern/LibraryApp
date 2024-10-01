from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from models import db, User, Book, Library  # Asegúrate de importar todos los modelos

app = Flask(__name__)
app.config.from_object(Config)

# Inicializa la instancia de SQLAlchemy
db.init_app(app)

# Inicializa Flask-Migrate
migrate = Migrate(app, db)

@app.route('/')
def index():
    libraries = Library.query.all()
    return render_template('base.html', libraries=libraries)


@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        # Para agregar un nuevo usuario
        user_name = request.form['user_name']
        major = request.form['major']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']

        new_user = User(user_name=user_name, major=major, email=email, phone_number=phone_number, address=address)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!')

        return redirect(url_for('manage_users'))

    # Obtener todos los usuarios
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    # Aquí puedes manejar tanto la actualización como la eliminación
    if request.form['_method'] == 'PUT':
        user = User.query.get(user_id)
        user.user_name = request.form['user_name']
        user.major = request.form['major']
        user.email = request.form['email']
        user.phone_number = request.form['phone_number']
        user.address = request.form['address']
        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('manage_users'))

    elif request.form['_method'] == 'DELETE':
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!')
        return redirect(url_for('manage_users'))
    

@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        # Para agregar un nuevo usuario
        book_name = request.form['book_name']
        author = request.form['author']
        publication_year = request.form['publication_year']
        isbn = request.form['isbn']
        loans = request.form['loans']

        new_book = User(book_name=book_name, author=author, publication_year=publication_year, isbn=isbn, loans=loans)
        db.session.add(new_book)
        db.session.commit()
        flash('User added successfully!')

        return redirect(url_for('manage_users'))

    # Obtener todos los usuarios
    books = Book.query.all()
    return render_template('books.html', books=books)


@app.route('/books/<int:user_id>', methods=['POST'])
def edit_book(book_id):
    # Aquí puedes manejar tanto la actualización como la eliminación
    if request.form['_method'] == 'PUT':
        user = User.query.get(book_id)
        user.user_name = request.form['user_name']
        user.major = request.form['major']
        user.email = request.form['email']
        user.phone_number = request.form['phone_number']
        user.address = request.form['address']
        db.session.commit()
        flash('User updated successfully!')
        return redirect(url_for('manage_users'))

    elif request.form['_method'] == 'DELETE':
        user = User.query.get(book_id)
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!')
        return redirect(url_for('manage_users'))
    

@app.route('/loans', methods=['GET', 'POST'])
def manage_loans():
    
    # Obtener todos los prestamos
    
    return render_template('loans.html')








if __name__ == '__main__':
    app.run(debug=True)
