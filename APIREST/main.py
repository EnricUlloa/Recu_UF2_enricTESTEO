from fastapi import FastAPI, Form
from services.user import create_user, create_table, obtain_user

app = FastAPI()

create_table()

@app.post("/formulario/registro", response_model=dict)
async def register(
    nombre: str = Form(...),
    apellido: str = Form(...),
    email: str = Form(...),
    descripcion: str = Form(None),
    curso: str = Form(...),
    anio: str = Form(...),
    direccion: str = Form(...),
    cp: str = Form(None),
    password: str = Form(...)
):
    result = create_user(nombre, apellido, email, descripcion, curso, anio, direccion, cp, password)
    return result

@app.get("/formulario/perfil/{email}")
async def obtener(email: str):
    result = obtain_user(email)
    return result