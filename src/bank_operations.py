import re
from collections import Counter
from typing import Dict, List


def process_bank_search(data: List[Dict[str, str]], search: str) -> List[Dict[str, str]]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка.
    """
    if not search:
        return []
    result = [
        transaction for transaction in data if re.search(search, transaction["description"], flags=re.IGNORECASE)
    ]
    return sorted(result, key=lambda x: x["description"])


def process_bank_operations(data: List[Dict[str, str]], categories: list) -> dict:
    """
     Принимает список словарей с данными о банковских операциях и список категорий операций, и возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    descriptions = [transaction["description"] for transaction in data]
    filtered_descriptions = [desc for desc in descriptions if desc in categories]
    return dict(Counter(filtered_descriptions))
