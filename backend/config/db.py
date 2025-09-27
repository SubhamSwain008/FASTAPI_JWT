from pymongo import MongoClient 
import os
from dotenv import load_dotenv
load_dotenv()

try :
    client = MongoClient(os.getenv("MONGO_URI"))
    print("DB Connected")
except:
    print("failed to connect to db")