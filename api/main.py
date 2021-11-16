import os

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

# Import des services
from service.authService import auth
from service.defaultService import DefaultService
from service.userService import utilisateur
from db.init_db import init_db
from db.db import dump_db

# Initialisation de la base de données si elle n'existe pas
init_db()
dump_db()


# Création de l'API
app = FastAPI(title="API - FastAPI", version="0.1.0",
              description="API de service.")

origins = []
ports = ["3002", "3001", "3000"]
urls = ["http://localhost", "http://127.0.0.1"]

for url in urls:
    origins.append(url)
    for port in ports:
        origins.append(url + ":" + port)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Injection des services
app.include_router(auth)
DefaultService(app)
app.include_router(utilisateur)


#Execution de l'API
#Commandes à commenter pour l'utilisation de Docker
if(__name__ == "__main__"):
    uvicorn.run(app, host="127.0.0.1", port=8888)