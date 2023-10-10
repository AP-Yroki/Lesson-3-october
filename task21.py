n = 8
x= []
y = []
for i in range(n):
    n_x, n_y = [int(s) for s in input().split()]
    x.append(n_x)
    y.append(n_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')