
from pymongo.mongo_client import MongoClient

password = "zMRGH2h5D4zRrLsn"
uri = "mongodb+srv://moezeus:"+password+"@mentorham.5hfxzes.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['mentor_HAM'] #nama database bisa disesuaikan
my_collections = db['mentor'] #disesuaikan dengan nama collection

# Data yang ingin dimasukkan
data_1 = {'nama':'Markonah', 'jurusan':'Bahasa', 'Nilai':'98'}
data_2 = {'nama':'Bambang', 'jurusan':'Semanggi', 'Nilai':'99'}
results = my_collections.insert_many([data_1, data_2])

print(results.inserted_ids) #menghasilkan ID data yang dimasukkan