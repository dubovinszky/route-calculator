# Route Calculator

Route calculator is a small python application for processing routes from KML files in order to calculate the total traveled route in kilometers. It is also apptempts to filter outliner coordinates.

## HOW TO INSTALL
It is proposed to use virtualenv.

 * pyvenv .ve
 * source .ve/bin/activate
 * pip install -r requirements.txt
 
## USAGE

python calculate_route.py <path_to_kml_file>

## RUN TESTS

 * pip install -r dev_requirements.txt
 * py.test tests/

## DEV NOTES

Developed and tested using Python 3.5.1