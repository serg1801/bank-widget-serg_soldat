from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def main() -> None:
    account_card = "Maestro 1596837868705199"
    date_format = "2024-03-11T02:26:18.671407"

    masked_card = mask_account_card(account_card)
    new_date = get_date(date_format)

    print(masked_card)
    print()
    print(new_date)
    print()
    list_transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    list_transactions_changed_1 = filter_by_state(list_transactions)
    list_transactions_changed_2 = filter_by_state(list_transactions, "CANCELED")
    list_transactions_changed_sorted = sort_by_date(list_transactions)

    print(list_transactions_changed_1)
    print()
    print(list_transactions_changed_2)
    print()
    print(list_transactions_changed_sorted)


if __name__ == "__main__":
    main()
