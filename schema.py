from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    """Registration schema"""
    full_name: str
    email: EmailStr

