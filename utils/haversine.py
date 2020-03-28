import math

def haversine(coords1, coords2):
    """
    Haversine formula from https://www.geeksforgeeks.org/haversine-formula-to-find-distance-between-two-points-on-a-sphere/

    Parameters
    ----------
    coords1 : tuple
        Coordinates of point 1
    coords2 : tuple
        Coordinates of point 2

    Returns
    -------
    dist: float
        The distance between coords1 and coords2
    """
    lat1, lon1 = coords1
    lat2, lon2 = coords2

     # distance between latitudes
    # and longitudes
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # apply formulae
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    dist = rad * c
    return dist