# 1.

# from sys import argv
# name, n_1, n_2, n_3 = argv
# print(int(n_1) * int(n_2) + int(n_3))


# 2.

# a = [300, 600, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 100, 200]
# b = [a[i] for i in range(1, len(a)) if a[i] > a[i-1]]
# print(b)

# 3.

# print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

# 4.

# a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# # [23, 1, 3, 10, 4, 11]
# b = []
# c = []
# [b.append(i) for i in a if a.count(i) > 1]
# [c.append(i) for i in a if i not in b]
# print(c)


# a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# # [23, 1, 3, 10, 4, 11]
# print([i for i in a if a.count(i) == 1])


# 5.
# from functools import reduce
# a = []
# [a.append(i) for i in range(100, 1001) if i % 2 == 0]
# print(reduce(lambda x, y: x*y, a))


# from functools import reduce
# print(reduce(lambda x, y: x*y, [i for i in range(100, 1001) if i % 2 == 0]))

# 6.
# import itertools
# for i in itertools.count(3):
#   print(i)
#   if i >= 10:
#       break


# a = [300, 600, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 100, 200]
# count = 0
# for i in itertools.cycle(a):
#     print(i)
#     count += i
#     if count > 5000:
#         break

# 7.


def fact(n):
    acc = 1
    ch = 1
    while ch <= n:
        acc = acc * ch
        yield acc
        ch += 1


n = 5
for el in fact(n):
    print(el)
