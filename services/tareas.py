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
