from pyrebase import initialize_app

# Configuración de Firebase (importada desde config/firebase_config.py)
from app.config.firebase_config import firebase_config
# Inicialización de Firebase
firebase = initialize_app(firebase_config)
db = firebase.database()