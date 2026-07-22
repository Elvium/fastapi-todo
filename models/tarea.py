from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from database.database import engine


class Base(DeclarativeBase):
    pass


class Tarea(Base):

    __tablename__ = "tareas"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    descripcion: Mapped[str] = mapped_column(
        String(100)
    )

    prioridad: Mapped[int] = mapped_column(
        Integer
    )

    estado: Mapped[str] = mapped_column(
        String(30)
    )


Base.metadata.create_all(bind=engine)
