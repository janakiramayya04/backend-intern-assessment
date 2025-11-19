from fastapi import APIRouter

from app.api.auth import router as auth_router
from app.api.items import router as items_router

router= APIRouter()

@router.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"} 

router.include_router(auth_router)
router.include_router(items_router)