import pytest
from datetime import datetime


@pytest.fixture(scope="class")
def class_fixture():
    """
    Фикстура для класса
    """
    print(f'Время начала выполнения класса с тестами: {datetime.now()}\n')
    yield None
    print(f'Время окончания выполнения класса с тестами: {datetime.now()}\n')


@pytest.fixture()
def test_fixture():
    """
    Фикстура для конкретного теста, используется не для всех тестов
    """
    print(f'Время выполнения теста {datetime.now()}\n')