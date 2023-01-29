import re


def hide_parol():
    pattern = r'^[A-z0-9]+: [A-z0-9-]+$'
    str = input('Введіть пароль: ')
    repl = 'Пароль'

    print(re.sub(pattern, repl, str))

hide_parol()