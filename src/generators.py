from typing import Any, Dict, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> iter:
    """
      Принимает на вход список словарей, представляющих транзакции, и  возвращает  итератор,
     который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD).
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction




def transaction_descriptions(transactions: List[Dict[str, Any]]) -> iter:
    """
      Генератор. Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction['description']



def card_number_generator(start: int, stop: int) -> iter:
    """
      Генератор. Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X— цифра номера карты.
     Может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    for number in range(int(start), int(stop) + 1):
        card_number = str(number).zfill(16)  # заполняем нулями до 16 цифр
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number
