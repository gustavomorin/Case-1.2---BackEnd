import model
import dtos
from fastapi import Response

def register_user(infos: dtos.Register):
    new_user = model.User(**infos.__dict__, is_employee=False)
    model.users_model.append(new_user)
    return {"status": "success"}

def user_login(email:str, password:str, response:Response):
    for usr in model.users_model:
        if (usr.email == email and usr.senha == password):
            response.status_code = 200
            return{
                "status":"success",
                "message":"Usuario loggado com sucesso",
                "is_employees": usr.is_employee
            }
    response.status_code = 404
    return{
                "status":"success",
                "message":"Usuario não encontrado"
            }

