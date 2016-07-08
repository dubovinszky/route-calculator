from route.file import get_file_contents
from route.kml import get_coordinates
from route.distance import calculate_distances, recalculate_filtered_distances
from route.outliners import get_outliner_indexes


def calculate_total_route(file_path):
    """Calculates the total traveled route in kilometers with filtering the outliner coordinates.

    :param file_path: the path to the KML file
    :retuturns: the total traveled route in kilometers
    :rtype: float

    """

    file_content = get_file_contents(file_path)
    coordinates = get_coordinates(file_content)
    coordinates_with_distances = calculate_distances(coordinates)

    outliner_indexes = get_outliner_indexes([d.get('distance_to', 0) for d in coordinates_with_distances])

    filtered_coordinates_with_distances = recalculate_filtered_distances(coordinates_with_distances, outliner_indexes)

    return sum([d.get('distance_to', 0) for d in filtered_coordinates_with_distances])
