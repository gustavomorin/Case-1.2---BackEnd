from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class Register(BaseModel):
    email: str
    senha: str
    celular: str
    nome: str
    cep: str

