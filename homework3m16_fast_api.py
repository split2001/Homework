from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()  # инициализируем приложение

users = {'1': 'Имя: Example, возраст: 18'}

#  4 ключевых запроса
#  get - получение ответа от сервера (адрес в строке ?переменная=значение)
#  put - обновление данных (изменить существующие данные, обновить информацию о пользователе)
#  delete - удаление данных
#  post - создание данных (создание нового пользователя или записи)


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_message(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
               age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_message(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
               age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)],
                         user_id: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"


@app.delete('/user/{user_id}')
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'



# запуск
# в терминале ввод python -m uvicorn Python_Homework.Module16.homework3m16_fast_api:app