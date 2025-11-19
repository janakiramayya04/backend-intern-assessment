import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME: str = "Backend Task"
    PROJECT_VERSION: str = "1.0.0"

    
    DATABASE_URL: str = os.getenv("DATABASE_URL") or ""
    SECRET_KEY: str = os.getenv("SECRET_KEY") or ""
    ALGORITHM: str = os.getenv("ALGORITHM") or ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

settings = Settings()