# Machine Learning - Mean Median Mode


import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

mean = numpy.mean(speed)
median = numpy.median(speed)
mode = numpy.bincount(speed).argmax()

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)