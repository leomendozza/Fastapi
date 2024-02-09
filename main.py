from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo: str
    autor: str
    paginas: int
    editorial: Optional[str]

@app.get("/")
def index():
    return {"mensaje":"Hola"}

@app.get("/libros/{id}")
def mostrar_libro(id):
    return {"data":id}

@app.post("/Libros")
def insertar_libro(libro: Libro):
    return{"mensaje": f"libro {libro.titulo} insertado"}