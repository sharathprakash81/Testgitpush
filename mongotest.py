import pymongo
client = pymongo.MongoClient("mongodb+srv://sp27:be990396@cluster0.hinrq6i.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "Sharath Prakash",
    "email": "sharathprakash81@gmail.com",
    "surname":"Prakash"
}
d={
    "name": "Sharath Prakash",
    "email": "sharathprakash81@gmail.com",
    "surname":"Prakash"
}
d={
    "name": "Sharath Prakash",
    "email": "sharathprakash81@gmail.com",
    "surname":"Prakash"
}
d={
    "name": "Sharath Prakash",
    "email": "sharathprakash81@gmail.com",
    "surname":"Prakash"
}
d={
    "name": "Sharath Prakash",
    "email": "sharathprakash81@gmail.com",
    "surname":"Prakash"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)