# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
 # aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random

def generate_random_name():
    """
    Генератор, который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
    :return: результирующая строка - два слова из латинских букв от 1 до 15 символов, разделенных пробелами
    """
    a = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        yield ' '.join(''.join(random.choice(a) for _ in range(random.randint(1, 15))) for _ in range(2))


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
