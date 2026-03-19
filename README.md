# Проект "Мои банковские операции"

## Описание:

Проект "Мои банковские операции" - это виджет на Python, 
который показывает несколько последних успешных банковских операций клиента.
---

## Установка:

+ Установите на свой компьютер GitHub.
+ Клонируйте репозиторий с GitHub  с помощью веб-URL.
```
 git clone https://github.com/serg1801/bank-widget-serg_soldat.git
```
---

## Использование:

В текущем виде, программа запускается в модуле main.py:

---

## Примеры использования функций:

**Модуль masks**
содержит функции для наложения масок на конфиденциальные данные:

+ get_mask_card_number(card_number: str) -> str**

Принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX

     Пример: 7000792289606361 → 7000 79** **** 6361

+ get_mask_account(account_number: int | str) -> str

Принимает на вход номер счета и возвращает маску номера по правилу **XXXX

     Пример: 73654108430135874305 → **4305

**Модуль widget**
содержит функции для работы с банковскими данными:

+ mask_account_card(account_card: str) -> str

Принимает  строку, содержащую тип и номер карты или счета, и возвращает строку с замаскированным номером.

     Пример: "Visa Platinum 8990922113665229" → "Visa Platinum  8990 92** **** 5229"

+ get_date(date_format: str) -> str

Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").

      Пример: "2024-03-11T02:26:18.671407" → "11.03.2024"

**Модуль processing**
содержит  функции для фильтрации и сортировки банковских операций:

+ filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]

