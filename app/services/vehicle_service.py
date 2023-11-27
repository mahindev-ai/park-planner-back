# app/services/vehicle_service.py
from app.extensions import db

def get_all_vehicles():
    vehicles = db.child("vehicles").get()
    if vehicles.val():
        return list(vehicles.val().values())
    else:
        return []

def get_vehicle(vehicle_plate):
    vehicle = db.child("vehicles").child(vehicle_plate).get()
    return vehicle.val()

def create_vehicle(vehicle_data):
    new_vehicle = {
        "plate": vehicle_data["plate"],
        "branch": vehicle_data["branch"],
        "model": vehicle_data["model"],
        "idPropietario": vehicle_data["idPropietario"]
    }
    db.child("vehicles").child(vehicle_data["plate"]).set(new_vehicle)
    return new_vehicle

def update_vehicle(vehicle_plate, updated_data):
    vehicle = get_vehicle(vehicle_plate)
    if vehicle:
        vehicle.update(updated_data)
        db.child("vehicles").child(vehicle_plate).update(vehicle)
        return vehicle

def delete_vehicle(vehicle_plate):
    db.child("vehicles").child(vehicle_plate).remove()
