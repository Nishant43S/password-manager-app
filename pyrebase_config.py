import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

config = {
  "apiKey": os.getenv("API_KEY"),
  "authDomain": os.getenv("ADMIN_DOMAIN"),
  "databaseURL": os.getenv("DB_URL"),
  "projectId": os.getenv("PROJECT_ID"),
  "storageBucket": os.getenv("STORAGE_BUCKET"),
  "messagingSenderId": os.getenv("SENDER_ID"),
  "appId": os.getenv("APP_ID")
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

