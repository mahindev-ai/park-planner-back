# app/models/person.py
from app.models import person_model
from flask_restx import Namespace, Resource

api = Namespace('persons', description='Persons related operations')

person = api.model('Person', person_model)

@api.route('/')
class PersonResource(Resource):
    @api.doc('list_person')
    def get(self):
        return {'hello': 'world'}