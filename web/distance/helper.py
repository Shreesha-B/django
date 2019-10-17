from math import sin, cos, sqrt, atan2


def calc(lon1, lon2, lat1, lat2):

    r = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = r * c

    return distance
