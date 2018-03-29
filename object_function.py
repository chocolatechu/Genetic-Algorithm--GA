import math


def object_function(decode):
    x1 = decode[0]
    x2 = decode[1]
    x3 = decode[2]
    object_values = 20.0+x1**2+x2**2-10.0*(math.cos(2*math.pi*x3)+math.cos(2*math.pi*x3))
    return 100.0-object_values


