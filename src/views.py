from fastapi import APIRouter, Response
import controllers
import model
import dtos

router = APIRouter()

@router.post("/users")
def registrar_usuario(body: dtos.Register):
    users = controllers.register_user(body)
    return {"status": "success"}

@router.post("/login")
def user_login(credentials: dtos.UserLogin, response: Response):
    return controllers.user_login(
        email = credentials.email, 
        password = credentials.password,
        response=response
    )
