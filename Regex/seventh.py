import re

def find():
    pattern = r'[0-9]+'
    str =  '''Alex - 1700грн Artem - 8000грн Ernest - 95000грн'''

    result = re.findall(pattern, str)
    for ind, val in enumerate(result, start = 1):
        print(f'{ind}) {val}')
    
find()
