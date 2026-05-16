import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from pathlib import Path

# Obtenir le chemin du dossier actuel (appfood) de manière absolue
BASE_DIR = Path(__file__).resolve().parent

# Construire le chemin complet vers le fichier firebase_key.json
# Cela garantit que le chemin est correct, peu importe où le serveur est lancé
CREDENTIALS_PATH = os.path.join(BASE_DIR, 'firebase_key.json')

# Initialiser Firebase
cred = credentials.Certificate(CREDENTIALS_PATH)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bssfood-7eeec-default-rtdb.europe-west1.firebasedatabase.app/'
})
db_ref = db.reference()

def get_firebase_db():
    return db_ref