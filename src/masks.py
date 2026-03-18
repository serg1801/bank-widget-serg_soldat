import re

from src.logging_config import setup_logging

masks_logger = setup_logging("masks")


def get_mask_card_number(card_number: int | str) -> str:
    """
    Принимает на вход номер карты в виде числа
     и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    card_str = str(card_number)

    if len(card_str) != 16:
        masks_logger.error("Номер карты должен содержать 16 цифр.")
        raise ValueError("Номер карты должен содержать 16 цифр.")

    if not card_str.isdigit():
        masks_logger.error("Номер карты должен содержать только цифры.")
        raise ValueError("Номер карты должен содержать только цифры.")

    formatted_number_card = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return formatted_number_card


def get_mask_account(account_number: int | str) -> str:
    """
    Принимает на вход номер счета и возвращает маску номера по правилу **XXXX
    """

    if not isinstance(account_number, str):
        account_number = str(account_number)

    # Извлекаем только цифры из строки
    numbers = re.findall(r"\d+", account_number)
    if numbers:
        # Берем последние 4 цифры
        last_four = numbers[-1][-4:]
        return f"**{last_four}"
    return "**неизвестно"
