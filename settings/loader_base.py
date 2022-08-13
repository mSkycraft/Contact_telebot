from settings.config import contacts_file
import json

users = {}
contact_book_admins = {}

def ImportUsers():
    global users
    _file = open(contacts_file,'r')
    users = json.load(_file)
    _file.close()

def Load_base():
    try:
        ImportUsers()
        print(f'Импорт контактов выполнен')
    except:
        print(f'Ошибка в импорте базы контактов')