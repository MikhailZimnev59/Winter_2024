x = float(input('Введите число: '))
y = float(input('Введите число №2: '))

# Проверка, что y не равно 0 для операций деления
if y == 0:
print('Проверим, что y не равно 0')
else:
sum = x + y
diff = x - y
prod = x * y
div = x / y
int_div = x // y


max1 = max2 = float('-inf')

# Сравниваем сумму
if sum > max1:
max2 = max1
max1 = sum
elif sum > max2:
max2 = sum

# Сравниваем разность
if diff > max1:
max2 = max1
max1 = diff
elif diff > max2:
max2 = diff

# Сравниваем произведение
if prod > max1:
max2 = max1
max1 = prod
elif prod > max2:
max2 = prod

# Сравниваем деление
if div > max1:
max2 = max1
max1 = div
elif div > max2:
max2 = div

# Сравниваем целочисленное деление
if int_div > max1:
max2 = max1
max1 = int_div
elif int_div > max2:
max2 = int_div

print(sum, diff, prod, div, int_div, max2)
print(f'Второе максимальное значение: {max2}')