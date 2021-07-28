size = 4
matr = [[1] * size for i in range(size)]
print(matr)
for i in range(0, size):
    for j in range(i, size):
        matr[i][j] = 0
print(matr)