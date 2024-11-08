from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from models import User
from schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):  # подключается к базе данных в момент обращения при
    # помощи функции get_db
    users = db.scalar(select(User).all())
    return users  # возвращать список всех пользователей из БД


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):  # подключается к базе данных в момент
    # обращения при помощи функции get_db
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)]):  # подключается к базе данных в момент обращения при
    # помощи функции get_db
    pass


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], user_id: int):  # подключается к базе данных в момент
    # обращения при помощи функции get_db
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='User was not found'
    )


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)]):  # подключается к базе данных в момент обращения
    # при помощи функции get_db
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='User was not found'
    )
