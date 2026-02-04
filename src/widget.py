import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета,
     и возвращает строку с замаскированным номером.
    """

    if "счет" in account_card.lower():
        letters_count = "".join(re.findall(r"\D+", account_card))
        numbers_count = "".join(re.findall(r"\d+", account_card))
        return f"{letters_count.capitalize()} {get_mask_account(numbers_count)}"
    else:
        letters_card = "".join(re.findall(r"\D+", account_card))
        numbers_card = "".join(re.findall(r"\d+", account_card))
        return f"{letters_card} {get_mask_card_number(numbers_card)}"


def get_date(date_format: str) -> str:
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
     и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
    """

    date_split_list = date_format.split("T")
    formated_date = re.sub(
        r"(\d{4})-(\d{2})-(\d{2})", r"\3.\2.\1", (date_split_list[0])
    )

    return formated_date
