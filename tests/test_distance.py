from pytest import fixture
from route.distance import calculate_distance, calculate_distances, recalculate_filtered_distances


@fixture
def coordinate1():
    return 52.499687, 13.323018


@fixture
def coordinate2():
    return 52.499664, 13.322848


@fixture
def coordinate3():
    return 42.438074, 18.616069


@fixture
def c1_c2_distance():
    return 0.01178835252771814


@fixture
def c2_c3_distance():
    return 1186.629783578611


@fixture
def distances(coordinate1, coordinate2, coordinate3):
    return [{'lat': coordinate1[0], 'lon': coordinate1[1], 'distance_to': 100},
            {'lat': 10, 'lon': 10, 'distance_to': 100},
            {'lat': coordinate2[0], 'lon': coordinate2[1], 'distance_to': 100},
            {'lat': 10, 'lon': 10, 'distance_to': 100},
            {'lat': coordinate3[0], 'lon': coordinate3[1]}]


def test_distance_calculator_close_points(coordinate1, coordinate2, c1_c2_distance):
    distance = calculate_distance(*(coordinate1 + coordinate2))

    assert distance == c1_c2_distance


def test_distance_calculator_far_points(coordinate2, coordinate3, c2_c3_distance):
    distance = calculate_distance(*(coordinate2 + coordinate3))

    assert distance == c2_c3_distance


def test_calculate_distances(coordinate1, coordinate2, coordinate3, c1_c2_distance, c2_c3_distance):
    coordinates = [coordinate1, coordinate2, coordinate3]

    distances = calculate_distances(coordinates)

    assert distances == [{'lat': coordinate1[0], 'lon': coordinate1[1], 'distance_to': c1_c2_distance},
                         {'lat': coordinate2[0], 'lon': coordinate2[1], 'distance_to': c2_c3_distance},
                         {'lat': coordinate3[0], 'lon': coordinate3[1]}]


def test_recalculate_filtered_distances(distances, c1_c2_distance, c2_c3_distance):
    recalculated_coordinates = recalculate_filtered_distances(distances, indexes=[0, 2])

    assert recalculated_coordinates[0]['distance_to'] == c1_c2_distance
    assert recalculated_coordinates[1]['distance_to'] == c2_c3_distance
