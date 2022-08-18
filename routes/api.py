from fastapi import APIRouter
from src.endpoints import userinfo

router = APIRouter()

router.include_router(userinfo.router)