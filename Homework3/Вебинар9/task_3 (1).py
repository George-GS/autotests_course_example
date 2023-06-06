# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

f = open("test_file/task_3.txt", 'r', encoding='utf-8')
d = f.readlines()
n = "\n"
new = [[]]
for i in d:  # цикл генерирует массив new из списков, разделяя по "\n"
    if i == n:
        new.append([])
    else:
        new[-1].append(i)

j = 0
allsum = []
for j in range(len(new)):  # цикл составляет список из сумм каждого списка в массиве new
    i = 0
    sum = 0
    for i in range(len(new[j])):
        sum += int(new[j][i][:-1])
        i += 1
    allsum.append(sum)
    j += 1
allsum.sort()
three_most_expensive_purchases = allsum[-1] + allsum[-2] + allsum[-3]  # сортируем и складываем последние 3

assert three_most_expensive_purchases == 202346
