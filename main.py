from fastapi import FastAPI, BackgroundTasks
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from fastapi_mail import FastMail, MessageSchema,ConnectionConfig

from schema import  UserSchema
from models import User
from mongoengine.errors import NotUniqueError


app = FastAPI()

conf = ConnectionConfig(
    MAIL_USERNAME = "clab.dev20@gmail.com",
    MAIL_PASSWORD = "clabdev123",
    MAIL_FROM = "clab.dev20@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",    
    MAIL_TLS = True,
    MAIL_SSL = False

)

@app.post('/api/register')
async def register_user(background_tasks: BackgroundTasks, payload: UserSchema)-> JSONResponse:
    try:
        user = User(full_name=payload.full_name, email=payload.email)
        user.save()
        registeredUser = UserSchema(full_name=user.full_name, email=user.email)
    except NotUniqueError:
        return JSONResponse(status_code=404, content={"error": "Email already used"})

    message = MessageSchema(
    subject="Registered",
    recipients=[payload.email,],
    body=f"thanks {payload.full_name} for registering in our datascience event" 
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message,message)
    
    
    return JSONResponse(content=jsonable_encoder(registeredUser) , status_code=201)
