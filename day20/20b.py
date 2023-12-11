import copy
n = [int(i) for i in open("input","r")]
permute = copy.deepcopy(n)
ln = len(n)
print(len(set(permute)))
permute = list(enumerate(permute))
KEY = 811589153

for mix in range(10):
    print("Mix", mix)
    ctr = 0
    for i in range(ln):
        index = None
        val = None
        for idx, j in enumerate(permute):
            if j[0] == i:
                index = idx
                val = j[1]
            index
        ctr += 1
        if ctr % 100 == 0:
            print(ctr)

        if val == 0:
            continue
        val = (val * KEY) % (ln - 1)

        if val > 0:
            for j in range(val):
                s = (index+j) % ln
                t = (index+j+1) % ln
                permute[s], permute[t] = permute[t], permute[s]

        if val < 0:
            for j in range(-val):
                s = (index-j) % ln
                t = (index-j-1) % ln
                permute[s], permute[t] = permute[t], permute[s]

ln = len(n) 
z = None
for idx, j in enumerate(permute):
    if j[1] == 0:
        z = idx
        break
print(len(permute))
print(z)
print(permute[(z + 1000) % ln][1]*KEY , permute[(z + 2000) % ln][1]*KEY , permute[(z + 3000) % ln][1]*KEY)
print(permute[(z + 1000) % ln][1]*KEY + permute[(z + 2000) % ln][1]*KEY + permute[(z + 3000) % ln][1]*KEY)

