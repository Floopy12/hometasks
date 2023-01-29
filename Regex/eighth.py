import re


def diagnosis():
    pattern = r'^Ім\'я: ([А-яїі\']+)[ А-яіїІЇ\':0-9]+Діагноз: ([А-яіїІЇ\']+)$'
    str = 'Ім\'я: Максим Вік: 56 Місто: Київ Діагноз: Грип'

    result = list(re.match(pattern, str).group(1,2))
    print(result[0], result[1])
    

diagnosis()
