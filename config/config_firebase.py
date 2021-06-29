import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def init():
    cred = credentials.Certificate('./serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()
