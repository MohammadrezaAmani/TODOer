from fastapi import FastAPI

from todoer.routes.api import users_router

app = FastAPI()

app.include_router(users_router)
