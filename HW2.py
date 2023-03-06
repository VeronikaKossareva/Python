1.
s = ['слово', 's', 3, [5, 7], 67.5, True, None]
for i in s:
    print(type(i))


2.
a = 0
s = []
b = int(input('How many elements will be in the list: '))
for i in range(b):
    b = input('Enter element of list: ')
    s.append(b)
print(len(s))
while a < len(s)-1:
    s.insert(a, s[a+1])
    s.pop(a+2)
    a = a + 2
print(s)


3.
a = input('Enter month number: ')
winter = ['1', '2', '12']
w_dict = dict.fromkeys(winter, "Winter")
spring = ['3', '4', '5']
sp_dict = dict.fromkeys(spring, "Spring")
summer = ['6', '7', '8']
su_dict = dict.fromkeys(summer, "Summer")
autumn = ['9', '10', '11']
a_dict = dict.fromkeys(autumn, "Autumn")
dictionary = w_dict | sp_dict | su_dict | a_dict
print(dictionary.get(a))


4.
stroka = input('Enter the string: ')
stroka = stroka.split()
a = 0
while a != len(stroka):
    if len(stroka[a]) > 10:
        stroka[a] = stroka[a][:10]
        a = a + 1
    else: a = a + 1
n = 1
for i in stroka:
    print(n, '.', ' ', stroka[n - 1], sep='')
    n += 1


5.
li2 = [7, 5, 3, 3, 2]
while True:
    b = input('Enter new number or enter "buy": ')
    if b == 'buy':
        break
    else:
        li1 = li2.copy()
        b = int(b)
        li1.append(b)
        li1.sort()
        li1 = li1[::-1]
        print(li1)

6.

name = ['computer', 'printer', 'scanner']
price = ['20000', '6000', '2000']
quantity = ['5', '2', '7']
unit = ['pcs']

a = 0
kor1 = name[a]+price[a]
print(kor1)
n = 1
for i in stroka:
    print(n, '.', ' ', stroka[n - 1], sep='')
    n += 1