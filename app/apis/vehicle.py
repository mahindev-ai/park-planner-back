# app/apis/vehicle_namespace.py
from app.models import vehicle_model
from app.services.vehicle_service import get_all_vehicles, get_vehicle, create_vehicle, update_vehicle, delete_vehicle
from flask_restx import Namespace, Resource

api = Namespace('Vehicles', description='Vehicles related operations')

vehicle = api.model('Vehicle', vehicle_model)

@api.route('/')
class VehicleList(Resource):
    @api.doc('list_vehicles')
    @api.marshal_list_with(vehicle)
    def get(self):
        '''List all vehicles'''
        vehicles = get_all_vehicles()
        return vehicles

    @api.doc('create_vehicle')
    @api.expect(vehicle)
    @api.marshal_with(vehicle, code=201)
    def post(self):
        '''Create a new vehicle'''
        new_vehicle = create_vehicle(api.payload)
        return new_vehicle, 201

@api.route('/<string:plate>')
@api.param('plate', 'The vehicle plate')
@api.response(404, 'Vehicle not found')
class Vehicle(Resource):
    @api.doc('get_vehicle')
    @api.marshal_with(vehicle)
    def get(self, plate):
        '''Fetch a vehicle given its plate'''
        vehicle = get_vehicle(plate)
        if vehicle:
            return vehicle
        else:
            api.abort(404, "Vehicle not found")

    @api.doc('update_vehicle')
    @api.expect(vehicle)
    @api.marshal_with(vehicle)
    def put(self, plate):
        '''Update a vehicle given its plate'''
        updated_vehicle = update_vehicle(plate, api.payload)
        if updated_vehicle:
            return updated_vehicle
        else:
            api.abort(404, "Vehicle not found")

    @api.doc('delete_vehicle')
    @api.response(204, 'Vehicle deleted')
    def delete(self, plate):
        '''Delete a vehicle given its plate'''
        delete_vehicle(plate)
        return '', 204
