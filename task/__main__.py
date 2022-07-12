import uvicorn
from .settings import settings

from db import connection_db
from .script.create_db import create_tables

create_tables()
connection_db()

uvicorn.run(
    'task.app:app',
    host=settings.server_host,
    port=settings.server_port,
    reload=True,
)
