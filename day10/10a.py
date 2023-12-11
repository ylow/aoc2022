X = 1
cycle = 1
acc = 0

def accres():
    global acc
    if cycle % 40 == 20:
        print(cycle, X)
        acc += X * cycle

for line in open("input"):
    l = line.strip()
    ins = l[:4]
    rest = l[4:]
    if ins == "noop":
        accres()
        cycle += 1
    elif ins == "addx":
        d = int(rest)
        accres()
        cycle += 1
        accres()
        cycle += 1
        X += d
accres()

print(acc)
