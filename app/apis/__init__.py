# app/apis/__init__.py
from flask import Blueprint
from flask_restx import Api

# Importar los namespaces
from .person import api as person_ns
# from .user import api as user_ns
# from .vehicle import api as vehicle_ns
# from .register import api as register_ns

# Crear un Blueprint para el API
api_blueprint = Blueprint('v1', __name__)

# Inicialización de la instancia de la clase Api
api = Api(
    api_blueprint,
    title='Park Planner API',
    version='1.0',
    description='The API designed for the residential security system will focus on providing endpoints for the registration of residents, guards, vehicles, and access verification.',
)

# Agregar la instancia de la clase Api al Blueprint

# Agregar los namespaces a la instancia de la clase Api
api.add_namespace(person_ns, path='/persons')
# api.add_namespace(user_ns, path='/users')
# api.add_namespace(vehicle_ns, path='/vehicles')
# api.add_namespace(register_ns, path='/registers')