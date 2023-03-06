1.

# class Matrix:
#     def __init__(self):
#         self.a = [[31, 32], [37, 43], [51, 86]]
#         self.b = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
#         self.c = [[3, 5, 38, 3], [8, 3, 7, 1]]
#         self.d = [[1, 1], [1, 1], [1, 1]]
#
#     def __str__(self):
#         print(f'{self.a[0][0]} {self.a[0][1]}')
#         print(f'{self.a[1][0]} {self.a[1][1]}')
#         print(f'{self.a[2][0]} {self.a[2][1]}')
#         print()
#
#         print(f'{self.b[0][0]} {self.b[0][1]} {self.b[0][2]}')
#         print(f'{self.b[1][0]} {self.b[1][1]} {self.b[1][2]}')
#         print(f'{self.b[2][0]} {self.b[2][1]} {self.b[2][2]}')
#         print()
#
#         print(f'{self.c[0][0]} | {self.c[0][1]} | {self.c[0][2]} | {self.c[0][3]}')
#         print('--------------')
#         print(f'{self.c[1][0]} | {self.c[1][1]} | {self.c[1][2]}  | {self.c[1][3]}')
#         print()
#
#
#     def __add__(self):
#         e = [[self.a[i][j] + self.d[i][j] for j in range (len(self.a[0]))] for i in range(len(self.a))]
#         print(f'{e[0][0]} {e[0][1]}')
#         print(f'{e[1][0]} {e[1][1]}')
#         print(f'{e[2][0]} {e[2][1]}')
#
#
# q = Matrix()
# q.__str__()
# q.__add__()


2.


# class Clothes:
#     def __init__(self, size, hight):
#         self.size = size
#         self.hight = hight
#
#     @property
#     def size(self):
#         return self.__size
#
#     @size.setter
#     def size(self, size):
#         if size < 44:
#             self.__size = 44
#         elif size > 58:
#             self.__size = 58
#         else:
#             self.__size = size
#
#     @property
#     def hight(self):
#         return self.__hight
#
#     @hight.setter
#     def hight(self, hight):
#         if hight < 150:
#             self.__hight = 150
#         elif hight > 200:
#             self.__hight = 200
#         else:
#             self.__hight = hight
#
# class Coat(Clothes):
#
#     def coat(self):
#         return self.size * 6.5 + 0.5
#
#
# class Suite(Clothes):
#     def suite(self):
#         return 2 * self.hight + 0.3
#
#
# b = Coat(1, 1)
# print(b.coat())
#
# c = Suite(1, 1)
# print(c.suite())
#
# print(b.coat() + c.suite())


3.

# class Cell():
#     def __init__(self, num):
#         self.num = num
#
#
#     def __add__(self, other):
#         return Cell(self.num + other.num)
#
#     def __sub__(self, other):
#         return Cell(self.num - other.num)
#
#     def __mul__(self, other):
#         return Cell(self.num * other.num)
#
#     def __truediv__(self, other):
#         return Cell(self.num // other.num)
#
#     def make_order(self, stolb):
#         if self.num % stolb == 0:
#             res5 = self.num // stolb * (stolb * '*'+'/n')
#             print(res5[:len(res5)-2])
#         else:
#             print(self.num // stolb * (stolb * '*'+'/n') + self.num % stolb * '*')
#
# a = Cell(12)
# b = Cell(3)
# res1 = a + b
# res2 = a - b
# res3 = a * b
# res4 = a / b
#
#
#
# print(res1.num)
# print(res2.num)
# print(res3.num)
# print(res4.num)
#
# a.make_order(5)

