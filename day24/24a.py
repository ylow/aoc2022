m = [list(f.strip()) for f in open("input", "r")]

height = len(m)
width = len(m[0])
start = (0, 1)
end = (height - 1, width - 2)
print(end)
m[start[0]][start[1]] = ''
m[end[0]][end[1]] = ''

def iloop(i):
    if i == 0:
        i = height - 2
    if i == height - 1:
        i = 1
    return i


def jloop(j):
    if j == 0:
        j = width - 2
    if j == width - 1:
        j = 1
    return j

def next_map(m):
    ret = [[''] * width for i in range(height)]
    for i in range(height):
        for j in range(width):
            if i == 0 or j == 0 or i == height-1 or j == width-1:
                ret[i][j] = m[i][j]
                continue
            if '>' in m[i][jloop(j-1)]:
                ret[i][j] += '>'
            if '<' in m[i][jloop(j+1)]:
                ret[i][j] += '<'
            if '^' in m[iloop(i+1)][j]:
                ret[i][j] += '^'
            if 'v' in m[iloop(i-1)][j]:
                ret[i][j] += 'v'
    return ret

def print_map(m):
    for l in m:
        s = []
        for c in l:
            if len(c) == 0:
                s.append('.')
            if len(c) == 1:
                s.append(c)
            if len(c) >= 2:
                s.append(str(len(c)))
        print(''.join(s))

q = [start]
steps = 0
while end not in q:
    m2 = next_map(m)
    q2 = []
    for (i,j) in q:
        if len(m2[i][j]) == 0:
            # wait
            q2.append((i,j))
        if len(m2[i+1][j]) == 0:
            q2.append((i+1,j))
        if len(m2[i-1][j]) == 0:
            q2.append((i-1,j))
        if len(m2[i][j-1]) == 0:
            q2.append((i,j-1))
        if len(m2[i][j+1]) == 0:
            q2.append((i,j+1))
    q = list(set(q2))
    m = m2
    steps += 1

print(steps)
