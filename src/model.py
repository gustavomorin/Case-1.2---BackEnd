from pydantic import BaseModel

class User(BaseModel):
    email: str
    senha: str
    celular: str
    nome: str
    cep: str
    is_employee: bool

users_model: list[User]=[
    User(email="andre@bionutri.com",senha="bionutri",celular="9963037895",nome="andre",cep="0331300",is_employee=True)
]


