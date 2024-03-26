m = [[1, 1, 1, 1, 1],
     [-1, -1, -1, -1, 1],
     [1, 1, 1, 1, 1],
     [1, -1, -1, -1, -1],
     [1, 1, 1, 1, 1]]


# Печать для отладки
def prir():
    for i in range(lm):
        for j in range(lm):
            print(f"{r[i, j]:3}", end=' ')
        print()


a, z = (0, 0), (4, 4)
# Словарь для накопления минимальных путей
r = {}
lm = len(m)
# Очень большое число
vbn = float('inf')
# Модифицируем входную матрицу, отрицательные числа превращаем в vbn
for i in range(lm):
    for j in range(lm):
        if m[i][j] < 0:
            m[i][j] = vbn
        r[i, j] = vbn
# Начальная точка
r[a] = m[a[0]][a[1]]

# Цикл по всем элементам матрицы пока еще есть изменения
tf = True
while tf:
    tf = False
    for i in range(lm):
        for j in range(lm):
            if m[i][j] != vbn:
                minij = min(r.get((i - 1, j), vbn), r.get((i + 1, j), vbn),
                            r.get((i, j - 1), vbn), r.get((i, j + 1), vbn))
                # Нашли соседа с более оптимальным путем
                if r[i, j] > m[i][j] + minij:
                    r[i, j] = m[i][j] + minij
                    tf = True
    prir()
    input()
# Строим путь от конца до начала, цепочкой минимальных соседов
path = [z]
x = z
while x != a:
    i, j = x[0], x[1]
    minij = min(r.get((i - 1, j), vbn), r.get((i + 1, j), vbn),
                r.get((i, j - 1), vbn), r.get((i, j + 1), vbn))
    for k in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), ]:
        if r.get(k, vbn) == minij:
            x = k
            path.append(x)
            break
# Выводим цепочку
print(path[::-1])


