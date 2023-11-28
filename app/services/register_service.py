# app/services/register_service.py
from app.extensions import db

def get_all_registers():
    registers = db.child("registers").get()
    if registers.val():
        # Convertir el diccionario de registros a una lista de diccionarios
        registers_list = list(registers.val().items())
        # Asignar el ID como una clave en cada diccionario
        formatted_registers = [{"id": service_id, **service_data} for service_id, service_data in registers_list]
        return formatted_registers
    else:
        return []


def get_register(register_id):
    register = db.child("registers").child(register_id).get()
    return register.val()

def create_register(register_data):
    new_register = {
        "date": register_data["date"],
        "time": register_data["time"],
        "iduser": register_data["iduser"],
        "idvehicle": register_data["idvehicle"],
        "Estado": register_data["Estado"]
    }
    result = db.child("registers").push(new_register)
    new_register["id"] = result["name"]  # Obtener el ID asignado por Firebase
    return new_register

def update_register(register_id, updated_data):
    register = get_register(register_id)
    if register:
        register.update(updated_data)
        db.child("registers").child(register_id).update(register)
        return register

def delete_register(register_id):
    db.child("registers").child(register_id).remove()
