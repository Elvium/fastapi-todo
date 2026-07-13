from fastapi import APIRouter
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

router = APIRouter()


class Usuario(BaseModel):
    nombre: str = Field(
        min_length=3,
        max_length=50
    )
    edad: int = Field(
        ge=18,
        le=120
    )
    email: EmailStr
    telefono: Optional[str] = None


class UsuarioResponse(BaseModel):
    nombre: str


@router.post("/usuarios", response_model=UsuarioResponse)
def crear_usuario(usuario: Usuario):

    return {

        "nombre": usuario.nombre
    }


@router.get("/saludo")
def saludo(nombre: Optional[str] = "Usuario"):
    return {"mensaje": "Hola " + nombre}
