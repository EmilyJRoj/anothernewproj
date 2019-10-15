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

# 102 sides.

# Accumulators

acc = 0
for X in range(1, 6):
    acc = acc + X

print(acc)

# compute the sum of the first 100 even numbers
# 25

# compute the sum of the first 50 odd numbers
#24

# compute the average of the first 100 odd numbers


# write a function that returns the average of the first N numbers, where N is a parameter.
# each number in the fibonacci sequence is the sum of the previous two numbers
# the first two numbers in the sequence are 1 and 1. compute the 10th fibonacci.
# write a function to compute the Nth fibonacci number, where N is a parameter.
# you may assume that N will be greater than or equal to 3.



