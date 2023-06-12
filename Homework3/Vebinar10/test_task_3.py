# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните
import pytest


import pytest

def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('args', [
                                pytest.param((5, 0), marks=pytest.mark.smoke),
                                pytest.param((6, 2), marks=pytest.mark.skip),
                                (5, 2),
                                (-8, -2),
                                (1, 0.5),
                                ])
def test1(args):
    all_division(args)
