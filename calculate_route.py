import sys
from route.core import calculate_total_route
from route.exceptions import InvalidKMLNoLineString, InvalidKMLNoCoordinates, AltitudeModeNotImplemented


if __name__ == '__main__':
    try:
        total_route = calculate_total_route(sys.argv[1])
    except IndexError:
        print("Please specify a file argument.")
    except FileNotFoundError:
        print("Please enter an existing file name.")
    except InvalidKMLNoLineString:
        print("Invalid KML file: no LineString were found!")
    except InvalidKMLNoCoordinates:
        print("Invalid KML file: no coordinated were found!")
    except AltitudeModeNotImplemented:
        print("Invalid altitude mode: only 'clampToGround' is supported!")
    else:
        print('The total route without the outliner coordinates is {} kilometers'.format(total_route))
