from pytest import fixture, raises

from route.kml import get_coordinates
from route.exceptions import InvalidKMLNoLineString, AltitudeModeNotImplemented, InvalidKMLNoCoordinates


@fixture
def kml_without_linestring():
    return """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2"  xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    <Document>
    </Document>
    """


@fixture
def kml_with_wrong_altitude_mode():
    return """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2"  xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    <Document>
        <Folder>
            <Placemark>
                <LineString>
                    <altitudeMode>relativeToGround</altitudeMode>
                </LineString>
            </Placemark>
        </Folder>
    </Document>
    """


@fixture
def kml_without_coordinates():
    return """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2"  xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    <Document>
        <Folder>
            <Placemark>
                <LineString>
                    <altitudeMode>clampToGround</altitudeMode>
                </LineString>
            </Placemark>
        </Folder>
    </Document>
    """


@fixture
def kml():
    return """<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2"  xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
    <Document>
        <Folder>
            <Placemark>
                <LineString>
                    <altitudeMode>clampToGround</altitudeMode>
                    <coordinates>
                        13.323018,52.499687,0 13.323018,52.499687,0 13.323018,52.499687,0
                    </coordinates>
                </LineString>
            </Placemark>
        </Folder>
    </Document>
    """


def test_get_coordinates_without_linestring(kml_without_linestring):
    with raises(InvalidKMLNoLineString):
        get_coordinates(kml_without_linestring)


def test_get_coordinates_with_wrong_altitude_mode(kml_with_wrong_altitude_mode):
    with raises(AltitudeModeNotImplemented):
        get_coordinates(kml_with_wrong_altitude_mode)


def test_get_coordinates_without_coordinates(kml_without_coordinates):
    with raises(InvalidKMLNoCoordinates):
        get_coordinates(kml_without_coordinates)


def test_get_coordinates(kml):
    coordinates = get_coordinates(kml)
    assert coordinates == [(13.323018, 52.499687), (13.323018, 52.499687), (13.323018, 52.499687)]
