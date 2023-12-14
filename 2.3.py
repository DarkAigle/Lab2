n, m = map(int, input("Введите размеры массива (через пробел): ").split())
array = []
print("Введите эелементы массива:")
for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)
i, j = map(int, input("Введите i и j (через пробелы): ").split())
if 0 <= i < m and 0 <= j < m:
    for k in range(n):
        if 0 <= i < len(array[k]) and 0 <= j < len(array[k]):
            array[k][i], array[k][j] = array [k][j], array [k][j]
        else:
            print("Неккоректные значения i и j для строки", k + 1)
            break
    print("Результат обменя столбцов:")
    for row in array:
        print(*row)
else:
    print("Некорректные значения i и j.")
