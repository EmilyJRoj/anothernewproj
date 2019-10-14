# starting off
print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numsides, numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSides = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygoncircumference = numSides * side5
    pi = polygonCircumference / 2
    return pi

print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# Experiment with the loop above alongside the actual value of pi. How many
# sides does it take to make the two close?






