# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы класса:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

# Здесь пишем код
import math


class Segment:
    def __init__(self, kor1: tuple, kor2: tuple):
        self.kor1 = kor1
        self.kor2 = kor2

    def length(self):
        """ Возвращает длину нашего отрезка, с округлением до 2 знаков после запятой """

        rez1 = round(math.sqrt(((self.kor2[0] - self.kor1[0]) ** 2) + ((self.kor2[1] - self.kor1[1]) ** 2)), 2)
        print(rez1)
        return rez1

    def x_axis_intersection(self):
        """ Возвращает True, если отрезок пересекает ось X, иначе False """
        if self.kor1[1] > 0 and self.kor2[1] > 0:
            rez2 = False
        elif self.kor1[1] < 0 and self.kor2[1] < 0:
            rez2 = False
        else:
            rez2 = True
        print(rez2)
        return rez2

    def y_axis_intersection(self):
        """Возвращает True, если отрезок пересекает ось Y, иначе False"""
        if self.kor1[0] > 0 and self.kor2[0] > 0:
            rez3 = False
        elif self.kor1[0] < 0 and self.kor2[0] < 0:
            rez3 = False
        else:
            rez3 = True
        print(rez3)
        return rez3


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]

test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
