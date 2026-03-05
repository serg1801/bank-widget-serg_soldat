import pytest

import requests

from unittest.mock import patch, Mock

from src.external_api import converting_amount_rubles


# Успешная конвертация валюты с ожидаемым результатом
@patch('src.external_api.requests.get')
def test_converting_amount_rubles_success(mock_get) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {'result': 74.5}
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '1',
            'currency': {
                'code': 'USD'
            }
        }
    }

    # Вызов тестируемой функции
    result = converting_amount_rubles(transaction)

    # Проверка результата
    assert result == 74.5


# Тест на ошибку HTTP
@patch('src.external_api.requests.get')
def test_converting_amount_rubles_status(mock_get):
    # Определение данных транзакции
    transaction = {
        'operationAmount': {
            'currency': {'code': 'USD'},
            'amount': '100'
        }
    }

    # Имитация ошибки HTTP
    mock_response = mock_get.return_value
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Mocked HTTP error")

    # Проверка, что функция возвращает None
    result = converting_amount_rubles(transaction)
    assert result is None

    # Убедиться, что raise_for_status был вызван
    mock_get.return_value.raise_for_status.assert_called_once()


# Тест на неправильный формат ответа
@patch('src.external_api.requests.get')
def test_key_error_handling(mock_get) -> None:
    # Имитация ответа API с отсутствующим ключом 'result'
    mock_get.return_value.json.return_value = {}
    mock_get.return_value.status_code = 200

    # Данные транзакции без нужного ключа
    transaction = {
        'operationAmount': {
            'currency': {'code': 'USD'},
            'amount': '100'
        }
    }

    try:
        converting_amount_rubles(transaction)
    except KeyError:
        print('KeyError caught as expected')
        assert result is None


@patch('src.external_api.requests.get')
def test_transaction_in_rubles(self) -> None:
    transaction = {
        'operationAmount': {
                'amount': "31957.58",
                'currency': {
                    'code': "RUB"
                }
            }
        }
    result = converting_amount_rubles(transaction)
    assert result == 31957.58, f"Expected 31957.58, but got {result}"


@patch('src.external_api.requests.get')
def test_request_exception(mock_get):
    # Настраиваем mock для выбрасывания исключения
    mock_get.side_effect = requests.exceptions.RequestException("Test exception")

    result = converting_amount_rubles({
        'operationAmount': {
            'currency': {'code': 'USD'},
            'amount': '100'
        }
    })

    # Проверяем, что функция возвращает None в случае исключения
    assert result is None
