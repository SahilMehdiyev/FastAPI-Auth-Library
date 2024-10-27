from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from schemas import UserCreate, UserLogin, Token
from auth import authenticate_user, create_access_token, get_current_user
from models import create_user, fake_users_db



app = FastAPI()

@app.post('/register', response_model=Token)
def register(user:UserCreate):
    if user.username in fake_users_db:
        raise HTTPException(status_code=400, detail= 'Username already exists')
    
    create_user(user.username, user.password)
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}


@app.post('/login', response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}



@app.get('/protected')
async def protected_route(current_user: UserLogin = Depends(get_current_user)):
    return {"message": f'Hello, {current_user.username}! This is a protected route '}