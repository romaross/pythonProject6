from random import randint as rnd  # Случайное целое
import math  # Модуль математических констант и функций
from functools import reduce


def init_matrix(_n, _m):
    """ Создать матрицу  """
    n = _n  # Число строк матрицы
    m = _m  # Число столбцов матрицы
    res_m = []  # Инициализация пустой матрицы
    for i in range(n):  # Итерация по строкам
        r = []  # Пустой ряд матрицы
        for j in range(m):  # Итерация по столбцам
            r.append(rnd(1, 9))  # Добавить случайный элемент матрицы
        res_m.append(r)  # Добавить ряд матрицы
    return res_m  # Вернуть результат


class Matrix:
    """ Класс матрицы """

    def __init__(self, _rows, _cols):  # Конструктор
        self.mat = init_matrix(_rows, _cols)  # Создать двумерный массив
        self.rows = _rows  # Число строк
        self.cols = _cols  # Число столбцов

    def __eq__(self, other):
        if type(other) is Matrix:
            if self.rows == other.rows and self.cols == other.cols:
                for ir in range(self.rows):
                    for jc in range(self.cols):
                        if self.mat[ir][jc] == other.mat[ir][jc]:
                            continue
                        else:
                            return False
            else:
                return False
        else:
            return False

    def __str__(self):
        s1 = '\n'
        for r in self.mat:
            s1 += str(r)
            s1 += '\n'
        return s1

    def get_rows(self):
        """ Количество строк """
        return self.rows  # Вернуть число строк

    def get_cols(self):
        """ Количество столбцов """
        return self.cols  # Вернуть число столбцов

    def set_elem(self, r, c, x):
        """ Установить элемент """
        if r < self.rows and c < self.cols:  # Если индексы не выходят за диапазон
            self.mat[r][c] = x  # Присвоить значение элементу матрицы

    def get_elem(self, r, c):
        """ Получить элемент  """
        if r < self.rows and c < self.cols:  # Если индексы не выходят за диапазон
            return self.mat[r][c]  # Вернуть значение элемента матрицы

    def max_elem(self):
        """ Максимальный элемент матрицы  """
        max1 = -math.inf  # Присвоить минус бесконечность
        for r in self.mat:  # Для каждой строки матрицы
            if max(r) > max1:  # Если текущий максимум больше локального
                max1 = max(r)  # Установить новый максимум
        return max1  # Вернуть найденный максимум

    def min_elem(self):
        """ Минимальный элемент матрицы  """
        min1 = math.inf  # Присвоить плюс бесконечность
        for r in self.mat:  # Для каждой строки матрицы
            if min(r) < min1:  # Если текущий минимум меньше локального
                min1 = min(r)  # Установить новый минимум
        return min1  # Вернуть найденный минимум

    def all_sum(self):
        """ Сумма элементов матрицы  """
        sum1 = 0  # Инициализировать нулём
        for r in self.mat:  # Для каждой строки матрицы
            sum1 += sum(r)  # Прибавить сумму строки к общей сумме
        return sum1  # Вернуть сумму

    def max_sum_row_index(self):
        """ Индекс максимального ряда матрицы  """
        max1, index1 = -math.inf, -1  # Инициализировать минус бесконечность и -1
        for i, r in enumerate(self.mat):  # Индекс и для каждой строки матрицы
            sum1 = reduce(lambda x, y: x + y, r)  # Сумма ряда
            if sum1 > max1:  # Если текущий максимум больше локального
                max1 = sum1  # Установить новый максимум
                index1 = i  # Запомнить индекс
        return index1  # Вернуть индекс

    def max_sum_col_index(self):
        """ Индекс максимальной колонки матрицы"""
        max1, index1 = -math.inf, -1  # Инициализировать минус бесконечность и -1
        for j in range(self.cols):  # Цикл по столбцам (индекс)
            sum1 = 0  # Инициализировать сумма 0
            for i in range(self.rows):  # Цикл по строкам (индекс)
                sum1 += self.mat[i][j]  # Прибавить значение к общей сумме
            if sum1 > max1:  # Если максимум столбца больше локального
                max1 = sum1  # Установить новый максимум
                index1 = j  # Запомнить индекс
        return index1  # Вернуть индекс

    def min_sum_row_index(self):
        """ Индекс минимального ряда матрицы  """
        min1, index1 = math.inf, -1  # Инициализировать плюс бесконечность и -1
        for i, r in enumerate(self.mat):  # Индекс и для каждой строки матрицы
            sum1 = reduce(lambda x, y: x + y, r)  # # Сумма ряда
            if sum1 < min1:  # Если текущий минимум меньше локального
                min1 = sum1  # Установить новый минимум
                index1 = i  # Запомнить индекс
        return index1  # Вернуть индекс

    def min_sum_col_index(self):
        """ Индекс минимальной колонки матрицы"""
        min1, index1 = math.inf, -1  # Инициализировать плюс бесконечность и -1
        for j in range(self.cols):  # Цикл по столбцам (индекс)
            sum1 = 0  # Инициализировать сумма 0
            for i in range(self.rows):  # Цикл по строкам (индекс)
                sum1 += self.mat[i][j]  # Прибавить значение к общей сумме
            if sum1 < min1:  # Если минимум столбца меньше локального
                min1 = sum1  # Установить новый минимум
                index1 = j  # Запомнить индекс
        return index1  # Вернуть индекс

    def zero_upper_diagonal(self):
        """ Обнулить все элементы выше главной диагонали """
        for i in range(0, self.rows):  # Цикл со счётчиком по строкам
            for j in range(i + 1, self.cols):  # Цикл со счётчиком по столбцам от счётчика по строкам +1
                self.mat[i][j] = 0  # Занулить элемент

    def zero_lower_diagonal(self):
        """ Обнулить все элементы ниже главной диагонали. """
        for i in range(0, self.rows):  # Цикл со счётчиком по строкам
            for j in range(i + 1, self.cols):  # Цикл со счётчиком по столбцам от счётчика по строкам +1
                if j < self.get_rows() and i < self.get_cols():  # Условие индексов для вхождения в размерность
                    self.mat[j][i] = 0  # Перевёрнутый индекс, занулить элемент


