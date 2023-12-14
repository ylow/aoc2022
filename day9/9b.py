import numpy as np

ROPE = [[0,0] for x in range(10)]
tlocs = set()

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    else:
        return 0

def update_pos(i):
    global tlocs, ROPE
    if abs(ROPE[i][1] - ROPE[i+1][1]) <= 1 and abs(ROPE[i][0] - ROPE[i+1][0]) <= 1:
        return
    ROPE[i+1][1] -= sign(ROPE[i+1][1] - ROPE[i][1])
    ROPE[i+1][0] -= sign(ROPE[i+1][0] - ROPE[i][0])
    if i+1 == len(ROPE) - 1:
        tlocs.add(tuple(ROPE[i+1]))

def update_rope():
    for i in range(len(ROPE)-1):
        update_pos(i)

tlocs.add(tuple(ROPE[9]))
for line in open('input','r'):
    ins, d = line.strip().split(' ')
    d = int(d)
    if ins == 'U':
        for i in range(d):
            ROPE[0][0] -= 1
            update_rope()
    if ins == 'D':
        for i in range(d):
            ROPE[0][0] += 1
            update_rope()
    if ins == 'L':
        for i in range(d):
            ROPE[0][1] -= 1
            update_rope()
    if ins == 'R':
        for i in range(d):
            ROPE[0][1] += 1
            update_rope()

print(len(tlocs))
