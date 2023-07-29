
from flask import Flask
from flask import request
from pymongo.mongo_client import MongoClient
import time

app = Flask('Flask_Testing')
password = "zMRGH2h5D4zRrLsn"
uri = "mongodb+srv://moezeus:"+password+"@mentorham.5hfxzes.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['mentor_HAM'] #nama database bisa disesuaikan
my_collections = db['mentor'] #disesuaikan dengan nama collection

@app.route('/', methods= ['GET'])
def hello_world():
    return 'TEST POST at /sensor1 route'

@app.route('/sensor1',methods=['POST'])
def data():
    temp = request.args.get('temperature')
    hum = request.args.get('humidity')

    if temp is not None: 
        temp = float(temp)
    if hum is not None:
        hum = float(hum)

    kirim_data(temp, hum)
    return f'Uploaded value Temp: {temp}; Humidity:{hum}'

def kirim_data(temp, hum):
    # Data yang ingin dimasukkan
    data_1 = {'timestamp': time.time(), 'temp': temp, 'hum': hum}
    data_2 = {'timestamp': time.time(), 'temp': temp, 'hum': hum}
    results = my_collections.insert_many([data_1, data_2])

    print(results.inserted_ids) #menghasilkan ID data yang dimasukkan

if __name__ == '__main__':
    app.run(host='0.0.0.0')