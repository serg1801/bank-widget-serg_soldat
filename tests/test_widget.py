import pytest
from typing import List, Tuple
from src.widget import mask_account_card, get_date

# Фикстура для подготовки данных
@pytest.fixture
def account_cards() -> List[Tuple[str, str]]:
    return [
        ("Visa Platinum 8990922113665229", "Visa Platinum  8990 92** **** 5229"),
        ("Maestro 1596837868705199", "Maestro  1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard  7158 30** **** 6758"),
        ("Visa Gold 5999414228426353", "Visa Gold  5999 41** **** 6353"),
        ("Счет 64686473678894779589", "Счет  **9589")
    ]

# Параметризация теста для mask_account_card
@pytest.mark.parametrize("input_data, expected_output", [
    ("Visa Platinum 8990922113665229", "Visa Platinum  8990 92** **** 5229"),
    ("Maestro 1596837868705199", "Maestro  1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard  7158 30** **** 6758"),
    ("Visa Gold 5999414228426353", "Visa Gold  5999 41** **** 6353"),
    ("Счет 64686473678894779589", "Счет  **9589")
])

def test_mask_account_card(input_data: str, expected_output: str) -> None:
    assert mask_account_card(input_data) == expected_output

def test_mask_account_card_invalid_data() -> None:
    with pytest.raises(ValueError):
        mask_account_card("Некорректные данные")

# Фикстура для подготовки данных с корректными и некорректными датами
@pytest.fixture
def date_formats() -> List[Tuple[str, str]]:
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("Некорректная строка без даты", None)
    ]

# Параметризация теста для get_date
@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2020-01-01T00:00:00.000000", "01.01.2020"),
    ("1999-12-31T23:59:59.999999", "31.12.1999"),
    ("Некорректная строка без даты", None)
])
def test_get_date_various_formats(input_date: str, expected: str) -> None:
    if expected is None:
        with pytest.raises(ValueError):
            get_date(input_date)
    else:
        assert get_date(input_date) == expected
