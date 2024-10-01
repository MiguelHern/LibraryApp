from app import app, db  # Importa 'app' y 'db' desde tu archivo 'app.py'
from models import Library  # Importa tu modelo Library

# Función para insertar datos iniciales
def insert_initial_data():
    with app.app_context():  # Crea el contexto de la aplicación
        if Library.query.count() == 0:  # Verifica si ya hay datos
            library1 = Library(library_name='Facultad de Ingeniería')
            library2 = Library(library_name='Facultad de Medicina')
            library3 = Library(library_name='Biblioteca Principal')
            
            db.session.add(library1)
            db.session.add(library2)
            db.session.add(library3)
            db.session.commit()
            print("Datos iniciales insertados.")
        else:
            print("Los datos ya existen en la base de datos.")

if __name__ == '__main__':
    insert_initial_data()  # Llama a la función directamente
