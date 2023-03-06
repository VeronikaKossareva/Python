1.

# from time import sleep
#
# class TrafficLight:
#     __color = 'свет'
# #
# #
# #
#     def running(self):
#         delay = 7
#         print('Загорелся красный {}'.format(__class__.__color))
#         sleep(delay)
#
#         delay = 2
#         print('Загорелся желтый {}'.format(__class__.__color))
#         sleep(delay)
#
#         delay = 5
#         print('Загорелся зеленый {}'.format(__class__.__color))
#         sleep(delay)
#
# a = TrafficLight()
# a.running()

2.

# class Road:
#     def __init__(self, lenght, width):
#         self._lenght = lenght
#         self._width = width
#
#     def massa(self):
#         return int((self._lenght * self._width * 25 * 5)/1000)
#
# a = Road(20, 5000)
# print(a.massa())

3.
# wage = 3500
# bonus = 500
#
#
# class Worker:
#     def __init__(self):
#         self.name = 'Veronika'
#         self.surname = 'Kosareva'
#         self.position = 'Data scientist'
#         self._income = {"wage": wage, "bonus": bonus}
#
# class Position(Worker):
#     def get_full_name(self):
#         super().__init__()
#         print(self.name, self.surname)
#
#     def get_total_income(self):
#         super().__init__()
#         x = self._income.values()
#         print(sum(x))
#
# a = Position()
# a.get_full_name()
# a.get_total_income()


4.

# import random
#
# class Car:
#     def __init__(self):
#         self.speed = random.randint(30, 70)
#         self.color = 'Красный'
#         self.name = 'BMW'
#         self.is_police = random.choice([True, False])
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def turn(self):
#         print('Машина повернула')
#
#     def show_speed(self):
#         print('Скорость автомобиля {}'.format(self.speed))
#
# class TownCar(Car):
#
#     def show_speed(self):
#         super().__init__()
#         if self.speed > 60:
#             print('Превышена скорость')
#         else: print('Скорость автомобиля {}'.format(self.speed))
#
#
# class SportCar(Car):
#     pass
#
# class WorkCar(Car):
#     def show_speed(self):
#         super().__init__()
#         if self.speed > 40:
#             print('Превышена скорость')
#         else: print('Скорость автомобиля {}'.format(self.speed))
#
# class PoliceCar(Car):
#     pass
#
# a = Car()
# a.show_speed()
#
# b = WorkCar()
# b.show_speed()
#
# c = TownCar()
# c.show_speed()



# 5.
#
#
# class Stationery:
#     title = 'название'
#
#     def draw(self):
#         print('Запуск отрисовки')
#
# class Pen(Stationery):
#     def pen(self):
#         print('Рисуем ручкой')
#
# class Pencil(Stationery):
#     def pencil(self):
#         print('Рисуем карандашом')
#
# class Handle(Stationery):
#     def handle(self):
#         print('Рисуем маркером')
#
# a = Stationery()
# a.draw()
#
# b = Pen()
# b.pen()
#
# b = Pencil()
# b.pencil()
#
# b = Handle()
# b.handle()