from app.extensions import db

def get_all_users():
    # Ejemplo: Obtener todos los usuarios de la base de datos
    users = db.child("users").get()
    if users.val():
        return list(users.val().values())
    else:
        return []

def get_user(user_id):
    # Ejemplo: Obtener un usuario de la base de datos
    user = db.child("users").child(user_id).get()
    return user.val()

def create_user(user_data):
    new_user = {
        "id": user_data["id"],
        "username": user_data["username"],
        "password": user_data["password"],
        "role": user_data.get("role", 1),  # Asignar un rol predeterminado si no se proporciona
        "role_name": user_data["role_name"]
    }
    db.child("users").child(new_user["id"]).set(new_user)
    return new_user

def update_user(user_id, updated_data):
    # Ejemplo: Actualizar un usuario en la base de datos
    user = get_user(user_id)
    if user:
        user.update(updated_data)
        db.child("users").child(user_id).update(user)
        return user

def delete_user(user_id):
    # Ejemplo: Eliminar un usuario de la base de datos
    db.child("users").child(user_id).remove()