Фильтрует список операций по статусу выполнения (например по 'EXECUTED')

      Пример: [
               {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
              ]  
         →   →   [
                  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                 ]
    

+ sort_by_date(list_dictionary: list[Dict[str, Any]], reverse_order: bool = True) -> List[Dict[str, Any]]

Сортирует список операций по дате (например по убыванию)

      Пример: [
               {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
              ]
        →   →   [
                 {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                ]

**Модуль generators**
содержит функции, реализующие генераторы для обработки данных.

+filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:

Создает генератор, который поочередно выдает транзакции, по заданной валюте (например по "RUB"

      Пример: transactions_ = 
     [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ] 
    →   → filter_by_currency(transactions_, "RUB") →   → 
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }

+ transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[Dict[str, Any]]:

Генератор, который возвращает описание каждой операции по очереди
        
    Пример: transactions = transactions_
            descriptions = transaction_descriptions(transactions_)
            for _ in range(5):
                print(next(descriptions))

         →   →  Перевод организации
                Перевод со счета на счет
                Перевод со счета на счет
                Перевод с карты на карту
                Перевод организации 

+ card_number_generator(start: int, stop: int) -> Iterator[str]:

Генератор, создает номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
      
    Пример:  for card_number in card_number_generator(1, 5):
                 print(card_number)

          →   →  0000 0000 0000 0001
                 0000 0000 0000 0002
                 0000 0000 0000 0003
                 0000 0000 0000 0004
                 0000 0000 0000 0005

**Модуль decorators**
используется  для размещения декораторов
+ log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:

декоратор, который будет автоматически логировать начало и конец выполнения функции,
а также ее результаты или возникшие ошибки

При оборачивание функции при заданном аргументе filename="mylog.txt", в файл mylog.txt,
записывается сообщение: "имя функции ok"

Без заданного аргумента, тоже сообщение выводится в консоль

     Пример:  @log(filename="mylog.txt")
              def divide_function(x, y):
              return x / y
              divide_function(4, 1)   →   →  divide_function ok

**Модуль file_readers**
в модуле реализованны функции для  считывание финансовых операций из CSV- и XLSX-файлов
+ read_csv_file(path_csv: str) -> list[dict]:
Функция для считывания финансовых операций из CSV. Принимает путь к файлу CSV, в качестве аргумента, 
и выдает список словарей с транзакциями.

+ read_excel_file(path_excel: str) -> list[dict]:
Функция для считывания финансовых операций из Excel. Принимает путь к файлу Excel, в качестве аргумента,
и выдает список словарей с транзакциями.

**Модуль bank_operations**
в модуле реализован поиск с помощью регулярных выражений и подсчет количества банковских операций определенного типа
+ process_bank_search
Функция для считывания финансовых операций из CSV. Принимает путь к файлу CSV, в качестве аргумента, 
и выдает список словарей с транзакциями.

+ process_bank_operations
Функция принимает список словарей с данными о банковских операциях и список категорий операций, и возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории

**Модуль main.py**
Содержит фукционал запуска  программы

+ Функция main предоставляет пользовательский интерфейс, отвечает за основную логику проекта с пользователем,
связывает функциональности между собой

---

## Разработка:

+ Проект находится в активной разработке. План работы в дальнейшем:

+ Добавление новых модулей для расширения функционала

+ Улучшение обработки различных форматов данных

+ Добавление тестов
---

## Тестирование:

*Тесты созданы в пакете **tests**. Модуля в пакете  tests содержат тесты для каждой функции.
Назвние модуля теста соответствует модулю функционального кода с префиксом test.
То есть, в модуле **test_masks.py** содержаться тесты для функций модуля **masks.py** и так далее.
Для тестирования был установлен фреймворк тестирования *pytest* и добавлена библиотека *pytest-cov*.
Запуск тестов: команда `pytest --cov` в терминале.
Code coverage — это метрика, которая показывает, какой процент кода программы был протестирован.
Чтобы запустить тесты с оценкой покрытия, можно воспользоваться командой: `pytest --cov=src --cov-report=html`.
Отчет будет сгенерирован в папке htmlcov и храниться в файле с названием index.html*

**Модуль test_masks.py**  содержит тесты для обрабоки функций get_mask_card_number, get_mask_account.

*Использован декаратор @pytest.mark.parametrize, который позволяет определить набор параметров
для теста и их возможные значений*

пример:

```
@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("123456", "**3456"),  # корректный номер
        ("78", "**78"),  # короткий номер
        ("123456789", "**6789"),  # более длинный номер
        ("0000", "**0000"),  # все нули
        ("12ab34", "**ab34"),  # номер с символами
    ],
)
```
+ test_get_mask_card_number(card_number: str, expected: str) -> None:**

  *В тесте проверяются разные варианты входных данных с ожидаемым результатом,
  что позволяет убедиться в корректной работе функции:*

      Пример: "1234567812345678" → → "1234 56** **** 5678"
              "0000000000000000" → → "0000 00** **** 0000"

+ test_get_mask_card_number_invalid(invalid_card_number: str) -> None:

  *Тест проверяет корректность обработки некорректных входных данных
  Ожидается, что при таких вводах функция выбросит исключение ValueError с соответствующими сообщениями об ошибках,
   подтверждающими, что номер карты должен содержать 16 цифр и только цифры.*

      Пример: 1234abcd5678efgh → → "Номер карты должен содержать только цифры."
                           123 → → "Номер карты должен содержать 16 цифр."

+ test_get_mask_account(account_number: str, expected: str) -> None:

  *Проверяются разные варианты входных данных с ожидаемым результатом,
  что позволяет убедиться в корректной работе функции:*

      Пример: "123456789" → → "**6789"
                 "12ab34" → → "**ab34"
                   "0000" → → "**0000"

+ test_get_mask_account_invalid(invalid_account_number: int | str) -> None:*

  *Тест для проверки обработки некорректных данных*

      Пример:  123 → → 123
                "" → → ""

**Модуль test_widget.py** содержит тесты для обрабоки функций  mask_account_card, get_date.

*Использован декаратор @pytest.mark.parametrize, который позволяет определить набор параметров
для теста и их возможные значений*

*пример параметризации  для test_mask_account_card :*

```
@pytest.mark.parametrize("input_data, expected_output", [
    ("Visa Platinum 8990922113665229", "Visa Platinum  8990 92** **** 5229"),
    ("Maestro 1596837868705199", "Maestro  1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard  7158 30** **** 6758"),
    ("Visa Gold 5999414228426353", "Visa Gold  5999 41** **** 6353"),
    ("Счет 64686473678894779589", "Счет  **9589")
])
```
+ test_mask_account_card(input_data: str, expected_output: str) -> None:

  *В тесте проверяются разные варианты входных данных с ожидаемым результатом,
  что позволяет убедиться в корректной работе функции*

      Пример: "Visa Platinum 8990922113665229" → → "Visa Platinum  8990 92** **** 5229"
                   "Счет 64686473678894779589" → → "Счет  **9589"

+ test_mask_account_card_invalid_data() -> None:

  *Тест на проверку исключения при вызове функции с некорректными аргументами
  Если в процессе исполнения возникает исключение нужного типа — тест проходит*

+ test_get_date_various_formats(input_date: str, expected: str) -> None:

  *Тест для get_date. Если входные данные "Некорректная строка без даты"
  то  в этом случае будет выброшено исключение ValueError.*

**Модуль test_processing.py** содержит тесты для обрабоки функций filter_by_state, sort_by_date.

*Применён  декоратор @pytest.mark.parametrize и фикстуры для предоставления тестовых данных @pytest.fixture*

*пример:*
```
# Фикстура для предоставления тестовых данных
@pytest.fixture
def transactions() -> List[Dict[str, Union[int, str]]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

# Параметризированные вводые
@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]),
    ("CANCELED", [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]),
    ("PENDING", []),  # Проверка при отсутствии словарей с указанным статусом
])
```

+ test_filter_by_state(transactions: List[Dict[str, any]], state: str, expected: List[Dict[str, any]]) -> None

    *В тесте проверяются разные варианты входных данных с ожидаемым результатом сортировки нового списка
    по соответствующему ключу, что позволяет убедиться в корректной работы функции*

+ test_sort_by_date_order(operations: List[Dict[str, Union[int, str]]], reverse_order: bool, expected_ids: List[int]) -> None:

    *Тестируем работу функции  sort_by_date в случае одинаковых значениях дат.* 

+ test_sort_by_date_same_dates(operations: List[Dict[str, Union[int, str]]], expected: List[int], reverse_order: bool) -> None:

    *Тестируем работу функции sort_by_date, при добавление еще одной транзакции с датой  транзакции, которая есть в списке*

+ test_sort_by_date_invalid_format

    *Тест на некорректные или нестандартные форматы дат*

**Модуль test_generators.py** содержит тесты для обрабоки функций 
filter_by_currency, transaction_descriptions, card_number_generator

*Применён  декоратор @pytest.mark.parametrize.*

*Для функций  test_filter_by_currency и  test_transaction_descriptions в модуле* conftest.py *создана фикстура @pytest.fixture
def transactions_()*

+ test_filter_by_currency(transactions_: List[Dict[str, Any]], currency_code: str, expected_count: int) -> None

    *Тест на работу генератора с разными значениями валют и пустым списком транзакций.*

+ test_transaction_descriptions(transactions_: List[Dict[str, Any]], expected_descriptions: List[str]) -> None:

    *Тест на обработку  работы генератора с выдачей описания транзакций*

+ test_card_number_generator(start: int, stop: int, expected: List[str]) -> None

    *Тест на обработку генерации номеров карт в заданном диапазоне*

**Модуль test_decorators.py** содержит тесты для обработки дакораторов в модуле decorators

Применён  декоратор @pytest.mark.parametrize

+ test_log_to_console
 
    *Тест для обработки работы декоратора для вывода сообщения в консоль*

+ test_log_to_file

    *Тест для обработки работы декоратора для записи сообщения в файл*

**Модуль test_file_readers.py**
содержит функционал для тестирования функций в модуле file_readers.py

применен декоратор patch и Mock-объекты

+ test_read_csv_file
    *Тест для обработки правильной работы фукции read_csv_file. То есть чтоб она находила путь к файлу csv
и возращала список словарей с транзакциями*

+ test_read_csv_file_parser_error
    *Тест на обработку ошибки парсинга*

+ test_read_excel_file
    *Тест на правильную работу функции read_excel_file. То есть чтоб она находила путь к файлу XLSX
и возращала список словарей с транзакциями*

+ test_read_excel_file_raises_value_error
    *Тест на обработку ошибки ValueError

**Модуль test_bank_operations.py**
содержит тесты для тестирования функций в модуле bank_operations.py 

применен @pytest.mark.parametrize и фикстура data_ c модуля conftest.py

+ test_process_bank_search
     *Тест на работу функции process_bank_search с различными типами входных данных*

+  test_process_bank_operations
     *Тест на обработку работы функции process_bank_operations с различными входными данными и параметрами сортировки*

+ test_empty_transactions_list 
     *Тест обработки функции process_bank_operations, в случае если входные данные это пустой список

---

## Автор проекта:

Soldatov Sergei
