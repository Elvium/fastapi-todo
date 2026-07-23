from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from database.database import get_db


router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)

tareas = []


# ===========================
# MODELOS
# ===========================

class Tarea(BaseModel):
    descripcion: str = Field(
        min_length=5,
        max_length=100,
        description="Descripción resumida de la tarea"
    )

    prioridad: int = Field(
        ge=1,
        le=5,
        description="Prioridad entre 1 y 5"
    )


class TareaResponse(BaseModel):
    id: int
    descripcion: str
    prioridad: int
    estado: str


# ===========================
# ENDPOINTS
# ===========================

@router.get("/", response_model=list[TareaResponse])
def obtener_tareas(db: Session = Depends(get_db)):
    return tareas


@router.get("/{id}", response_model=TareaResponse)
def obtener_tarea(id: int, db: Session = Depends(get_db)):

    for tarea in tareas:
        if tarea["id"] == id:
            return tarea

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )


@router.post(
    "/",
    response_model=TareaResponse,
    status_code=201
)
def crear_tarea(
    tarea: Tarea,
    db: Session = Depends(get_db)
):

    nueva = Tarea(
        descripcion=tarea.descripcion,
        prioridad=tarea.prioridad,
        estado="Pendiente"
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


@router.put("/{id}", response_model=TareaResponse)
def actualizar_tarea(id: int, tarea: Tarea, db: Session = Depends(get_db)):

    for item in tareas:

        if item["id"] == id:

            item["descripcion"] = tarea.descripcion
            item["prioridad"] = tarea.prioridad

            return item

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )


@router.delete("/{id}", status_code=204)
def eliminar_tarea(id: int, db: Session = Depends(get_db)):

    for indice, tarea in enumerate(tareas):

        if tarea["id"] == id:

            tareas.pop(indice)

            return None

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )


# ===========================
# FILTROS
# ===========================

@router.get("/buscar/")
def buscar_tareas(texto: str, db: Session = Depends(get_db)):

    return [
        tarea
        for tarea in tareas
        if texto.lower() in tarea["descripcion"].lower()
    ]


@router.get("/estado/")
def filtrar_estado(estado: str):

    return [
        tarea
        for tarea in tareas
        if tarea["estado"].lower() == estado.lower()
    ]
