from fastapi import FastAPI, Depends
from routers.tareas import router as tareas_router
from routers.usuarios import router as usuarios_router
from routers.depends import obtener_mensaje, obtener_fecha, obtener_autor, verificar_usuario

app = FastAPI()


@app.get("/mensaje")
def mensaje(mensaje=Depends(obtener_mensaje)):

    return {
        "Mensaje": mensaje
    }


@app.get("/autor")
def autor(autor=Depends(obtener_autor)):

    return {
        "Autor": autor
    }


@app.get("/verificar")
def verificar(verificar=Depends(verificar_usuario)):

    return {
        "acceso": verificar
    }


@app.get("/hora")
def hora(hora=Depends(obtener_fecha)):

    return {
        "hora": hora
    }


app.include_router(tareas_router)
app.include_router(usuarios_router)
