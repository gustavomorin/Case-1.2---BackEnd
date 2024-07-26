from fastapi import FastAPI, Request
from views import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()



# class Hello(BaseModel):
#     photo: str
#     description: str
# @app.get("/hello")
# def hello(request: Request):
#     print (dict(request))
#     return {"name":"Gustavo"}

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)