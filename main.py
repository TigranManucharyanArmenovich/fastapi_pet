from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_database, drop_database
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_database()
    print("Ok we clean this mess")
    await create_database()    
    print("well boys.. we put this shit here... what to do now")
    yield
    print("bye bye")

app = FastAPI(lifespan=lifespan)

app.include_router(tasks_router)


