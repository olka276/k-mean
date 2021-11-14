from validators import validate_dimensions
from exceptions import UnevenDimensionsError


# a, b are points we are getting distance between of.
def euclidean(a, b):
    if not validate_dimensions(a, b):
        raise UnevenDimensionsError('Uneven tuples given.')

    distsum = 0
    for i in range(len(a)):
        distsum += pow(b[i] - a[i], 2)

    return pow(distsum, 0.5)

