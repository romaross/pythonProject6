'''Написать программу для работы с матрицами:
1. Создание
2. Вывод
3. Сумма всех элементов
4. Нахождение максимального элемента
5. Нахождение минимального элемента.'''
import random


def createArray():
    r = 0
    n = int(input('Enter first index matrix: '))
    m = int(input('Enter second index matrix: '))
    a = int(input('matrix values from: '))
    b = int(input('matrix values to: '))
    array = []

    for i in range(n):
        array.append([])
        for j in range(m):
            array[i].append(random.randint(a, b))
            r += 1
    min = array[0][0]
    max = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] < min:
                min = array[i][j]
            elif array[i][j] > max:
                max = array[i][j]
    for i in range(n):
        print(array[i])
    print(max, min)
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += array[i][j]
    print(sum)


createArray()
