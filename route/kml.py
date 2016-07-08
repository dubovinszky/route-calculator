from bs4 import BeautifulSoup

from route.exceptions import InvalidKMLNoLineString, AltitudeModeNotImplemented, InvalidKMLNoCoordinates

SUPPORTED_ALTITUDE_MODES = ['clampToGround']


def get_coordinates(kml_string):
    """Returns with the coordinates from the kml_string

    :param kml_string: the content of the KML file (type:str)
    :returns: the list of the coordinates
    :rtype: list

    """

    coordinates = _parse_coordinates(kml_string)
    return [_convert_coordinates(c) for c in filter(lambda x: x.strip() != '', coordinates.text.split(' '))]


def _convert_coordinates(coordinates):
    coordinate_parts = coordinates.split(',')

    return (float(coordinate_parts[0]), float(coordinate_parts[1]))


def _parse_coordinates(kml_string):
    kml = BeautifulSoup(kml_string, 'xml')

    line_string = _find_element(find_in=kml, element_name='LineString', on_error=InvalidKMLNoLineString)
    _check_altitude_mode(line_string)
    return _find_element(find_in=line_string, element_name='coordinates', on_error=InvalidKMLNoCoordinates)


def _find_element(find_in, element_name, on_error):
    element = find_in.find(element_name)
    if not element:
        raise on_error

    return element


def _check_altitude_mode(find_in):
    altitude_mode = find_in.find('altitudeMode').text
    if altitude_mode not in SUPPORTED_ALTITUDE_MODES:
        raise AltitudeModeNotImplemented
