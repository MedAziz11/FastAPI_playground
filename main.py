from fastapi import FastAPI, status
from typing import Optional
from fastapi import Response

from schema import  RegisterSchema


app = FastAPI()


@app.post('api/register/{id}')
async def register_user(payload: RegisterSchema):
    if id==1:
        return Response({'error':'user already exists'}, status.HTTP_400_BAD_REQUEST)
    return Response({'created':f'register completed {payload.full_name}'}, status.HTTP_201_CREATED)