porog = int(input())
n = int(input())
n1 = 0
erc = 0
porc = 0
maxx = 0
sr = 0
for i in range(n):
    c = input()
    if c == 'error':
        erc += 1
    else:
        if float(c) > porog:
            porc += 1
        if float(c) > maxx:
            maxx = float(c)
        sr += float(c)
        n1 += 1
print("Количество записей:",n)
print("Количество ошибок:",erc)
print("Знгачений выше порога",porc)
print(f'Максимальное значение: {maxx:.1f}')
print(f'Среднее значение: {sr/n1:.1f}')