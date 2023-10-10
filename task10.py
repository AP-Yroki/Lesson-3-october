f_max = int(input())
s_max = int(input())

if f_max < s_max:
    f_max, s_max = s_max, f_max
i = int(input())

while i != 0:
    if i > f_max:
        s_max, f_max = f_max, i
    elif i > s_max:
        s_max = i
    i = int(input())

print(s_max)