from mongoengine import Document, fields, connect

from dotenv import load_dotenv
import os

load_dotenv()
connect(host= os.getenv("URI"))


class User(Document):
    """User Document"""
    full_name= fields.StringField(required=True)
    email = fields.EmailField(required=True, unique=True)
    #created_at= fields.DateTimeField()

    meta ={
        'collection': 'Users'
    }


