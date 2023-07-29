
from pymongo.mongo_client import MongoClient

password = "zMRGH2h5D4zRrLsn"
uri = "mongodb+srv://moezeus:"+password+"@mentorham.5hfxzes.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client['mentor_HAM'] #nama database bisa disesuaikan
my_collections = db['mentor'] #disesuaikan dengan nama collection

# Read Data
for x in my_collections.find():
    print(x)