import uvicorn


uvicorn.run(
    'task.app:app',
    reload=True
)
