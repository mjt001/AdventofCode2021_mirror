h = 0
d = 0
a = 0

file = open("input.txt")

for e in file:
    com, val = e.split(" ")
    if com == "forward":
        h += int(val)
        d += int(val)*a
    elif com == "up":
        a -= int(val)
    elif com == "down":
        a += int(val)

print(h)
print(d)
print(h*d)

