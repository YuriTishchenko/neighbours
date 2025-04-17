import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = 'Neighbours API'
    database_url: str
    debug: bool = True
    environment: str = 'dev'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()