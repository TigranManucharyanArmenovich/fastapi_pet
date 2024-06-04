from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional
engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


class TasksTable(Base):
    __tablename__ = "Tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)