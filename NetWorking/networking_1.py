import requests
import re

sum = input('Введіть сумму в грн:  ')

str = requests.get('https://api.monobank.ua/bank/currency')
info = str.text

pattern = re.findall(r'"currencyCodeA":840,"currencyCodeB":980,[\w:"]+,"rateBuy":([\d\s.]+)', info)

result = float(sum)/float(pattern[0])
print(result)



