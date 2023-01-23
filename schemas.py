from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_model = True
        schema_extra = {
            'example': {
                "username": "Guilherme",
                "email" : "guibrbr@gmail.com",
                "password" : "password",
                "is_staff": False,
                "is_activate": True
            }
        }



class Settings(BaseModel):
    authjwt_secret_key:str='fb4e96406c644330bec739634d43a5cdec41ad0dcc6ce4fa7d604b1c0ddaad5a'



class LoginModel(BaseModel):
    username:str
    password:str