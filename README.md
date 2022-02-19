# Mass_Unit_Converter_API
Microservice API that supports the Food Footprint Calculator. Performs conversions of mass units and returns results in JSON format. Implemented with Python/Flask.

## How to Use:
To convert common mass units, send a GET request to the API endpoint. Parameters for the converter must be included in the GET request as part of the URL path.

In the following URL, replace `<mass>/<units>/<result_units>/` with the current mass, current units, and desired units for the conversion result: 

`https://cs361-mass-unit-converter.herokuapp.com/<mass>/<units>/<result_units>/`

A response will be returned in JSON format and will include the parameters passed to the converter, as well as the resulting mass conversion. The JSON response will have the following structure:

`{"mass": "<mass>", "units": "<units>", "result_units": "<result_units>", "result_mass": "<result_mass>"}`

## List of Acceptable Units:
- lb
- oz
- mg
- g
- kg
- ton (Metric)
- ton (US)
- ton (Imperial)
- st

## Example:
Convert 56 lbs. to kgs. 

GET request sent to the following URL:
`https://cs361-mass-unit-converter.herokuapp.com/56/lb/kg/`

Response in JSON:
`{"mass": "56", "units": "lb", "result_units": "kg", "result_mass": "25.401152"}`