a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Обмен
a, b = b, a
print(f"До обмена: a = {a}, b = {b} ")
print("Первое число: ", a)
print("Второе число: ", b)