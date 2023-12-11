s = 0
maxs = 0
ses = []
for line in open("input",'r'):
    line = line.strip()
    if len(line) == 0:
        ses.append(s)
        if s > maxs:
            maxs = s
        s = 0
    else:
        s += int(line)

print(maxs)
ses.sort()
print(ses[-3:])
print(sum(ses[-3:]))
