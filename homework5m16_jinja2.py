from fastapi import FastAPI, status, Body, HTTPException, Request, Form, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates  # позволяет подключить директорию для обработки templates
from typing import Annotated


app = FastAPI()  # инициализируем приложение

templates = Jinja2Templates(directory=r'C:\Users\davla\PycharmProjects\pythonProject2\Python_Homework\Module16'
                                      r'\homework5m16_jinja2\templates2')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


#  4 ключевых запроса
#  get - получение ответа от сервера (адрес в строке ?переменная=значение)
#  put - обновление данных (изменить существующие данные, обновить информацию о пользователе)
#  delete - удаление данных
#  post - создание данных (создание нового пользователя или записи)


@app.get('/')
async def get_smth(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]):
    user_id = len(users) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)],
        user_id: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail=f'User {user_id} was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.pop(user_id - 1)
            return user
    raise HTTPException(status_code=404, detail='User was not found')

# запуск
# в терминале ввод python -m uvicorn Python_Homework.Module16.homework5m16_jinja2.homework5m16_jinja2:app
