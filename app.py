# Author: Andrew Blair
# Date: 2/10/2022
# Description: 

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def convert_to_kgs(mass, units):
    """Function has two parmeters: a string that is a mass quantity 
    and a string that is a unit of measurement for mass. Returns 
    the equivaent mass as measured in kilograms."""
    to_kgs = {
        'lb' : 0.453592,
        'oz' : 0.0283495,
        'mg' : 0.000001,
        'g' : 0.001,
        'kg' : 1,
        'ton (metric)' : 1000,
        'ton (us)' : 907.185,
        'ton (imperial)' : 1016.05,
        'st' : 6.35029,
    }
    return float(mass) * to_kgs[units]

def convert_from_kgs(mass, units):
    """Function has two parmeters: a string that is a mass quantity 
    mesured in kilograms and a string that is a unit of measurement 
    for mass. Returns the equivaent mass as measured in the 
    specified units."""
    from_kgs = {
        'lb' : 2.20462,
        'oz' : 35.274,
        'mg' : 1000000,
        'g' : 1000,
        'kg' : 1,
        'ton (metric)' : 0.001,
        'ton (us)' : 0.00110231,
        'ton (imperial)' : 0.000984207,
        'st' : 0.157473,
    }
    return float(mass) * from_kgs[units]

class MassConverter(Resource):
    """###"""
    def get(self, mass, units, result_units):
        """###"""
        kg_mass = convert_to_kgs(float(mass), units)
        result_mass = convert_from_kgs(kg_mass, result_units)
        response_data = {
            'mass': mass,
            'units': units,
            'result_units': result_units,
            'result_mass': str(result_mass),
        }
        return response_data
        
# Register GhgData resource with API at root endpoint
api.add_resource(MassConverter, '/<mass>/<units>/<result_units>/')

if __name__ == "__main__":
    app.run(port=7000)
