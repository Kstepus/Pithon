def get_matrix(n, m, value):
    matrix = []
    print(get_matrix)
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
matrix = get_matrix(2, 2, 10) #   - Матрица во плоти - бонусом
for i in matrix:
    print(*i)
matrix = get_matrix(3, 5, 42)
for i in matrix:
    print(*i)
matrix = get_matrix(4, 2, 13)
for i in matrix:
    print(*i)