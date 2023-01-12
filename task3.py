# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

list = list(map(int, input("Введите последовательность чисел (через пробел): \n").split()))
print(f"Полученная последовательность: {list}")

list_count = []
for i in list:
    count = 0
    for k in list:
        if k == i:
            count += 1
    list_count.append(count)
res = []
for i in range(len(list_count)):
    if list_count[i] == 1:
        res.append(list[i])
print(res)