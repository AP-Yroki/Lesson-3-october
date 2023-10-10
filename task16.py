a = [int(i) for i in input().split()]
x = int(input())
loc = 0
while loc < len(a) and a[loc] >= x:
    loc += 1
print(loc + 1)