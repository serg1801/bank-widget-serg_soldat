import logging

from src.logging_config import setup_logging

masks_logger = setup_logging('masks')

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

    if len(account_number) < 4:
        masks_logger.info(f"Счёт отформатирован: {'**' + account_number}")
        return "**" + account_number
    else:
        masks_logger.info(f"Счёт отформатирован: {'**' + account_number[-4:]}")
        return "**" + account_number[-4:]
