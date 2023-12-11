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

y = 2000000
#y = 10 
ctr = 0
sensor_set = set(sensors)
beacon_set = set(beacons)
for x in range(minx - max(sensor_range), maxx+max(sensor_range)+1):
    coord = (x,y)
    if coord in sensor_set or coord in beacon_set:
        continue
    for s in range(len(sensors)):
        if mand(coord, sensors[s]) <= sensor_range[s]:
            ctr += 1
            break

print(ctr)
