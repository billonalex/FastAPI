from datetime import timedelta
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from models.token import Token

from models.user import User
import repository.authRepository as authRepository
from repository.userRepository import UserRepository
userRepository = UserRepository()

auth = APIRouter(
    tags=["Authentification"],
    responses={404: {"description": "Not found"}},
)

@auth.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authRepository.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=authRepository.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authRepository.create_access_token(
        data={
            "username": user.username, 
            "idutilisateur": user.idutilisateur
            }, 
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@auth.get("/users/me")
async def read_users_me(current_user: User = Depends(authRepository.get_current_active_user)):
    return current_user
