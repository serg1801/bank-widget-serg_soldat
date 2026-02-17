def get_mask_card_number(card_number: int | str) -> str:
    """
    Принимает на вход номер карты в виде числа
     и возвращает маску номера по правилу XXXX XX** **** XXXX
    """
    card_str = str(card_number)

    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр.")

    if not card_str.isdigit():
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
        return "**" + account_number
    else:
        return "**" + account_number[-4:]
