i_max = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i_max]:
        i_max = i

print(a[i_max], [i_max])