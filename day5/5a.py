c = {}
c[1] = "NRGP"
c[2] = "JTBLFGDC"
c[3] = "MSV"
c[4] = "LSRCZP"
c[5] = "PSLVCWDQ"
c[6] = "CTNWDMS"
c[7] = "HDGWP"
c[8] = "ZLPHSCMV"
c[9] = "RPFLWGZ"

for k in c.keys():
    c[k] = list(c[k])

import re
for line in open("input"):
    matches = re.match(r"move (\d*) from (\d*) to (\d*)", line)
    n = int(matches[1])
    s = int(matches[2])
    t = int(matches[3])
    print(n,s,t)
    for i in range(n):
        v = c[s].pop()
        c[t].append(v)

r = []
for k in sorted(c.keys()):
    r.append(c[k][-1])

print(''.join(r))



