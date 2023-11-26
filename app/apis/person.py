# app/models/person.py
from app.models import person_model
from app.services.person_service import get_all_persons, get_person, create_person, update_person, delete_person
from flask_restx import Namespace, Resource

api = Namespace('Persons', description='Persons related operations')

person = api.model('Person', person_model)

@api.route('/')
class PersonResource(Resource):

    @api.doc('list_person')
    @api.marshal_list_with(person)
    def get(self):
        '''List all persons'''
        people = get_all_persons()
        return people
    
    @api.doc('create_person')
    @api.expect(person)
    @api.marshal_with(person, code=201)
    def post(self):
        '''Create a new person'''
        new_person = create_person(api.payload)
        return new_person, 201
    
@api.route('/<string:id>')
@api.param('id', 'The person identifier')
@api.response(404, 'Person not found')
class Person(Resource):
    @api.doc('get_person')
    @api.marshal_with(person)
    def get(self, id):
        '''Fetch a person given its identifier'''
        person = get_person(id)
        if person:
            return person
        else:
            api.abort(404, "Person not found")

    @api.doc('update_person')
    @api.expect(person)
    @api.marshal_with(person)
    def put(self, id):
        '''Update a person given its identifier'''
        updated_person = update_person(id, api.payload)
        if updated_person:
            return updated_person
        else:
            api.abort(404, "Person not found")

    @api.doc('delete_person')
    @api.response(204, 'Person deleted')
    def delete(self, id):
        '''Delete a person given its identifier'''
        delete_person(id)
        return '', 204