from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from service.tareas import obtener_tarea_service, obtener_tareas_service, crear_tarea_service, eliminar_tarea_service, actualizar_tarea_service
from database.database import get_db


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

    return obtener_tareas_service(db)


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

    return crear_tarea_service(tarea, db)


@router.put("/{id}", response_model=TareaResponse)
def actualizar_tarea(
    id: int,
    tarea: Tarea,
    db: Session = Depends(get_db)
):

    tarea_update = actualizar_tarea_service(id, tarea, db)

    if tarea_update is None:

        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )

    return tarea_update


@router.delete("/{id}", status_code=204)
def eliminar_tarea(
    id: int,
    db: Session = Depends(get_db)
):
    tarea_del = eliminar_tarea_service(id, db)

    if tarea_del is None:

        raise HTTPException(
            status_code=404,
            detail="Tarea no encontrada"
        )
    return None
