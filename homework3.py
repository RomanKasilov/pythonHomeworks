"""
Створити клас Rectangle:
-він має приймати дві сторони x,y
-описати поведінку на арифметични методи:
  + сумма площин двох екземплярів ксласу
  - різниця площин двох екземплярів ксласу
  == площин на рівність
  != площин на не рівність
  >, < меньше більше
  при виклику метода len() підраховувати сумму сторін
"""

from typing import Self
import timeit


class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __square(self):
        return self.x * self.y

    def __add__(self, other: Self) -> int:
        return self.__square() + other.__square()

    def __sub__(self, other: Self) -> int:
        return self.__square() - other.__square()

    def __eq__(self, other: Self) -> bool:
        return self.__square() == other.__square()

    def __ne__(self, other: Self) -> bool:
        return self.__square() != other.__square()

    def __lt__(self, other: Self) -> bool:
        return self.__square() < other.__square()

    def __gt__(self, other: Self) -> bool:
        return self.__square() > other.__square()

    def __len__(self) -> int:
        return (self.x + self.y) * 2


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 6)

# print(len(r1))
"""
створити класс Human (name, age)
створити два класси Prince и Cinderella які наслідуються від Human:
у попелюшки мае бути ім'я, вік, розмір нонги
у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, 
та шукати ту саму

в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
також має бути метод классу який буде виводити це значення
"""


class Human:
    # __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name: str, age: int, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    __slots__ = 'foot_size',

    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        print(Cinderella.__count)

    def get_self(self):
        return self.name


class Prince(Human):
    def __init__(self, name: str, age: int, shoe_size: int):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    __slots__ = 'shoe_size',

    def find_cinderella(self, cinderellas: list[Cinderella]):
        print([cinderella for cinderella in cinderellas if self.shoe_size == cinderella.foot_size])


cinderellas_list = [Cinderella('masha', 19, 36),
                    Cinderella('manya', 30, 45),
                    Cinderella('valya', 30, 36)]
c1 = Cinderella('valya', 30, 36)

prinz = Prince('fedya', 19, 36)
prinz.find_cinderella(cinderellas_list)
Cinderella.get_count()
my_setup = """
class Human:


    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name: str, age: int, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1



    def __repr__(self):
        return str(self.__dict__)

    @classmethod
    def get_count(cls):
        print(Cinderella.__count)

    def get_self(self):
        return self.name
        
c1 = Cinderella('valya', 30, 36)
"""

# it = timeit.timeit("Cinderella('valya', 30, 36)", setup=my_setup, number=10000000)
# print(it)
