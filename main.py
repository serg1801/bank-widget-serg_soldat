from src.bank_operations import process_bank_search
from src.file_readers import read_csv_file, read_excel_file
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def main():
    """
     Предоставляет пользовательский интерфейс, отвечает за основную логику проекта с пользователем,
    связывает функциональности между собой.
    """
    transactions_ = []
    operations_sort_state = []
    while True:
        print("\nПривет!\nДобро пожаловать в программу работы с банковскими транзакциями.\n")
        print(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла:"
        )
        users_choice = (input("\nВаш выбор: ")).strip()
        if users_choice == "1":
            print("Для обработки выбран JSON-файл.")
            file_path = "data/operations.json"
            transactions_ = read_json_file(file_path)
            break
        elif users_choice == "2":
            print("Для обработки выбран CSV-файл.")
            path_csv = "data/transactions.csv"
            transactions_ = read_csv_file(path_csv)
            break
        elif users_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            path_excel = "data/transactions_excel.xlsx"
            transactions_ = read_excel_file(path_excel)
            break
        else:
            print("\nНеверный выбор. Выберите 1,2 или 3")
            continue

    while True:
        print(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        status = ["EXECUTED", "CANCELED", "PENDING"]
        user_status = (input("\nВаш выбор: ")).strip().upper()
        if user_status in status:
            status_filter = user_status
            print(f"Был выбран статус: {status_filter}")
            operations_sort_state = filter_by_state(transactions_, status_filter)
            break
        else:
            print(f'Статус операции "{user_status}" недоступен')
            continue

    while True:
        sort_by_date_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sort_by_date_choice in ["да", "нет"]:
            if sort_by_date_choice == "да":
                while True:
                    order_choice = (
                        input(
                            "Отсортировать по возрастанию или по убыванию?"
                            '\nВведите "по возрастанию" или "по убыванию"\n'
                        )
                        .strip()
                        .lower()
                    )
                    if order_choice == "по возрастанию":
                        order_filter = False
                        operations_sort_data = sort_by_date(operations_sort_state, order_filter)
                        break
                    elif order_choice == "по убыванию":
                        order_filter = True
                        operations_sort_data = sort_by_date(operations_sort_state, order_filter)
                        break
                    else:
                        print(f'Ввод "{order_choice}" некорректен. Пожалуйста, попробуйте снова.')
            else:
                operations_sort_data = operations_sort_state
            break
        else:
            print(f'Ввод "{sort_by_date_choice}" некорректен. Наберите Да или Нет.')

    while True:
        currency_filter = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
        if currency_filter == "нет":
            transactions_lst = operations_sort_data
            break
        elif currency_filter == "да":
            currency_code_ = "RUB"
            # Определяем путь к ключу валюты в зависимости от формата файла
            if users_choice == "1":  # JSON
                currency_key_path = ["operationAmount", "currency", "code"]
                transactions_lst = list(filter_by_currency(operations_sort_data, currency_code_, currency_key_path))
                break
            elif users_choice == "2":  # CSV
                currency_key_path = ["currency_code"]  # Фактический ключ для CSV
                transactions_lst = list(filter_by_currency(operations_sort_data, currency_code_, currency_key_path))
                break
            elif users_choice == "3":  # XLSX
                currency_key_path = ["currency_code"]  # фактический ключ для XLSX
                transactions_lst = list(filter_by_currency(operations_sort_data, currency_code_, currency_key_path))
                break
        else:
            print(f'Ввод "{currency_filter}" некорректен. Наберите Да или Нет.')

    while True:
        word_filter = (
            input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
        )
        if word_filter == "да":
            search_word = input("Введите слово для фильтрации транзакций по описанию: ").strip()
            filtered_transactions = process_bank_search(transactions_lst, search_word)
            break
        elif word_filter == "нет":
            filtered_transactions = transactions_lst
            break
        else:
            print(f'Ввод "{word_filter}" некорректен. Наберите Да или Нет.')

    print("\nРаспечатываю итоговый список транзакций...")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}\n")

    for transaction in filtered_transactions:
        date = get_date(transaction["date"])
        description = transaction["description"]
        to_account = mask_account_card(transaction.get("to", ""))

        if transaction["description"] != "Открытие вклада":
            from_account = mask_account_card(transaction.get("from", ""))
            print(f"{date} {description}")
            print(f"{from_account} -> {to_account}")
        else:
            print(f"{date} {description}")
            print(to_account)

        if users_choice == "1":
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]
        else:
            amount = transaction["amount"]
            currency = transaction["currency_name"]

        print(f"Сумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
