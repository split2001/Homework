from fastapi import FastAPI

app = FastAPI()  # инициализируем приложение


@app.get('/')
async def welcome():
    return {'Главная страница'}


@app.get('/user/admin')
async def admin():
    return {'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def userid(user_id):
    return {f"Вы вошли как пользователь № {user_id}"}


@app.get('/user')
async def user(name: str, age: int):
    return {f'Информация о пользователе. Имя:{name}, Возраст:{age}'}


# запуск
# в терминале ввод python -m uvicorn Python_Homework.Module16.homework1m16_fast_api:app
