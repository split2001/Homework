from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()  # инициализируем приложение


@app.get('/')
async def welcome():
    return {'Главная страница'}


@app.get('/user/admin')
async def admin():
    return {'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def userid(user_id: int = Path(ge=1, le=100, description='Enter User ID', example=1)):
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get('/user/{username}/{age}')
async def user(name: Annotated[str, Path(ge=5, le=20, description='Enter username', example='UrbanUser')],
               age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    return {f'Информация о пользователе. Имя:{name}, Возраст:{age}'}


# запуск
# в терминале ввод python -m uvicorn Python_Homework.Module16.homework2m16_fast_api:app
