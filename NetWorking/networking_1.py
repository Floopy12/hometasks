import requests
import re

sum = input('Введіть сумму в грн:  ')

str = requests.get('https://api.monobank.ua/bank/currency')

pattern = re.findall(r'"currencyCodeA":840,"currencyCodeB":980,[\w:"]+,"rateBuy":([\d\s.]+)', str.text)

result = float(sum)/float(pattern[0])
print(f'Ви отримаете {round(result, 2)}$ по курсу {pattern[0]}')



