from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router




@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Heeey... we clean this mess. Now all good')
    await create_tables()
    print("hello... We starting here")
    yield
    print("Выключение") 
    # Clean up the ML models and release the resources

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
