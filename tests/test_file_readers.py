from typing import Any
from unittest.mock import Mock, patch

import pandas as pd
import pytest

from src.file_readers import read_csv_file, read_excel_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv: Mock) -> None:
    test_data: dict[str, Any] = {
        "id": [650703.0],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": [16210.0],
        "currency_name": ["Sol"],
        "currency_code": ["PEN"],
        "from": ["Счет 58803664561298323391"],
        "to": ["Счет 39745660563456619397"],
        "description": ["Перевод организации"],
    }

    # Создаем DataFrame из test_data
    mock_read_csv.return_value = pd.DataFrame(test_data)

    # Ожидаемый результат
    expected_result = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

    # Вызываем функцию и проверяем результат
    result = read_csv_file("fake_path.csv")
    assert result == expected_result


@patch("pandas.read_csv")
def test_read_csv_file_parser_error(mock_read_csv: Mock) -> None:
    # Настраиваем mock, чтобы вызывать ошибку парсинга
    mock_read_csv.side_effect = pd.errors.ParserError("Ошибка парсинга")

    # Проверяем, что вызывается ошибка ValueError
    with pytest.raises(ValueError) as excinfo:
        read_csv_file("fake_path.csv")

    assert "Ошибка при чтении файла CSV" in str(excinfo.value)


@patch("src.file_readers.pd.read_excel")
def test_read_excel_file(mock_read_excel: Mock) -> None:
    # Создаем пример данных, которые будет возвращать мок
    mock_df = pd.DataFrame(
        {
            "id": [650703.0],
            "state": ["EXECUTED"],
            "date": ["2023-09-05T11:30:32Z"],
            "amount": [16210.0],
            "currency_name": ["Sol"],
            "currency_code": ["PEN"],
            "from": ["Счет 58803664561298323391"],
            "to": ["Счет 39745660563456619397"],
            "description": ["Перевод организации"],
        }
    )
    mock_read_excel.return_value = mock_df

    # Вызываем функцию и проверяем результат
    expected_result = mock_df.to_dict(orient="records")
    result = read_excel_file("fake_path.xlsx")

    assert result == expected_result


@patch("src.file_readers.pd.read_excel")
def test_read_excel_file_raises_value_error(mock_read_excel: Mock) -> None:
    mock_read_excel.side_effect = ValueError("Ошибка при чтении файла Excel")
    with pytest.raises(ValueError, match="Ошибка при чтении файла Excel"):
        read_excel_file("non_existent_file.xlsx")
