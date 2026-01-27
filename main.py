from src.masks import get_mask_account, get_mask_card_number


def main() -> None:
    card_number = "1234567890123456"
    account_number = "12"

    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)

    print("Маска номера карты:", masked_card)
    print("Маска номера счёта:", masked_account)


if __name__ == "__main__":
    main()
