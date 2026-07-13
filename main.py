from fastapi import FastAPI
from routers.tareas import router as tareas_router
from routers.usuarios import router as usuarios_router


app = FastAPI()

app.include_router(tareas_router)
app.include_router(usuarios_router)
