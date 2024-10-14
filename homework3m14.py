from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup  # машина состояний
from aiogram.dispatcher import FSMContext  # машина состояний
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # импорт для клавиатуры
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio


api = '8013988302:AAFGF77NP7mI2pRi8WvqQ6TIvl3-4BbPIs8'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)  # инициализируем клавиатуру как экземпляр класса
button_1 = KeyboardButton(text='Рассчитать')  # создаем кнопку с параметром text
button_2 = KeyboardButton(text='Информация')  # создаем кнопку с параметром text
button_3 = KeyboardButton(text='Купить')  # создаем кнопку с параметром text
# kb.add(button_1) добавляем кнопку в клавиатуру
# kb.add(button_2) добавляем кнопку в клавиатуру
kb.add(button_1, button_3)  # добавляем кнопки в один ряд
kb.add(button_2)

ikb = InlineKeyboardMarkup(resize_keyboard=True)  # инициализируем ин лайн-клавиатуру как экземпляр класса
inl_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')  # создаем инлайн-клавиатуру
inl_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')  # создаем ин лайн-клавиатуру
ikb.add(inl_button, inl_button2)  # добавляем ин лайн-клавиатуру

ikb_2 = InlineKeyboardMarkup(resize_keyboard=True)  # инициализируем ин лайн-клавиатуру как экземпляр класса
inl_button3 = InlineKeyboardButton(text='Product1', callback_data='product_buying')  # создаем инлайн-клавиатуру
inl_button4 = InlineKeyboardButton(text='Product2', callback_data='product_buying')  # создаем ин лайн-клавиатуру
inl_button5 = InlineKeyboardButton(text='Product3', callback_data='product_buying')  # создаем ин лайн-клавиатуру
inl_button6 = InlineKeyboardButton(text='Product4', callback_data='product_buying')  # создаем ин лайн-клавиатуру
ikb_2.row(inl_button3, inl_button4, inl_button5, inl_button6)  # добавляем ин лайн-клавиатуру


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=['Рассчитать'])  # параметр, когда функция реагирует на определенные сообщения
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ikb) # вызываем инлайн-клавиатуру для вывода на экран user


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    with open('files/1.jpeg', 'rb') as img:
        await message.answer_photo(img, 'Product1 - белково-углеводный продукт для набора '
                                        'массы Gainer Optimum Nutrition.Цена: 6100.')
    with open('files/2.jpg', 'rb') as img2:
        await message.answer_photo(img2, 'Product2 - универсальный источник дополнительного белка Whey Ptotein.'
                                         'Цена: 4200.')
    with open( 'files/3.jpg','rb') as img3:
        await message.answer_photo(img3, 'Product3 - 100% чистый микронизированный креатин Creatinr HardLine.'
                                         'Цена: 2700.')
    with open('files/4.jpg', 'rb') as img4:
        await message.answer_photo(img4, 'Product4 - Аминокислоты BCAA.Цена: 3800.')
    await message.answer('Выберите продукт для покупки:', reply_markup=ikb_2)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


@dp.callback_query_handler(text='formulas')  # handler для инлайн-клавиатур с параметром равным callback_data кнопки
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()  # чтобы кнопка не завершала работу


@dp.callback_query_handler(text='calories')  # handler для инлайн-клавиатур с параметром равным callback_data кнопки
async def set_age(call):
    await call.message.answer('Введите,пожалуйста, свой возраст.')  # вывод сообщения пользователю
    await UserState.age.set()  # ожидаем ввода возраста в атрибут UserState.age и устанавливаем его


@dp.message_handler(state=UserState.age)  # handler, который откликается на переданное состояние UserState.age
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Отлично! Теперь укажите свой рост.')
    await UserState.growth.set()  # ожидаем ввода роста в атрибут UserState.growth и устанавливаем его


@dp.message_handler(state=UserState.growth)  # handler, который откликается на переданное состояние UserState.growth
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Супер. Последний этап - Ваш вес.')
    await UserState.weight.set()  # ожидаем ввода веса в атрибут UserState.weight и устанавливаем его


@dp.message_handler(state=UserState.weight)  # handler, который откликается на переданное состояние UserState.weight
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()  # запоминаем в переменную data все ранее введённые состояния
    # составляем формулу использую ключи к словарю с состояниями
    formula = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма калорий:{formula}')
    await state.finish()  # закрываем машину состояний


@dp.message_handler(commands=['start'])  # параметр, когда функция отрабатывает по определенной команде
async def start_2(message):
    await message.answer(f'Привет, {message.from_user.username}.Я бот,который помогает следить за здоровьем.'
                         f' Выберите команду,'
                         'чтобы начать.', reply_markup=kb)  # вызываем клавиатуру для вывода на экран user


@dp.message_handler()  # обработчик всех сообщений, ставим в конец, чтобы не перехватывал остальные команды.
async def all_massages(message):
    await message.answer('Введите команду /start.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
