from src.widget import mask_account_card, get_date


def main() -> None:
    account_card = str("Visa Platinum 8990922113665229")
    date_format = str("2024-03-11T02:26:18.671407")

    masked_card = mask_account_card(account_card)
    new_date = get_date(date_format)

    print(masked_card)
    print(new_date)


if __name__ == "__main__":
    main()
