def divide_numbers(a,b):
    try:
        result = a / b
        print(f"Результат деления: {result}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
    except TypeError:
        print("Ошибка: неверный тип данных")
    finally:
        print("Этот блок всегда выполняется, независимо от исключений")
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(10, "2")