N = 4
M = 5
A = [[0] * M for i in range(N)]
for i in range(len(A)):  # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
        print(A[i][j], end=' ')
    print()
