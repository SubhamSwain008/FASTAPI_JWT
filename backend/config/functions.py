from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import jwt
from dotenv import load_dotenv
import os
load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRES_IN', '300'))
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
password_context =  CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str) -> str:
    
    return password_context.hash(password)


def verify_password(passsword:str,password2:str):
    
    
    return password_context.verify(passsword,password2)

def create_access_token(data:dict,expires_delta:timedelta |None=None): 
    to_encode = data.copy()
    expire=datetime.now(timezone.utc)+ (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})#adds expiration payload to the token
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # type: ignore
