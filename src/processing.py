from datetime import datetime
from typing import Any, Hashable


def filter_by_state(transactions: list[dict[Hashable, Any]], state: str = "EXECUTED") -> list[dict[Hashable, Any]]:
    """
      Принимает список словарей и опционально значение для ключа 'state'(по умолчанию 'EXECUTED'),
     и возвращает новый список словарей, содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению.
    """

    return [data for data in transactions if data.get("state") == state]


def sort_by_date(operations: list[dict[Hashable, Any]], reverse_order: bool = True) -> list[dict[Hashable, Any]]:
    """
      Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание),
    и возвращает новый список, отсортированный по дате (date).
    """
    # Преобразуем строки дат в объекты datetime для сортировки
    for item in operations:
        date_str = item["date"]
        if "Z" in date_str:
            item["date"] = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        else:
            item["date"] = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

    # Сортируем список словарей по ключу 'date' и "id"(в случае одинаковых дат)
    sorted_list: list[dict[Hashable, Any]] = sorted(
        operations, key=lambda x: (x["date"], x["id"]), reverse=reverse_order
    )

    # Преобразуем обратно в строковый формат
    for item in sorted_list:
        item["date"] = item["date"].strftime("%Y-%m-%dT%H:%M:%S.%f")

    return sorted_list
