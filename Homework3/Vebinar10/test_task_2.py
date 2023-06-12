# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    """"
    Функция деления, возвращающая результат деления
    """
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


def test_zero():
    """
    Тест деления на ноль
    """
    with pytest.raises(ZeroDivisionError):
        all_division(3, 0)


@pytest.mark.smoke
def test2():
    """
    Тест с делением без остатка
    """
    assert all_division(8, 2) == 4


@pytest.mark.smoke
def test3():
    """
    Тест с делением с остатком
    """
    assert all_division(10, 4) == 2.5


def test4():
    """
    Тест с делением двух отрицательных чисел
    """
    assert all_division(-12, -2) == 6


def test5():
    """
    Тест с делением дробных чисел
    """
    assert all_division(5, 0.5) == 10
