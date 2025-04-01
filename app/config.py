import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Bank Branch API"
    admin_email: str = "admin@bankapi.com"
    
    class Config:
        env_file = ".env"

settings = Settings()