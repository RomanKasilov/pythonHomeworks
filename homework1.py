# =======strings============
"""
1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
наприклад:
st = 'as 23 fdfdg544' введена строка
2,3,5,4,4        #вивело в консолі.
"""
# st = 'as 23 fdfdg544'
# numList = [i for i in st if i.isdigit()]
# print(','.join(numList))
# print(','.join(i for i in st if i.isdigit()))
"""
2)написати прогу яка вибирає зі введеної строки числа і виводить їх 
так як вони написані
наприклад:
  st = 'as 23 fdfdg544 34' #введена строка
  23, 544, 34              #вивело в консолі
"""
# st = 'as 23 fdfdg544 34'
# print(','.join(''.join(i if i.isdigit() else ' ' for i in st).split()))


# ========== list comprehension ===========
"""
1)є строка:
greeting = 'Hello, world'
записати кожний символ як окремий елемент списку і зробити його заглавним:
['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
"""
# greeting = 'Hello, world'
# print([i.title() for i in greeting])
# print([i.upper() for i in greeting])

"""
2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
приклад:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
"""

# print([i ** 2 for i in range(50) if i % 2 == 1])


# ============ function =================
# - створити функцію яка виводить ліст
'''
def show_list(some_list):
    print(some_list)
'''

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
"""
def max_num(a, b, c):
    res = max(a, b, c)
    print(res)
    return res
"""

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
'''
def num_func(*args):
    min_num = min(*args)
    max_num = max(*args)
    print(max_num)
    return min_num
'''


# - створити функцію яка повертає найбільше число з ліста

def max_num_in_list(some_num_list):
    return max(some_num_list)


# - створити функцію яка повертає найменьше число з ліста
"""
def min_num_in_list(some_num_list):
    return min(some_num_list)
"""

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
"""
def sum_of_nums(arr):
    return sum(arr)
"""

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
"""
def avr_of_nums(arr):
    return sum(arr) / len(arr)
"""

# =======================================

"""
1)Дан list:
  list = [22, 3,5,2,8,2,-23, 8,23,5]
  - знайти мін число
  - видалити усі дублікати
  - замінити кожне 4-те значення на 'X'
2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
3) вывести табличку множення за допомогою цикла while
4) переробити це завдання під меню
"""
list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def min_num():
    print(min(list1))


def delete_duplicate():
    l1 = list1.copy()
    print(list(set(l1)))


def change_to_x():
    l1 = list1.copy()
    print(['X' if (i + 1) % 4 == 0 else num for i, num in enumerate(l1)])


def print_square(num=4):
    for i in range(num):
        if i == 0 or i == num - 1:
            print('*' * num)
        else:
            print('*' + ' ' * (num - 2) + '*')


def pifagor_table():
    size = 9
    a = 1
    while a <= size:
        b = 1
        while b <= size:
            res = a * b
            print(' ' if res // 10 else '  ', end='')
            print(res, end='')
            # print(f'{res:3}', end='')
            b += 1
        print()
        a += 1


while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на "X"')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла while')
    print('6) exit')

    choice = input('enter your choice:')

    if choice == '1':
        min_num()
    elif choice == '2':
        delete_duplicate()
    elif choice == '3':
        change_to_x()
    elif choice == '4':
        print_square()
    elif choice == '5':
        pifagor_table()
    elif choice == '6':
        break
