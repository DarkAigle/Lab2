# Ввод размеров массива
n, m = map(int, input("Введите размеры массива (через пробел): ").split())

# Ввод элементов массива
array = []
for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

# Ввод чисел i и j
i, j = map(int, input("Введите i и j (через пробел): ").split())

# Проверка корректности введенных значений i и j
if 0 <= i < m and 0 <= j < m:
    # Обмен столбцов i и j
    for k in range(n):
        array[k][i], array[k][j] = array[k][j], array[k][i]

    # Вывод результата
    print("Результат обмена столбцов:")
    for row in array:
        print(*row)
else:
    print("Некорректные значения i и j.")