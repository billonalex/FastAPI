from typing import Optional, List

from pydantic import BaseModel

class User(BaseModel):
    idutilisateur: int
    nom: Optional[str]
    prenom: Optional[str]
    adresse: Optional[str]
    codepostal: Optional[int]
    ville: Optional[str]
    pays: Optional[str]
    telephone: Optional[str]
    mail: Optional[str]
    username: Optional[str]
    disabled: Optional[bool] = None
    password: Optional[str]

class UserList(BaseModel):
    utilisateurs: List[User]
    nb_row: int