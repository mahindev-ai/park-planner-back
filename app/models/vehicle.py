from flask_restx import fields

vehicle_model = {
    'plate': fields.String(required=True, description='Número de placa del vehículo'),
    'branch': fields.String(description='Marca del vehículo'),
    'model': fields.String(description='Modelo del vehículo'),
    'idPropietario': fields.Integer(description='ID del propietario del vehículo')
}