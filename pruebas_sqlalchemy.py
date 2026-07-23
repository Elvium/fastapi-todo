from database.database import SessionLocal
from models.tarea import Tarea

db = SessionLocal()

nueva = Tarea(
    descripcion="Aprender PostgreSQL",
    prioridad=5,
    estado="Pendiente"
)


db.add(nueva)
db.commit()
db.refresh(nueva)


print(nueva.id)

db.close()
