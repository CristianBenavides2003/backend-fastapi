from pydantic import BaseModel, Field

class UserBase(BaseModel):
    id: int
    nombre: str
    correo: str

class UserCreate(UserBase):
    id: int = Field(..., example=1)

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True