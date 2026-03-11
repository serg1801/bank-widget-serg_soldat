import json

from src.logging_config import setup_logging

utils_logger = setup_logging("utils")


def read_json_file(file_path: str) -> list:
    """
     Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            transactions_list = json.load(file)
            if isinstance(transactions_list, list):
                utils_logger.info(f"Файл {file_path} успешно прочитан.")
                return transactions_list
            else:
                utils_logger.warning(f"Содержимое файла {file_path} не является списком.")
    except FileNotFoundError:
        utils_logger.error(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        utils_logger.error(f"Ошибка декодирования JSON в файле {file_path}.")
    return []


# transactions_ = read_json_file('data/operations.json')
# print(transactions_)
