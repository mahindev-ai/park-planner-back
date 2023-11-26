from flask_restx import fields

person_model = {
    'id': fields.Integer(description='ID de la persona'),
    'name': fields.String(description='Nombre de la persona'),
    'identity': fields.String(description='Identidad de la persona'),
    'number': fields.String(description='Número de la persona'),
    'mail': fields.String(description='Correo de la persona'),
    'address': fields.String(description='Dirección de la persona'),
    'type': fields.Integer(description='Tipo de persona (Residente o visitante)'),
    'name_type': fields.String(description='Nombre del tipo de persona')
}