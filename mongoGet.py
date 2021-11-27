
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['IoT']

col=db['user']

def get_user():
  
  for doc in col.find().sort("Date",-1).limit(1):
    print(doc)

def get_user_M():  
  for doc in col.find().sort("Date",-1).limit(5):
    print(doc)

get_user_M()
