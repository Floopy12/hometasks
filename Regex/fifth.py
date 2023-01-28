import re

def company_name():
    pattern = r'^Компанія:([А-яії0-9 ]+):[А-яії0-9: ]+'
    str = input('Введіть інформацію про компанію: ')


    result = re.match(pattern, str)
    if result:
        print(result.group(1))
    else:
        print('Інформація про назву відсутня.')

company_name()