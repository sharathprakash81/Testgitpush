import pymongo

client = pymongo.MongoClient("mongodb+srv://sp27:be990396@cluster0.hinrq6i.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["sharath"]

#record= collection.find()
#for i in record:
     # print(i)

#data=collection.find({"companyName": "iNeuron"})
data = collection.find({"courseOffered":{"$gt": "E"}})
for i in data:
    print(i)