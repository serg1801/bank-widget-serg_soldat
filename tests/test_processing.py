import pytest

from datetime import datetime

from src.processing import filter_by_state, sort_by_date


# Фикстура для предоставления тестовых данных
@pytest.fixture
def transactions():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

# Параметризированные тесты для различных значений статуса
@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]),
    ("CANCELED", [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]),
    ("PENDING", []),  # Проверка при отсутствии словарей с указанным статусом
])
def test_filter_by_state(transactions, state, expected):
    result = filter_by_state(transactions, state)
    assert result == expected

# Фикстура для предоставления тестовых данных
@pytest.fixture
def operations():
    return [
        {"id": 1, "date": "2022-03-01T12:30:00.000000"},
        {"id": 2, "date": "2022-01-15T08:45:00.000000"},
        {"id": 3, "date": "2022-03-01T12:30:00.000000"},  # одинаковая дата
        {"id": 4, "date": "2022-02-20T09:15:00.000000"}
    ]

# Тесты для различных условий сортировки
@pytest.mark.parametrize("reverse_order, expected_ids", [
    (True, [3, 1, 4, 2]),  # Убывающий порядок с учетом сортировки по id для одинаковых дат
    (False, [2, 4, 1, 3])  # Возрастающий порядок
])
def test_sort_by_date_order(operations, reverse_order, expected_ids):
    sorted_operations = sort_by_date(operations, reverse_order)
    result_ids = [op["id"] for op in sorted_operations]
    assert result_ids == expected_ids

# Проверка корректности сортировки при одинаковых датах
@pytest.mark.parametrize("reverse_order, expected", [(True, [5, 3, 1]), (False, [2, 4, 1])])
def test_sort_by_date_same_dates(operations, expected, reverse_order):
    operations_with_same_date = operations + [
        {"id": 5, "date": "2022-03-01T12:30:00.000000"}  # еще одна одинаковая дата
    ]
    sorted_list = sorted(operations, key=lambda x: (x["date"], x["id"]), reverse=reverse_order)
    sorted_operations = sort_by_date(operations_with_same_date, reverse_order)
    assert [op["id"] for op in sorted_operations[:3]] == expected

# Тесты на некорректные или нестандартные форматы дат
@pytest.mark.parametrize("invalid_date", [
    "2022-03-01",  # Неполный формат
    "01-03-2022T12:30:00.000000",  # Неправильный формат
    "not-a-date"  # Некорректная строка
])
def test_sort_by_date_invalid_format(operations, invalid_date):
    operations_with_invalid_date = operations + [
        {"id": 6, "date": invalid_date}
    ]
    with pytest.raises(ValueError):
        sort_by_date(operations_with_invalid_date)