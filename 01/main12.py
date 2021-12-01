file = open("input.txt")
sum_alt = 0
c = 0
a = [0,0,0]

for e in file:
    del a[0]
    a.append(e)
    sum = int(a[0]) + int(a[1]) + int(a[2])
    if sum > sum_alt:
        c += 1
    sum_alt = sum


print(c-3)