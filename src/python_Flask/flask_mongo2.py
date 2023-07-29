
from flask import Flask
from flask import request
from pymongo.mongo_client import MongoClient

app = Flask('Flask_Testing')
password = "zMRGH2h5D4zRrLsn"
uri = "mongodb+srv://moezeus:"+password+"@mentorham.5hfxzes.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['mentor_HAM'] #nama database bisa disesuaikan
my_collections = db['mentor'] #disesuaikan dengan nama collection

def get_temp_data():
    list_temp = []
    for x in my_collections.find():
        list_temp.append(x['temp'])
    
    result= sum(list_temp)/len(list_temp)
    return str(result)

def get_hum_data():
    list_hum = []
    for x in my_collections.find():
        list_hum.append(x['hum'])
    
    result= sum(list_hum)/len(list_hum)
    return str(result)

@app.route('/', methods= ['GET'])
def hello_world():
    return 'Temp data at /sensor1/temperature/avg and Humidity data at /sensor1/kelembapan/avg'

@app.route('/sensor1/temperature/avg',methods=['GET'])
def show_temp_avg():
    avg_temp = get_temp_data()
    
    return f'average temperature data is: {avg_temp}'

@app.route('/sensor1/kelembapan/avg',methods=['GET'])
def show_temp_hum():
    avg_hum = get_hum_data()
    
    return f'average temperature data is: {avg_hum}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')