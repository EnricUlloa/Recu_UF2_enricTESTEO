from config import database
from schema.users_sch import user_schema

#conn = database.connection_db()

def create_table():
    conn = database.connection_db()
    cursor = conn.cursor()
    sql_table = '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            apellido VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            descripcion TEXT,
            curso VARCHAR(100) NOT NULL,
            anio VARCHAR(100) NOT NULL,
            direccion VARCHAR(200) NOT NULL,
            cp VARCHAR(10),
            password VARCHAR(255) NOT NULL
        )    
    '''
    cursor.execute(sql_table)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla creada correctamente")
    return {"mensaje": "Tabla creada correctamente"}

def create_user(nombre, apellido, email, descripcion, curso, anio, direccion, cp, password):
    conn = database.connection_db()
    cursor = conn.cursor()
    sql_insert = '''INSERT INTO users (nombre, apellido, email, descripcion, curso, anio, direccion, cp, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    values = (nombre, apellido, email, descripcion, curso, anio, direccion, cp, password)
    cursor.execute(sql_insert, values)
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje": "Usuario creado correctamente"}

def obtain_user(email):
    conn = database.connection_db()
    cursor = conn.cursor()
    sql_view = "SELECT id, nombre, apellido, email, curso, anio, direccion FROM users WHERE email = %s"
    cursor.execute(sql_view, (email,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    if resultado is None:
        return {"error": "Usuario no encontrado"}
    return user_schema(resultado)

def update_user(id, apellido, direccion):
    conn = database.connection_db()
    cursor = conn.cursor()
    sql_update = '''UPDATE users SET apellido = %s, direccion = %s WHERE id = %s'''
    cursor.execute(sql_update, (apellido, direccion, id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje": "Usuario actualizado correctamente"}
