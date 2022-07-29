from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    phone: str

    class Config:
        orm_mode = True


class JSONResponseModel(BaseModel):
    data: int
    code: int


class UserOutModel(BaseModel):
    email: str
    name: str
