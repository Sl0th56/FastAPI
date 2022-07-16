import os

from pydantic import BaseSettings
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = f'{Path(__file__).parents[1]}/'
path = os.path.join(dir_path, '.env')
DB_NAME = f'fastapi_app.db'

class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url = f'sqlite:///{root_dir}' + DB_NAME

settings = Settings()
