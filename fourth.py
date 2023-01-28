import re

def validation():
    parol = input('Введіть пароль: ')
    pattern = r'^[A-Z][0-9]{3,5}[+_^$%][a-z]{5}$'
    result = re.findall(pattern, parol)
    if result:
        print('Пароль прийнято!')
    else:
        print('Невірний пароль!')


validation()
