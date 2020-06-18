import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase

class Fire():
    def __init__(self):
        self.auth = Fire.init_auth(self)
        self.db = Fire.init_db(self)

    def init_auth(self):  
        firebaseConfig = {
            'apiKey': "AIzaSyAopjFhQL0sG7DqIZpxSOf1NyE5pgK5Y7Y",
            'authDomain': "python-practice-c2a44.firebaseapp.com",
            'databaseURL': "https://python-practice-c2a44.firebaseio.com",
            'projectId': "python-practice-c2a44",
            'storageBucket': "python-practice-c2a44.appspot.com",
            'messagingSenderId': "1037362814034",
            'appId': "1:1037362814034:web:ec43adf22c148f0d2a938b"
        }

        pyreApp = pyrebase.initialize_app(firebaseConfig)
        return pyreApp.auth()

    def init_db(self):
        cred = credentials.Certificate("/Users/akshaykumar/Documents/Projects/FlaskLearning/db_example/key.json")
        firebase_admin.initialize_app(cred)
        return firestore.client()

    def create_user(self, email, password):
        self.auth.create_user_with_email_and_password(email, password)
        return self.auth.sign_in_with_email_and_password(email, password)

    def login(self, email, password):
        return self.auth.sign_in_with_email_and_password(email, password)
