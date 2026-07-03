from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

tareas = []


class Tarea(BaseModel):
    descripcion: str
    prioridad: int


class Usuario(BaseModel):
    nombre: str
    edad: int


@app.get("/tareas")
def obtener_tareas():
    return tareas


@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    nueva = {
        "id": len(tareas) + 1,
        "descripcion": tarea.descripcion,
        "prioridad": tarea.prioridad,
        "estado": "Pendiente"
    }

    tareas.append(nueva)

    return nueva


@app.get("/tareas/{id}")
def encontrar_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea

    return {"mensaje": "Tarea no encontrada"}


@app.post("/usuarios")
def crear_usuario(usuario: Usuario):

    return {
        "mensaje": "Usuario creado",
        "usuario": usuario
    }


@app.put("/tareas/{id}")
def actualizar_tarea(id: int, tarea: Tarea):

    if 1 <= id <= len(tareas):

        tareas[id-1]["descripcion"] = tarea.descripcion
        tareas[id-1]["prioridad"] = tarea.prioridad

        return {
            "mensaje": "Tarea actualizada",
            "tarea": tareas[id-1]
        }

    return {
        "mensaje": "Tarea no encontrada"
    }


@app.delete("/tareas/{id}")
def eliminar_tarea(id: int):
    if 1 <= id <= len(tareas):
        tareas.pop(id-1)
        return {"mensaje": "Tarea eliminada"}

    return {"mensaje": "Tarea no encontrada"}


@app.get("/saludar")
def saludar(nombre: str):
    return {"mensaje": f"Hola {nombre}"}


@app.get("/buscar")
def buscar(texto: Optional[str] = None):
    return {"busqueda": texto}


@app.get("/par")
def es_par(numero: int):
    return {"numero": numero,
            "es_par": numero % 2 == 0}


@app.get("/saludo")
def saludo(nombre: Optional[str] = "Usuario"):
    return {"mensaje": "Hola " + nombre}


@app.get("/filtrar/estado")
def filtrar_estados(estado: str):
    return [
        tarea
        for tarea in tareas
        if tarea["estado"].lower() == estado.lower()
    ]


@app.get("/tareas/buscar")
def buscar_tareas(texto: str):
    return [
        tarea
        for tarea in tareas
        if texto.lower() in tarea["descripcion"].lower()
    ]
