1.

# my_file = open('NewText.txt', 'w')
# a = 'hj'
# while len(a) >= 1:
#     a = input('vvedite stroku v fayl: ')
#     my_file.write(a)
#     for line in a:
#         my_file.write(line + '\n')
# my_file.close()


2.

count = 0
with open(r"C:\Users\moroz\Desktop\Ника\github-projects\HW_python\Simonov.txt", "r", encoding="utf-8") as file:
    for line in file:
        count += 1
        print("Кол-во слов в строке: ", len(line.split()))
        print(line)
    print("Кол-во строк: ", count)

3.

# count = 0
# b = []
# with open(r"C:\Users\moroz\Desktop\3.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         count += 1
#         a = line.split()
#         [b.append(int(a[1]))]
#         if int(a[1]) > 20000:
#             print(a[0])
#     print(sum(b)/count)


4.

# x = {'One':'Один', 'Two':"Два", 'Three':"Три", 'Four':"Четыре"}
# with open(r"C:\Users\moroz\Desktop\5.4.txt", "r", encoding="utf-8") as file:
#     for line in file:
#
#         for i in x.keys():
#             line = line.replace(i, str(x[i]))
#
#         my_file = open('5.4_new.txt', 'a+')
#         my_file.write(line)
#         my_file.close()


5.
# a = input('Введите набор чисел, разделённых пробелами: ')
# my_file = open('5.5.txt', 'w+')
# my_file.write(a)
# my_file.close()
#
# my_file = open('5.5.txt', 'r')
# for line in my_file:
#     a = line.split()
#     a = [int(i) for i in a]
#     print(sum(a))


6.

# import re
# predmet = []
# vremya = []
# with open(r"C:\Users\moroz\Desktop\5.6.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         a = line.split()
#         [predmet.append(a[0][:-1])]
#         nums = re.findall(r'\d+', line)
#         nums = [int(i) for i in nums]
#         [vremya.append(sum(nums))]
# a = dict(zip(predmet, vremya))
# print(a)


7.
# x = []
# firma = []
# pribil = []
# average_profit = []
# with open(r"C:\Users\moroz\Desktop\5.7.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line)
#         a = line.split()
#         [firma.append(a[0])]
#         [pribil.append(int(a[2])-int(a[3]))]
# [average_profit.append(i) for i in pribil if i > 0]
# ch = sum(average_profit)/len(average_profit)
# d = {'average_profit': ch}
# b = dict(zip(firma, pribil))
# x.append(b)
# x.append(d)
# print(x)
#
# import json
# with open("my_file.json", "w") as write_f:
#     json.dump(x, write_f)
# json_str = json.dumps(x)
# print(json_str)








