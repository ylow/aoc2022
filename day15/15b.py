import re
maxx = 0
minx = 100000000000
sensors = []
beacons = []
sensor_range = []

def mand(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for line in open("input", 'r'):
    m = re.match("Sensor at x=([-\d]*), y=([-\d]*): closest beacon is at x=([-\d]*), y=([-\d]*)", line)
    sx = int(m[1])
    sy = int(m[2])
    sensors.append((sx, sy))
    bx = int(m[3])
    by = int(m[4])
    beacons.append((bx, by))
    sensor_range.append(mand(sensors[-1], beacons[-1]))
    maxx = max(maxx, sx)
    maxx = max(maxx, bx)
    minx = min(minx, sx)
    minx = min(minx, bx)

print(sensors)
print(beacons)
print(sensor_range)
print(minx, maxx)

limit = 20
limit = 4000000

#for y in range(1400000,limit + 1):
#    if y % 10000 == 0:
#        print(y, limit)
#    x = 0
#    while x <= limit:
#        ok = True
#        for s in range(len(sensors)):
#            md = mand((x,y), sensors[s]) 
#            if md <= sensor_range[s]:
#                ydelta = abs(sensors[s][1] - y)
#                x += sensor_range[s] - ydelta 
#                ok = False
#        if ok:
#            print((x,y))
#            exit(0)

def probe(x,y):
    if x >= 0 and y >= 0 and x<= limit and y <= limit:
        ok = True
        for s in range(len(sensors)):
            md = mand((x,y), sensors[s]) 
            if md <= sensor_range[s]:
                ok = False
                break
        if ok:
            print((x,y))

for s in range(len(sensors)):
    print(f"Walking sensor {s}")
    # we walk the grid one step outside of its sensor range
    (x,y) = (sensors[s][0] - sensor_range[s] - 1, sensors[s][1])
    probe(x,y)
    for t in range(sensor_range[s] + 1):
        (x,y) = (x+1,y-1)
        probe(x,y)
    print(".")
    assert(mand((x,y), sensors[s]) == sensor_range[s] + 1)
    for t in range(sensor_range[s] + 1):
        (x,y) = (x+1,y+1)
        probe(x,y)
    print(".")
    assert(mand((x,y), sensors[s]) == sensor_range[s] + 1)
    for t in range(sensor_range[s] + 1):
        (x,y) = (x-1,y+1)
        probe(x,y)
    print(".")
    assert(mand((x,y), sensors[s]) == sensor_range[s] + 1)
    for t in range(sensor_range[s] + 1):
        (x,y) = (x-1,y-1)
        probe(x,y)
    assert(mand((x,y), sensors[s]) == sensor_range[s] + 1)
    print(".")
