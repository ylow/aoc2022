ctr = 0
for row in open("input","r"):
    r = row.strip().split(',')
    l0,r0 = [int(i) for i in r[0].split('-')]
    l1,r1 = [int(i) for i in r[1].split('-')]
    if (l1 <= r0 and r0 <= r1) or (l0 <= r1 and r1 <= r0):
        ctr += 1

print(ctr)
