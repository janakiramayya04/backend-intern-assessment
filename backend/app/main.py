from fastapi import FastAPI
# from app.api.router import user, item
# from app.core.database import engine, Base
import logging
logging.basicConfig(level=logging.INFO)
app = FastAPI()
# Base.metadata.create_all(bind=engine)
# app.include_router(user.router)
# app.include_router(item.router)
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}