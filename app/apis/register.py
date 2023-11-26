# app/apis/register_namespace.py
from app.models import register_model
from app.services.register_service import get_all_services, get_register, create_register, update_register, delete_register
from flask_restx import Namespace, Resource

api = Namespace('Registers', description='Registers related operations')

register = api.model('Register', register_model)

@api.route('/')
class RegisterList(Resource):
    @api.doc('list_registers')
    @api.marshal_list_with(register)
    def get(self):
        '''List all registers'''
        registers = get_all_services()
        return registers

    @api.doc('create_register')
    @api.expect(register)
    @api.marshal_with(register, code=201)
    def post(self):
        '''Create a new register'''
        new_register = create_register(api.payload)
        return new_register, 201

@api.route('/<string:id>')
@api.param('id', 'The register identifier')
@api.response(404, 'Register not found')
class Register(Resource):
    @api.doc('get_register')
    @api.marshal_with(register)
    def get(self, id):
        '''Fetch a register given its identifier'''
        register = get_register(id)
        if register:
            return register
        else:
            api.abort(404, "Register not found")

    @api.doc('update_register')
    @api.expect(register)
    @api.marshal_with(register)
    def put(self, id):
        '''Update a register given its identifier'''
        updated_register = update_register(id, api.payload)
        if updated_register:
            return updated_register
        else:
            api.abort(404, "Register not found")

    @api.doc('delete_register')
    @api.response(204, 'Register deleted')
    def delete(self, id):
        '''Delete a register given its identifier'''
        delete_register(id)
        return '', 204