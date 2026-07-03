from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def inicio():
    return {"mensaje": "Hola, Ronaldo. Mi primera API con FastAPI"}


@app.get("/saludo")
def saludo():
    return {"mensaje": "Bienvenido al mundo del backend con Python"}


@app.get("/saludo/{nombre}")
def saludo_nombre(nombre: str):
    return {"mensaje": f"Te amo mucho {nombre}, Estoy haciendo esto con Fastapi y prometo que encontrare trabajo pronto"}


@app.get("/suma/{a}/{b}")
def suma(a: int, b: int):
    return {
        "resultado": a + b
    }


@app.get("/multiplicar/{a}/{b}")
def multiplicar(a: int, b: int):
    return {
        "resultado": a * b
    }


@app.get("/resta/{a}/{b}")
def resta(a: int, b: int):
    return {
        "resultado": a - b
    }


@app.get("/par/{a}")
def par(a: int):

    return {"numero": a,
            "es_par": a % 2 == 0}
