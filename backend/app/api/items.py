from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from jose import jwt, JWTError
from sqlalchemy import select

from app.core import database, config
from app.api.auth import oauth2_scheme
from app.models import models
from app.schemas import schemas

router = APIRouter(tags=["Items"])



async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(database.get_db)
):
    try:
        payload = jwt.decode(
            token,
            config.settings.SECRET_KEY,
            algorithms=[config.settings.ALGORITHM]
        )
        user_email = payload.get("sub")
        if user_email is None:
            raise HTTPException(status_code=401, detail="Invalid credential")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credential")

    result = await db.execute(
        select(models.User).where(models.User.email == user_email)
    )
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user


@router.post("/items/", response_model=schemas.ItemResponse)
async def create_item(
    item: schemas.ItemCreate,
    db: AsyncSession = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_item = models.Item(**item.dict(), owner_id=current_user.id)
    db.add(new_item)

    await db.commit()
    await db.refresh(new_item)

    return new_item



@router.get("/items/", response_model=List[schemas.ItemResponse])
async def read_items(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role == "admin":
        result = await db.execute(
            select(models.Item).offset(skip).limit(limit)
        )
        return result.scalars().all()

    result = await db.execute(
        select(models.Item)
        .where(models.Item.owner_id == current_user.id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()



@router.delete("/items/{item_id}")
async def delete_item(
    item_id: int,
    db: AsyncSession = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    
    result = await db.execute(
        select(models.Item).where(models.Item.id == item_id)
    )
    item = result.scalar_one_or_none()

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    
    if current_user.role != "admin" and item.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this item")

    await db.delete(item)
    await db.commit()

    return {"detail": "Item deleted"}
