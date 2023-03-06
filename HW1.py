1.
name = 'Вероника'
vozrast = '27'
print ("Меня зовут", name, "мне", vozrast, "лет")
print ('--------')
mesto_prozivaniya = input('В каком городе ты родился?')
mesto_rozhdeniya = input('В каком городе ты проживаешь?')
print ('Я родился в', mesto_rozhdeniya)
print ('Проживаю в', mesto_prozivaniya)


2.
t = int(input('Insert time in secconds: '))
h = t//3600
m = t%3600//60
s = t%3600%60
if h < 10:
    h = '0'+ str(h)
if m < 10:
    m = '0'+ str(m)
if s < 10:
    s = '0'+ str(s)
print (h,':',m,':',s)


3.
n = input('Insert number: ')
print(int(n)+int(n+n)+int(n+n+n))


4.
a = input('Enter a positive integer: ')
b = 0
m = a[0]
while b < len(a)-1:
    if a[b] >= a[b+1]:
        m = a[b]
        b = b + 1
    else:
        m = a[b+1]
        b = b + 1
print(m)

5.
viruchka = input('Введите значение выручки: ')
izderzhki = input('Введите значение издержек: ')
if int(viruchka) > int(izderzhki):
    print('Прибыль')
    pribil = int(viruchka) - int(izderzhki)
    rentabelnost = (pribil / int(viruchka))
    print('Рентабельность фирмы', rentabelnost)
    ludi = input('Введите кол-во людей в компании: ')
    print('Прибыль фирмы в расчёте на одного сотрудника', pribil / int(ludi))

else:
    print('Убыток')


6.
a = 2
b = 3
x = 1
while a < b:
    x = x + 1
    a = 1.1 * a
print('На', x, 'день спортсмен достиг результата не менее', b, 'км')



