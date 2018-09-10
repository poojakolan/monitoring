from flask import Flask
import pymongo

app1 = Flask(__name__)

@app1.route('/sayHello')
def hello_world():
    return 'Hello, World!'

@app1.route('/api2')
def hello_world_api2():
    return 'Hello, World! from api2'

@app1.route('/mongoTest')
def hello_world_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["local"]
    mycol = mydb['student']
    mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(mydict)
    print(x)
    return "mongo "+ str(x.inserted_id)

@app1.route('/mongoRead')
def hello_world_mongo_read():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["local"]
    mycol = mydb['student']
    x = mycol.find_one()
    print(x)
    return "mongo "+ str(x)
