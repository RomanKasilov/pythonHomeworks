import json
from typing import TypedDict

"""1) Є файл emails.txt ваша задача записати в новий файл тільки email'ли з доменом gmail.com
    (Хеш то що з ліва записувати не потрібно)
"""

# try:
#     with open('emails.txt', 'r') as emails, open('results.txt', 'w') as results:
#         for line in emails:
#             if line.strip().endswith('gmail.com'):
#                 results.write(line.split()[-1] + '\n')
# except Exception as err:
#     print(err)


"""
2) Створити записну книжку покупок:
- у покупки повинна бути id, назва і ціна
- всі покупки зберігаємо в файлі
з функціоналу:
 * вивід всіх покупок
 * має бути змога додавати покупку в книгу
* має бути змога шукати по будь якому полю покупку
* має бути змога показати найдорожчу покупку
* має бути можливість видаляти покупку по id
(ну і меню на це все)
"""

Purchase = TypedDict('Purchase', {'id': int, 'name': str, 'price': int})


class PurchaseBook:
    def __init__(self):
        self.__file_name = input('enter file name') + '.json'
        self.__data: list[Purchase] = []
        self.__menu()

    def __read_file(self):
        try:
            with open(self.__file_name) as f:
                self.__data = json.load(f)
        except Exception as err:
            print(err)

    def __write_file(self):
        try:
            with open(self.__file_name, 'w') as f:
                json.dump(self.__data, f)
        except Exception as err:
            print(err)

    @staticmethod
    def input_to_int(msg: str) -> int:
        while True:
            str_from_input = input(msg)

            if not str_from_input.isdigit():
                print('Please enter price in digit characters')
                continue

            return int(str_from_input)

    def __show_all_purchases(self):
        self.__read_file()
        for item in self.__data:
            print(item)
        print('-' * 10)

    def __add(self):
        pk = self.__data[-1]['id'] + 1 if self.__data else 1
        name = input('enter  purchase name:')
        price = self.input_to_int('enter price')
        self.__data.append({'id': pk, 'name': name, 'price': price})
        self.__write_file()

    def __search(self):
        search = input('enter value:')
        for item in self.__data:
            for v in item.values():
                if v == search:
                    print(item)
                else:
                    print('not found')
                    return

    def __max_price(self):
        if self.__data:
            sorted_data = sorted(self.__data, key=lambda item: item['price'], reverse=True)
            print(sorted_data[0])
        else:
            print('list is empty')
            return

    def __del_by_id(self):
        self.__show_all_purchases()
        pk = self.input_to_int('delete id:')
        index = next((i for i, v in enumerate(self.__data) if v['id'] == pk), None)
        if index is not None:
            del self.__data[index]
            self.__write_file()
        else:
            print('Not found')
            return

    def __menu(self):
        while True:
            print('1) Get All')
            print('2) Add item')
            print('3) Search item')
            print('4) Most expensive')
            print('5) Delete by id')
            print('6) Exit')

            choice = input('enter your choice:')

            match choice:
                case '1':
                    self.__show_all_purchases()
                case '2':
                    self.__add()
                case '3':
                    self.__search()
                case '4':
                    self.__max_price()
                case '5':
                    self.__del_by_id()
                case '6':
                    break


# PurchaseBook()

"""
Є ось такий список:
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]

потрібно брати по черзі с кожного списку id і класти в список res, 
    якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку

з даним списком мае вийти ось такий результат:
res = [1110, 1120, 1130, 1111, 1122, .......]
"""
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]
res = []
gen_list = [(i['id'] for i in item if i['id'] not in res) for item in data]
while gen_list:
    gen = gen_list.pop(0)
    try:
        res.append(next(gen))
    except StopIteration:
        continue
    gen_list.append(gen)
# print(res)
