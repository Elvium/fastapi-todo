from database.database import SessionLocal
from models.tarea import Tarea
from sqlalchemy import select

db = SessionLocal()

stmt = select(Tarea)

resultado = db.execute(stmt)

tareas = resultado.scalars().all()

for tarea in tareas:
    print(tarea.descripcion)

stmt2 = select(Tarea).filter(Tarea.id == 1)

resultado2 = db.execute(stmt2)

tarea = resultado2.scalars().first()

if tarea is not None:
    print(tarea)
    print(tarea.descripcion)
else:
    print("No hay tarea con dicho ID")

db.close()
