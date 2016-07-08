from math import radians, sin, cos, atan2, pow, sqrt
from itertools import tee, zip_longest

from route.commons import filter_consecutive_duplicates

R = 6371  # the radius of Earth in kilometers


def calculate_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two coorsinates in kilometers
       based on the Haversine formula

    :param lat1: first latitude (type: float)
    :param lon1: first longitude (type: float)
    :param lat2: second latitude (type: float)
    :param lon2: second longitude (type: float)
    :returns: the distance between the two coordinates in kilometers
    :rtype: float

    """

    phi_1 = radians(lat1)
    phi_2 = radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)

    a = pow(sin(delta_phi / 2), 2) + cos(phi_1) * cos(phi_2) * pow(sin(delta_lambda / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


def calculate_distances(coordinates):
    """Calculate distance between coordinates.

    :param coordinates: the list of the coordinates (type: list)
    :returns: list of coodrinates with the original index and the distance to the consecutive coordinate
    :rtype: dict

    """

    filtered_coordinates = filter_consecutive_duplicates(coordinates)
    return [_make_distance_element(i, coordinate_pair)
            for i, coordinate_pair in enumerate(_assemble_coordinate_pairs(filtered_coordinates))]


def recalculate_filtered_distances(distances, indexes):
    for i in reversed(indexes):
        distances.pop(i + 1)
        if i + 1 < len(distances):
            distances[i]['distance_to'] = calculate_distance(distances[i]['lat'], distances[i]['lon'],
                                                             distances[i + 1]['lat'], distances[i + 1]['lon'])

    return distances


def _assemble_coordinate_pairs(coordinates):
    i1, i2 = tee(coordinates)
    next(i2)
    return zip_longest(i1, i2)


def _make_distance_element(index, coordinate_pair):
    c1, c2 = coordinate_pair
    x = {'lat': c1[0], 'lon': c1[1]}
    if c2:
        x['distance_to'] = calculate_distance(*(c1 + c2))
    return x
