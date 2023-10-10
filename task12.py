
res = 0
x = 1
y = 1

while x or y != 0:
    x = int(input())
    if x == 0:
        break
    y = int(input())
    if y ==0:
        break
    if x == y:
        res += 1

print(res)

