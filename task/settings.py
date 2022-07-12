import os

from pydantic import BaseSettings
from starlette.config import Config
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = f'{Path(__file__).parents[1]}/'
path = os.path.join(dir_path, '.env')
config = Config(f'{path}')

class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    database_url = f'sqlite:///{root_dir}' + config('DB_NAME', cast=str)

settings = Settings()
