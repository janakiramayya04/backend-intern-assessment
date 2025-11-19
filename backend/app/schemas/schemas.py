from pydantic import BaseModel, EmailStr
from typing import List, Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    
class ItemResponse(ItemBase):
    id: int
    owner_id: int
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: str = "user"  

class UserResponse(UserBase):
    id: int
    role: str
    items: List[ItemResponse] = []
    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str