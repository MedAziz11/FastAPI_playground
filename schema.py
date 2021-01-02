from pydantic import BaseModel, EmailStr

class RegisterSchema(BaseModel):
    """Registration schema"""
    full_name: str
    email: EmailStr

