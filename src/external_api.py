from typing import Dict

import os

import requests

import random

from dotenv import load_dotenv




# Загружаем переменную окружения
load_dotenv()

API_KEY = os.getenv("API_KEY")

def converting_amount_rubles(transaction: Dict[str, Dict[str, Dict[str, str]]]) -> float:
    """
      Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
     Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли
    """

    code_transaction = transaction['operationAmount']['currency']['code']

    if code_transaction == "RUB":
        return float(transaction['operationAmount']['amount'])

    elif code_transaction in ["USD", "EUR"]:
        to = "RUB"
        from_= code_transaction
        amount = transaction['operationAmount']['amount']

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"

        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            result = response.json()
            return float(result['result'])
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except requests.exceptions.RequestException as err:
            print(f"Other error occurred: {err}")
            return None
        except KeyError:
            print("Unexpected response format")
            return None

# # Прочитать все транзакции
# transactions_list = read_json_file('data/operations.json')
#
# # Выбрать случайную транзакцию
# random_transaction = random.choice(transactions_list)
#
# # Передать её в функцию
# amount_in_rubles = round(converting_amount_rubles(random_transaction), 2)
#
# print(f"Amount in rubles: {amount_in_rubles}")
