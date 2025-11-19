from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.core import database, security
from app.models import models
from app.schemas import schemas

router = APIRouter(tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register", response_model=schemas.UserResponse)
async def register(
    user: schemas.UserCreate, 
    db: AsyncSession = Depends(database.get_db)
):
    
    result = await db.execute(
        select(models.User).where(models.User.email == user.email)
    )
    db_user = result.scalar_one_or_none()

    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

   
    hashed_pwd = security.get_password_hash(user.password)

    
    new_user = models.User(
        email=user.email,
        hashed_password=hashed_pwd,
        role=user.role
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


@router.post("/token", response_model=schemas.Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: AsyncSession = Depends(database.get_db)
):
    
    result = await db.execute(
        select(models.User).where(models.User.email == form_data.username)
    )
    user = result.scalar_one_or_none()

    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

   
    access_token = security.create_access_token(
        data={"sub": user.email, "role": user.role, "id": user.id}
    )

    return {"access_token": access_token, "token_type": "bearer"}
