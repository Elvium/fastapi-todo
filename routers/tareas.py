from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from sqlalchemy import select
from services.tareas import obtener_tarea_service

from database.database import get_db
from models.tarea import Tarea as TareaModel


router = APIRouter(
    prefix="/tareas",
    tags=["Tareas"]
)


# ===========================
# SCHEMAS PYDANTIC
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

    class Config:
        from_attributes = True


# ===========================
# ENDPOINTS
# ===========================


# GET TODAS LAS TAREAS
@router.get("/", response_model=list[TareaResponse])
def obtener_tareas(
    db: Session = Depends(get_db)
):

    stmt = select(TareaModel)

    result = db.execute(stmt)

    tareas = result.scalars().all()

    return tareas


# GET POR ID
@router.get("/{id}", response_model=TareaResponse)
def obtener_tarea(
    id: int,
    db: Session = Depends(get_db)
):
    tarea = obtener_tarea_service(db, id)

    if tarea is None:

        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return tarea


# CREAR TAREA

@router.post(
    "/",
    response_model=TareaResponse,
    status_code=201
)
def crear_tarea(
    tarea: Tarea,
    db: Session = Depends(get_db)
):

    nueva = TareaModel(

        descripcion=tarea.descripcion,

        prioridad=tarea.prioridad,

        estado="Pendiente"

    )

    db.add(nueva)

    db.commit()

    db.refresh(nueva)

    return nueva


@router.put("/{id}", response_model=TareaResponse)
def actualizar_tarea(
    id: int,
    tarea: Tarea,
    db: Session = Depends(get_db)
):

    stmt = select(TareaModel).filter(
        TareaModel.id == id
    )

    result = db.execute(stmt)

    tarea_db = result.scalars().first()

    if tarea_db is None:

        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    tarea_db.descripcion = tarea.descripcion
    tarea_db.prioridad = tarea.prioridad

    db.commit()

    db.refresh(tarea_db)

    return tarea_db


@router.delete("/{id}", status_code=204)
def eliminar_tarea(
    id: int,
    db: Session = Depends(get_db)
):

    stmt = select(TareaModel).filter(
        TareaModel.id == id
    )

    result = db.execute(stmt)

    tarea = result.scalars().first()

    if tarea is None:

        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    db.delete(tarea)

    db.commit()
