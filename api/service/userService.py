from fastapi import APIRouter, Depends
from models.response import Response

from models.user import User, UserList

import repository.authRepository as authRepository

from repository.userRepository import UserRepository
# Injection des repository
userRepository = UserRepository()

utilisateur = APIRouter(
    prefix="/utilisateur",
    tags=["Utilisateurs"],
    responses={404: {"description": "Not found"}},
)

@utilisateur.get(
    path="/",
    name="Récupération des utilisateurs",
    description="Permet la récupération des utilisateurs.",
    response_model=UserList
)
def get_users(current_user: User = Depends(authRepository.get_current_active_user)):
    return userRepository.get_users()

@utilisateur.get(
    path="/username/{username}",
    name="Vérification de l'existence d'un utilisateur par son username",
    description="Permet la vérification de l'existence d'un utilisateur par son username",
    response_model=Response
)
def get_users(username: str):
    return userRepository.usernameExists(username)

@utilisateur.put(
    path="/{idutilisateur}/password",
    name="Modification d'une propriété d'un utilisateur",
    description="Permet la modification d'une propriété d'un utilisateur.",
    response_model=Response
)
def update_password(idutilisateur: int, password: str, current_user: User = Depends(authRepository.get_current_active_user)):
    hashed_password = authRepository.get_password_hash(password)
    return userRepository.change_password(idutilisateur, hashed_password)