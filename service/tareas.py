from sqlalchemy import select
from sqlalchemy.orm import Session

from models.tarea import Tarea as TareaModel


def obtener_tarea_service(
    db: Session,
    tarea_id: int
):
    stmt = select(TareaModel).filter(
        TareaModel.id == tarea_id
    )

    result = db.execute(stmt)

    tarea = result.scalars().first()

    return tarea


def obtener_tareas_service(
    db: Session
):
    stmt = select(TareaModel)

    result = db.execute(stmt)

    tareas = result.scalars().all()

    return tareas


def crear_tarea_service(
    datos: Tarea,
    db: Session
):
    nueva = TareaModel(

        descripcion=datos.descripcion,

        prioridad=datos.prioridad,

        estado="Pendiente"

    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def actualizar_tarea_service(
    id: int,
    tarea: TareaModel,
    db: Session
):

    tarea_db = obtener_tarea_service(db, id)
    if tarea_db is None:
        return None
    tarea_db.descripcion = tarea.descripcion
    tarea_db.prioridad = tarea.prioridad
    db.commit()
    db.refresh(tarea_db)

    return tarea_db


def eliminar_tarea_service(
    id: int,
    db: Session
):
    tarea_delete = obtener_tarea_service(db, id)
    if tarea_delete is None:
        return None
    db.delete(tarea_delete)
    db.commit()
