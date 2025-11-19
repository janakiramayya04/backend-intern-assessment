import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
print("Loading environment variables from:", env_path)
load_dotenv(dotenv_path=env_path)
class Settings:
    PROJECT_NAME: str = "Backend Task"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_URL: str = ""

    SECRET_KEY: str = ""
    ALGORITHM: str = " "
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
