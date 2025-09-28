from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str
    email:str
class LoginUser(BaseModel):
    username:str
    password:str
