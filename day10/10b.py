X = 1
cycle = 1
acc = 0

img = [[' '] * 40 for _ in range(6)]

def accres():
    global img
    row = (cycle-1) // 40
    col = (cycle-1) % 40
    if col in [X-1, X, X+1]:
        img[row][col] = '#'

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

for i in img:
    print(''.join(i))
