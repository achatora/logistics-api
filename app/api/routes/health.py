from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_db

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/health/db")
async def database_health_check(
    db: Annotated[AsyncSession, Depends(get_db)],
):
    await db.execute(text("SELECT 1"))
    return {"database": "connected"}