def add_mat(_a, _b):
    """  Сумма матриц """
    if (type(_a) is Matrix) and (type(_b) is Matrix):  # Если входный параметры типа класса  Matrix
        if _a.get_rows() == _b.get_rows() and _a.get_cols() == _b.get_cols():  # Размерности матриц совпадают
            n, m = _a.get_rows(), _a.get_cols()  # Число строк и столбцов
            mat1 = Matrix(n, m)  # Создать новую матрицу
            for i in range(n):  # Цикл со счётчиком по строкам
                for j in range(m):  # Цикл со счётчиком по столбцам
                    mat1.set_elem(i, j, _a.get_elem(i, j) + _b.get_elem(i, j))  # Установить новый элемент суммы
            return mat1  # Вернуть матрицу
        else:  # Иначе
            return None  # Пустой результат
    else:  # Иначе
        return None  # Пустой результат


def sub_mat(_a, _b):
    """  Разность матриц """
    if (type(_a) is Matrix) and (type(_b) is Matrix):  # Если входные параметры типа класса  Matrix
        if _a.get_rows() == _b.get_rows() and _a.get_cols() == _b.get_cols():  # Размерности матриц совпадают
            n, m = _a.get_rows(), _a.get_cols()  # Число строк и столбцов
            mat1 = Matrix(n, m)  # Создать новую матрицу
            for i in range(n):  # Цикл со счётчиком по строкам
                for j in range(m):  # Цикл со счётчиком по столбцам
                    mat1.set_elem(i, j, _a.get_elem(i, j) - _b.get_elem(i, j))  # Установить новый элемент разности
            return mat1  # Вернуть матрицу
        else:  # Иначе
            return None  # Пустой результат
    else:  # Иначе
        return None  # Пустой результат


def mul_mat_scalar(_a, _scalar):
    """  Умножение матрицы на скаляр """
    if type(_a) is Matrix:  # Если входной параметр типа класса  Matrix
        n, m = _a.get_rows(), _a.get_cols()  # Число строк и столбцов
        mat1 = Matrix(n, m)  # Создать новую матрицу
        for i in range(n):  # Цикл со счётчиком по строкам
            for j in range(m):  # Цикл со счётчиком по столбцам
                mat1.set_elem(i, j, _a.get_elem(i, j) * _scalar)  # Установить новый элемент умножения
        return mat1  # Вернуть матрицу
    else:  # Иначе
        return None  # Пустой результат


def mul_mat(left_mat_a, right_mat_b):
    """  Умножение матрицы на матрицу """
    if (type(left_mat_a) is Matrix) and (type(right_mat_b) is Matrix):  # Если входные параметры типа класса  Matrix
        # Проверка на согласованность матриц
        if left_mat_a.get_rows() == right_mat_b.get_cols() and right_mat_b.get_rows() <= left_mat_a.get_cols():
            rows, cols = left_mat_a.get_cols(), right_mat_b.get_rows(),  # Число строк и столбцов
            mat1 = Matrix(rows, cols)  # Создать новую матрицу
            for i in range(rows):  # Цикл со счётчиком по строкам
                for j in range(cols):  # Цикл со счётчиком по столбцам
                    mat1.set_elem(i, j, 0)  # Установить новый элемент равный нулю
                    for k in range(right_mat_b.get_rows()):  # Цикл со счётчиком для умножения матриц
                        c = mat1.get_elem(i, j)  # Получить элемент на позиции i, j
                        c += left_mat_a.get_elem(i, k) * right_mat_b.get_elem(k, j)  # Вычислять сумму произведений
                        mat1.set_elem(i, j, c)  # Установить элемент на позиции i, j
            return mat1  # Вернуть матрицу
        else:  # Иначе
            return None  # Пустой результат
    else:  # Иначе
        return None  # Пустой результат


