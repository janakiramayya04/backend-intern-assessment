from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.core.database import engine, Base
from app.api.router import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up... Creating database tables...")
    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)
    print("Tables created successfully.")
    yield


app = FastAPI(title="Backend Task", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "API is running. Go to /docs for Swagger UI"}
