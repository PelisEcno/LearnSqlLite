import sqlite3

#Conectar a la base de datos
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

#Crear tabla de los usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
               ''')
#Pedir datos del usuario
user = input('Ingrese su nombre')
email = input('Ingrese su email')
username = input('Ingrese su nombre de usuario')
password = input('Ingrese su contraseña')

#Insertamos el usuario a la BD
cursor.execute('''
    INSERT INTO usuarios (nombre, email, username, password)
    VALUES (?,?,?,?)

''', (user, email, username, password))

#Guardamos cambios
conn.commit()

#Mostrar mensaje de exito
print("Usuario registrado con éxito")
print(f"Los datos del usuario registrado son:\nNombre: {user}\nEmail: {email}\nUsername: {username}\nPassword: {password}")

#Cerramos la conexion
conn.close()
