from flask_restx import fields

user_model = {
    'id': fields.String(description='ID del usuario'),
    'username': fields.String(description='Nombre de usuario'),
    'password': fields.String(description='Contraseña del usuario'),
    'role': fields.Integer(description='ID del rol del usuario'),
    'role_name': fields.String(description='Nombre del rol del usuario')
}