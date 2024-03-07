t = [[1, 1, 1, 1],
     [9, 6, 8, 555],
     [9, 2, 70, 1],
     [1, 1, 1, 1]]

lent = len(t)
vbn = float('inf')

r = {(0, 0): t[0][0]}


def pri():
    for i in range(lent):
        for j in range(lent):
            print(r.get((i, j), vbn), end=' ')
        print()
    input('---')


for i in range(lent):
    for j in range(lent):
        if (i, j) not in r:
            r[i, j] = t[i][j] + min(r.get((i - 1, j), vbn), r.get((i, (j - 1)), vbn))
        elif r[i, j] > t[i][j] + min(r.get((i - 1, j), vbn), r.get((i, (j - 1)), vbn)):
            r[i, j] = t[i][j] + min(r.get((i - 1, j), vbn), r.get((i, (j - 1)), vbn))
        pri()

x = y = lent - 1
way = [(x, y)]
while x > 0 or y > 0:
    if r.get((x - 1, y), vbn) < r.get((x, y - 1), vbn):
        x -= 1
    else:
        y -= 1
    way.append((x, y))
    print(way)
    input("===")
print(way[::-1])
