from fastapi import APIRouter
from config.db import client
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.user import User
from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from config.functions import hash_password,verify_password,create_access_token
from dotenv import load_dotenv
import os
load_dotenv()

Rout=APIRouter()
SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES =int(os.getenv('ACCESS_TOKEN_EXPIRES_IN', '300'))
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # type: ignore
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    user = client.jwt_data.users.find_one({"username": username})
    if not user:
        raise credentials_exception
    return user


@Rout.get("/")
def root():
    return {"msg":"hello"}

@Rout.post("/signup")
def create_user(user: User):
    try:
        # Hash the password securely
        user.password = hash_password(user.password)
        client.jwt_data.users.insert_one(dict(user))
        return {"message": "User created successfully"}
    except Exception as e:
        # Convert exception to string for response
        raise HTTPException(status_code=500, detail=str(e))

@Rout.post("/login")
def login(user: User):
    try:
        find_user = client.jwt_data.users.find_one({"username": user.username})
        if not find_user:
            raise HTTPException(status_code=400, detail="User not found")
       
        if verify_password(user.password,find_user.get("password")):
            acess_token_expire=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES )
            access_token = create_access_token(
            data={"sub": find_user["username"]}, expires_delta=acess_token_expire)
            return {"access_token": access_token, "token_type": "bearer"}
            
        return {"message": "user not found or password is wrong."}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
    
