from typing import Optional, List
from fastapi import FastAPI, Depends

from repository.authRepository import oauth2_scheme

def DefaultService(app: FastAPI):    
    @app.get("/items/")
    async def read_items(token: str = Depends(oauth2_scheme)):
        return {"token": token} 

    @app.get("/")
    async def read_items():
        return "Ajouter /docs ou /redoc à l'URL pour accéder à la documentation"