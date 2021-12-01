file = open("input.txt")
e_alt = 0
c = -1

for e in file:
    if int(e) > e_alt:
        c += 1
    e_alt = int(e)


print(c)