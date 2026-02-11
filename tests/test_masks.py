import pytest

from src.masks import get_mask_account, get_mask_card_number


# Фикстура для подготовки данных
@pytest.fixture
def card_numbers() -> list[tuple[str, str]]:
    return [
        ("1234567812345678", "1234 56** **** 5678"),  # корректный номер
        ("0000000000000000", "0000 00** **** 0000"),  # все нули
    ]


# Параметризация теста
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


# Тест на исключение
@pytest.mark.parametrize(
    "invalid_card_number", ["123", "1234abcd5678efgh", ""]  # короткий номер  # символы  # пустая строка
)
def test_get_mask_card_number_invalid(invalid_card_number: str) -> None:
    with pytest.raises(ValueError) as excinfo:
        get_mask_card_number(invalid_card_number)
    assert str(excinfo.value) in [
        "Номер карты должен содержать 16 цифр.",
        "Номер карты должен содержать только цифры.",
    ]


# Параметризация теста для get_mask_account
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("123456", "**3456"),  # корректный номер
        ("78", "**78"),  # короткий номер
        ("123456789", "**6789"),  # более длинный номер
        ("0000", "**0000"),  # все нули
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected


# Тест для проверки обработки некорректных данных
@pytest.mark.parametrize(
    "invalid_account_number",
    [
        123,  # числовой формат
        "",  # пустая строка
    ],
)
def test_get_mask_account_invalid(invalid_account_number: int | str) -> None:
    result = get_mask_account(invalid_account_number)
    # Проверь, что функция корректно возвращает маску даже для некорректных данных
    assert result.startswith("**")
