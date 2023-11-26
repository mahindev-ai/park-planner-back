from flask_restx import fields

register_model = {
    'id': fields.String(description='ID del registro'),
    'date': fields.String(description='Fecha del registro'),
    'time': fields.String(description='Hora del registro'),
    'iduser': fields.Integer(description='ID del usuario que registró'),
    'idvehicle': fields.String(description='Número de placa del vehículo registrado'),
    'Estado': fields.Boolean(description='Estado del registro')
}