import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]
env = os.getenv("APP_ENV", "development")
env_file = BASE_DIR / f".env.{env}"

load_dotenv(env_file)

def get_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise RuntimeError(f"Variável de ambiente obrigatória não definida: {name}")
    return value

@dataclass(frozen=True)
class Settings:
    DB_HOST: str = get_env("DB_HOST")
    DB_PORT: int = int(get_env("DB_PORT"))
    DB_USER: str = get_env("DB_USER")
    DB_PASSWORD: str = get_env("DB_PASSWORD")
    DB_NAME: str = get_env("DB_NAME")

settings = Settings()