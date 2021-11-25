import datetime
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['IoT']

col=db['user']

def add_user(temp, humidty, rain):
    json= {
        "Temp": temp,
        "Humidty":humidty,
        "Rain":rain,
        "Date": datetime.datetime.now()
    }
    return col.insert_one(json)

add_user(14,125,"Fales")