def main_func():
    """ Test function """
    rows_in_matrix = 4  # Константное количество строк в матрицах
    cols_in_matrix = 4  # Константное количество столбцов в матрицах
    m1 = Matrix(rows_in_matrix, cols_in_matrix)  # Создать объект матрицы
    try:  # Обработчик исключения
        print(m1)  # Вывод матрицы
        print('Max element ', m1.max_elem())  # Вызов - вывод максисальный элемент
        print('Min element ', m1.min_elem())  # Вызов - вывод минимальный элемент
        print('All summa ', m1.all_sum())  # Вызов - вывод сумма элементов
        print('Index of row with max summa ', m1.max_sum_row_index())  # Вызов - вывод индекс ряда макс. сумма
        print('Index of col with max summa ', m1.max_sum_col_index())  # Вызов - вывод индекс столбец макс. сумма
        print('Index of row with min summa ', m1.min_sum_row_index())  # Вызов - вывод индекс ряда мин. сумма
        print('Index of col with min summa ', m1.min_sum_col_index())  # Вызов - вывод индекс столбец мин. сумма
        m1.zero_upper_diagonal()  # Вызов метода обнуления верхней диагонали
        print('Zero upper diagonal ', m1)  # Вывод матрицы
        m1.zero_lower_diagonal()  # Вызов метода обнуления нижней диагонали
        print('Zero lower diagonal ', m1)  # Вывод матрицы
        matrix_a = Matrix(rows_in_matrix, cols_in_matrix)  # Создать матрицу
        matrix_b = Matrix(rows_in_matrix, cols_in_matrix)  # Создать матрицу
        matrix_c = add_mat(matrix_a, matrix_b)  # Сложить матрицы
        matrix_d = sub_mat(matrix_a, matrix_b)  # Вычесть матрицы
        g = input('Enter scalar number: ')  # Ввести число
        matrix_e = None  # Инициализация пустым значением
        matrix_f = Matrix(cols_in_matrix, rows_in_matrix)  # Создать матрицу
        matrix_h = Matrix(rows_in_matrix, cols_in_matrix)  # Создать матрицу
        matrix_g = mul_mat(matrix_f, matrix_h)  # Умножение матриц
        if g.isdigit():  # Проверка что число целое
            matrix_e = mul_mat_scalar(matrix_a, int(g.strip()))  # Умножение матрицы на скаляр
        print('Matrix A:', matrix_a)  # Вывод матрицы
        print('Matrix B:', matrix_b)  # Вывод матрицы
        if matrix_c is not None:  # Если матрица создана, то
            print('A + B:', matrix_c)  # Вывести значение матрицы суммы
        if matrix_d is not None:  # Если матрица создана, то
            print('A - B:', matrix_d)  # Вывести значение матрицы разности
        if matrix_e is not None:  # Если матрица создана, то
            print('A * g:', matrix_e)  # Вывести значение матрицы умноженной на скаляр
        print('Matrix F:', matrix_f)  # Вывод матрицы
        print('Matrix H:', matrix_h)  # Вывод матрицы
        if matrix_g is not None:  # Если матрица создана, то
            print('H * G', matrix_g)  # # Вывести значение матричного умножения

        matrix_i = Matrix(cols_in_matrix, rows_in_matrix)  # Создать матрицу ( транспонированную )
        matrix_i.zero_upper_diagonal()  # Вызов обнулить верхнию диагональ
        matrix_i.zero_lower_diagonal()  # Вызов обнулить нижнию диагональ
        for i in range(matrix_i.get_rows()):  # Цикл со счётчиком по строкам матрицы
            matrix_i.set_elem(i, i, int(g.strip()))  # Устанавливать число на главной диагонали
        print('Matrix I:', matrix_i)  #
        matrix_j = mul_mat(right_mat_b=matrix_a, left_mat_a=matrix_i)  # Вызов матричного умножения арг. по имени
        print('A * I:', matrix_j)  # Вывод матрицы
        assert matrix_e == matrix_j  # Диагностика на равенство матриц вычисленных по разному скаляр на главной
        #   диагонали или через матричное умножение
    except Exception as inst:  # Обработчик исключения
        print(inst)  # Вывод сообщения исключения


if __name__ == '__main__':
    main_func()
