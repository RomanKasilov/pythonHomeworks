"""
написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
- перший записує в список нову справу
- другий повертає всі записи
- протипізувати
"""

from typing import Callable


def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[None | str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        l1 = [*todo_list]
        return l1

    return add_todo, get_all


add_todos, get_all_todos = notebook()
add_todos('do something')
# print(get_all_todos())

"""
створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

Приклад:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
"""


def expanded_form(num: int) -> str:
    st = str(num)
    st_length = len(st) - 1
    res = [item + '0' * (st_length - i) for i, item in enumerate(st) if item != '0']
    return '+'.join(res)


# print(expanded_form(20323))


"""
створити декоратор котрий буде підраховувати скільки разів була запущена функція
продекорована цим декоратором,
та буде виводити це значення після виконання функцій
"""


def decor(function):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'count={count}')
        function(*args, **kwargs)
        print('*' * 10)

    return inner


@decor
def f1():
    print('func1')


@decor
def f2():
    print('func2')


# f1()
# f1()
# f1()
# f2()
# f1()
