import numpy as np
image = np.zeros([800,200], dtype=np.int8)

def drawline(src, dest):
    global image
    mini = min(src[0], dest[0])
    maxi = max(src[0], dest[0]) + 1
    minj = min(src[1], dest[1])
    maxj = max(src[1], dest[1]) + 1
    for i in range(mini, maxi):
        for j in range(minj, maxj):
            image[i,j] = 1

jlimit = 0
for l in open('input','r'):
    seq = [x.split(',') for x in l.strip().split('->')]
    for i in range(len(seq) - 1):
        src = [int(x) for x in seq[i]]
        dest = [int(x) for x in seq[i+1]]
        jlimit = max(jlimit,src[1])
        jlimit = max(jlimit,dest[1])
        drawline(src, dest)

print(jlimit)
jlimit += 2
image = image[:,:jlimit+1]
image[:,jlimit] = 1

s = 0
while image[500,0] == 0:
    sand = [500,0]
    while True:
        if image[sand[0],sand[1]+1] == 0:
            sand[1] += 1
        elif image[sand[0]-1,sand[1]+1] == 0:
            sand[0] -= 1
            sand[1] += 1
        elif image[sand[0]+1,sand[1]+1] == 0:
            sand[0] += 1
            sand[1] += 1
        else:
            break
    image[sand[0],sand[1]] = 2
    s+=1

print(s)

