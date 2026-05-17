import os
import firebase_admin
from firebase_admin import credentials, db

# Construire credentials depuis variables d'environnement
cred_dict = {
    "type": os.environ.get("FIREBASE_TYPE"),
    "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
    "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
    "token_uri": "https://oauth2.googleapis.com/token",
}

# Initialiser Firebase seulement si pas déjà fait
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_dict)

    firebase_admin.initialize_app(cred, {
        "databaseURL": os.environ.get("FIREBASE_DATABASE_URL")
    })

db_ref = db.reference()

def get_firebase_db():
    return db_ref