from fastapi import FastAPI
from db import engine, Base
from routes import user

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API running 🚀"}

app.include_router(user.router)