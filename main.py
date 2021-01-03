from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from schema import  UserSchema
from models import User
from mongoengine.errors import NotUniqueError


app = FastAPI()


@app.post('/api/register')
async def register_user(payload: UserSchema):
    try:
        user = User(full_name=payload.full_name, email=payload.email)
        user.save()
        registeredUser = UserSchema(full_name=user.full_name, email= user.email)
    except NotUniqueError:
        return JSONResponse(status_code=404, content={"error": "Email already used"})
    return JSONResponse(content=jsonable_encoder(registeredUser) , status_code=201)
