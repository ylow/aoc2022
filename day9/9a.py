H = [0,0]
T = [0,0]
tlocs = set()

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    else:
        return 0

def update_tail():
    global tlocs, T, H
    if abs(H[1] - T[1]) <= 1 and abs(H[0] - T[0]) <= 1:
    #    print(H, T)
        return
    T[1] -= sign(T[1] - H[1])
    T[0] -= sign(T[0] - H[0])
    #print(H, T)
    tlocs.add(tuple(T))

tlocs.add(tuple(T))
for line in open('input','r'):
    ins, d = line.strip().split(' ')
    d = int(d)
    if ins == 'U':
        for i in range(d):
            H[0] -= 1
            update_tail()
    if ins == 'D':
        for i in range(d):
            H[0] += 1
            update_tail()
    if ins == 'L':
        for i in range(d):
            H[1] -= 1
            update_tail()
    if ins == 'R':
        for i in range(d):
            H[1] += 1
            update_tail()

print(len(tlocs))
