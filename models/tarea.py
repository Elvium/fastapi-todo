from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
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
        String(100),
        nullable=False
    )

    prioridad: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    estado: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )


Base.metadata.create_all(bind=engine)
