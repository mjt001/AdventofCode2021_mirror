h = 0
d = 0

file = open("input.txt")

for e in file:
    com, val = e.split(" ")
    if com == "forward":
        h += int(val)
    elif com == "up":
        d -= int(val)
    elif com == "down":
        d += int(val)

print(h)
print(d)
print(h*d)

