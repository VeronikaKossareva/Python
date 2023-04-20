# 1.
#
#
# import re
# class Data():
#     data = '02-03-2023'
#
#     @classmethod
#     def chislo(cls):
#         nums = re.findall(r'\d+', cls.data)
#         nums = [int(i) for i in nums]
#         print(type(nums[0]), type(nums[1]), type(nums[2]))
#         print('Day:', nums[0])
#         print('Month:', nums[1])
#         print('Year:', nums[2])
#
#
#     @staticmethod
#     def validate(data):
#         nums = re.findall(r'\d+', data)
#         nums = [int(i) for i in nums]
#         if 1 <= nums[0] <= 31:
#             print('Day:',nums[0])
#         else:
#             print('Wrong day')
#
#         if 1 <= nums[1] <= 12:
#             print('Month:', nums[1])
#         else:
#             print('Wrong month')
#
#         if 2000 <= nums[2] <= 2023:
#             print('Year:', nums[2])
#         else:
#             print('Wrong year')
#
# a = Data()
# a.chislo()
# a.validate('32-03-2023')


2.


# class DelenieNaNol:
#     x = int(input('Введите числитель: '))
#     y = int(input('Введите знаменатель: '))
#
#     @classmethod
#     def delenie(cls):
#         try:
#             z = cls.x / cls.y
#             print(z)
#         except ZeroDivisionError:
#             print('На ноль делить нельзя')
#
# a = DelenieNaNol
# a.delenie()

3.

# class Chisla:
#
#     def proverka(self):
#         a = []
#         while True:
#
#             stroka = input("Введите число или stop для выхода: ")
#             if stroka == 'stop':
#                 print(a)
#                 break
#             else:
#                 try:
#                     float(stroka)
#                     a.append(stroka)
#
#                 except ValueError:
#                     print('Введите только числа')
#
# a = Chisla()
# a.proverka()


4, 5, 6.


# import random
# class Sklad:
#     def __init__(self):
#
#         self.dict = {}
#
#
#
#     def add(self):
#         n1 = ["Принтер", "Сканер", "Ксерокс"]
#         n2 = ['HP', 'Canon', 'Brother']
#         self.name = random.choice(n1) + ' ' + random.choice(n2)
#         self.articl = random.randint(10000, 99999)
#         self.dict[self.name] = self.articl
#         print('На складе', len(self.dict), 'единиц(а) техники:')
#         print(self.dict)
#
#
# class Orgtehnika:
#     def __init__(self):
#
#         self.dict = {}
#         n1 = ["Принтер", "Сканер", "Ксерокс"]
#         n2 = ['HP', 'Canon', 'Brother']
#         count = 0
#         while count < 10:
#             self.name = random.choice(n1) + ' ' + random.choice(n2)
#             self.articl = random.randint(10000, 99999)
#             self.dict[self.articl] = self.name
#             count += 1
#
#
#
#     def deport(self):
#         self.store_1 = {}
#         self.store_2 = {}
#         self.store_3 = {}
#
#         for i in self.dict:
#             if i <= 40000:
#                 self.store_1[i] = self.dict[i]
#                 print(i, 'перемещен в Store_1')
#
#             elif 40000 < i <= 70000:
#                 self.store_2[i] = self.dict[i]
#                 print(i, 'перемещен в Store_2')
#             else:
#                 self.store_3[i] = self.dict[i]
#                 print(i, 'перемещен в Store_3')
#
#
#         for i in self.store_1:
#             if self.store_1[i] in self.dict[i]:
#                 self.dict.pop(i)
#
#         for i in self.store_2:
#             if self.store_2[i] in self.dict[i]:
#                 self.dict.pop(i)
#
#         for i in self.store_3:
#             if self.store_3[i] in self.dict[i]:
#                 self.dict.pop(i)
#
#
#
#
#         print('В Store_1', len(self.store_1), 'ед. техники:')
#         print(self.store_1)
#         print('В Store_2', len(self.store_2), 'ед. техники:')
#         print(self.store_2)
#         print('В Store_3', len(self.store_3), 'ед. техники:')
#         print(self.store_3)
#
#
#
#
#
# class Printer(Orgtehnika):
#
#     def printer(self):
#
#         b = []
#         count = 0
#         for i in self.dict.values():
#             a = i.split()
#             if a[0] == 'Принтер':
#                 count += 1
#                 b.append(a[0] + ' ' + a[1])
#
#         print('Всего', count, 'принтеров:', b)
#
#
# class Scaner(Orgtehnika):
#     def scaner(self):
#
#         b = []
#         count = 0
#         for i in self.dict.values():
#             a = i.split()
#             if a[0] == 'Сканер':
#                 count += 1
#                 b.append(a[0] + ' ' + a[1])
#
#         print('Всего', count, 'сканеров:', b)
#
#
#
#
#
# class Xerox(Orgtehnika):
#     def xerox(self):
#
#         b = []
#         count = 0
#         for i in self.dict.values():
#             a = i.split()
#             if a[0] == 'Ксерокс':
#                 count += 1
#                 b.append(a[0] + ' ' + a[1])
#
#         print('Всего', count, 'ксероксов:', b)
#
#
#
# a = Sklad()
# a.add()
# a.add()
# a.add()
#
#
# b = Orgtehnika()
# b.deport()
#
# c = Printer()
# c.printer()
#
# d = Scaner()
# d.scaner()
#
# e = Xerox()
# e.xerox()


7.

# class Komplelsnoe_chislo():
#     def __init__(self, argument):
#         self.argument = argument
#
#     def __add__(self, other):
#         return other + self.argument
#
#     def __mul__(self, other):
#         return other * self.argument
# a = Komplelsnoe_chislo(2+3j)
# b = Komplelsnoe_chislo(-1+1j)
#
# print(a + b)
# print(a * b)





