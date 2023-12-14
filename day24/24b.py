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

def advance_state(state, i, j):
    if state == 0 and (i,j) == end:
        state = 1
    if state == 1 and (i,j) == start:
        state = 2
    return state

q = [(0, start[0], start[1])]
final_end = (2, end[0], end[1])
steps = 0
while final_end not in q:
    m2 = next_map(m)
    q2 = []
    for (state, i,j) in q:
        if len(m2[i][j]) == 0:
            # wait
            q2.append((state,i,j))
        if i+1 < height and len(m2[i+1][j]) == 0:
            nstate = advance_state(state, i+1,j)
            q2.append((nstate,i+1,j))
        if i-1 >= 0 and len(m2[i-1][j]) == 0:
            nstate = advance_state(state, i-1,j)
            q2.append((nstate,i-1,j))
        if len(m2[i][j-1]) == 0:
            nstate = advance_state(state, i,j-1)
            q2.append((nstate,i,j-1))
        if len(m2[i][j+1]) == 0:
            nstate = advance_state(state, i,j+1)
            q2.append((nstate,i,j+1))
    q = list(set(q2))
    m = m2
    steps += 1

print(steps)
