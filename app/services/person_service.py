# app/services/person_service.py
from app.extensions import db

def get_all_persons():
    people = db.child("persons").get()
    if people.val():
        return list(people.val().values())
    else:
        return []

def get_person(person_id):
    person = db.child("persons").child(person_id).get()
    return person.val()

def create_person(person_data):
    new_person = {
        "name": person_data["name"],
        "identity": person_data["identity"],
        "number":person_data["number"],
        "mail":person_data["mail"],
        "address":person_data["address"],
        "type":person_data["type"],
        "name_type":person_data["name_type"]
    }
    result = db.child("persons").child(new_person["identity"]).set(new_person)
    return new_person

def update_person(person_id, updated_data):
    person = get_person(person_id)
    if person:
        person.update(updated_data)
        db.child("persons").child(person_id).update(person)
        return person

def delete_person(person_id):
    db.child("persons").child(person_id).remove()
