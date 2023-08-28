import random

def print_list(msg, matrix):
    print(msg)
    for i in range(len(matrix)):
        print(*matrix[i], sep="  ")

def addition_matrix():
    matrix_C = [[0 for i in range(m)] for i in range(n)]
    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[i])):
            matrix_C[i][j] = matrix_A[i][j] + matrix_B[i][j]
    print_list("Результат сложения A + B:", matrix_C)

n, m = map(int, input("Введите размеры матриц  M x N через пробел: ").split())
a, b = map(int, input("Введите промежуток случайных чисел через пробел: ").split())
if a > b:
    a, b = b, a
matrix_A = [[random.randint(a, b) for i in range(m)] for i in range(n)]
matrix_B = [[random.randint(a, b) for i in range(m)] for i in range(n)]

print_list("Матрица A:", matrix_A)
print_list("Матрица B:", matrix_B)
addition_matrix()