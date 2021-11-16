from typing import Optional, List

from pydantic import BaseModel

from models.user import User

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    idutilisateur: Optional[str] = None