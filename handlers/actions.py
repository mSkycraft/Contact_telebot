from aiogram import types
import json
from settings import dp,contacts_file,users



@dp.message_handler(text="Safe")
@dp.message_handler(commands=['Safe'])
def Safe_base():
    global users
    _file = open(contacts_file,'w')
    json.dump(users,_file)
    _file.close()

@dp.message_handler(regexp=r'^Add')
async def add_user(message: types.Message):
    global users
    add_message = message.text[4:].split(', ')
    id_user = message["from"]["id"]
    contact = ''
    for data in add_message:
        contact  += data + ';'
    if(id_user not in users.keys()):
        users[id_user] = []
        users[id_user].append(contact)
    else:
        users[id_user].append(contact)
    await message.answer(text=f"Пользователь {add_message[0]} добавлен")

@dp.message_handler(regexp=r'^Search')
async def search_user(message: types.Message):
    global users
    id_user = message["from"]["id"]
    for contact in users[id_user]:
        if(contact.find(message.text[7:])!=-1):
            await message.answer(text=f'Найден контакт {contact}')

@dp.message_handler(regexp=r'^Delete')
async def search_user(message: types.Message):
    global users
    id_user = message["from"]["id"]
    for i in range(len(users[id_user])):
        if(users[id_user][i].find(message.text[7:])!=-1):
            await message.answer(text=f'Удален контакт {users[id_user][i]}')
            del users[id_user][i]
            break

@dp.message_handler(commands=['Test'])
async def test_bot(message:types.Message):
    await message.answer(text='Бот активен')
