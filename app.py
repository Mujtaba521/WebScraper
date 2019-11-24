from pymongo import MongoClient
# import clientData from app
client = MongoClient("mongodb+srv://admin:kK%23H7u%40SRp2ubKz@bankingdb-mesj0.mongodb.net/test?retryWrites=true&w=majority")

def clientData():
    db = client["Banking"]
    user1 = {
        "name": "Bill Mahor",
        "age":"20",
        "birthday": "23-11-2000"
    }
    user2 = {
        "name": "Stevan Klien",
        "age": "10",
        "birthday": "23-05-1819"
    }
    user3 = {
        "name": "Michael Ross",
        "age": "20",
        "birthday": "23-11-1999"
    }
    user4 = {
        "name": "Joseph Albert",
        "age": "42",
        "birthday": "23-11-1993"
    }
    user5 = {
        "name": "Diego Robertez",
        "age": "34",
        "birthday": "23-11-1985"
    }
    user6= {
        "name" : "Steve Madden",
        "age" : "19",
        "birthday" : "23-11-2004"

    }

    store = []
    #db['User'].insert_one(user1)
    for item in db['User'].find(user1).explain()['queryPlanner']['parsedQuery']['$and'][0:]:
        if(item.get('name') != None):
            store.append(item.get('name')['$eq'])

    for item in db['User'].find(user2).explain()['queryPlanner']['parsedQuery']['$and'][0:]:
        if(item.get('name') != None):
            store.append(item.get('name')['$eq'])

    for item in db['User'].find(user3).explain()['queryPlanner']['parsedQuery']['$and'][0:]:
        if(item.get('name') != None):
            store.append(item.get('name')['$eq'])

    for item in db['User'].find(user4).explain()['queryPlanner']['parsedQuery']['$and'][0:]:
        if(item.get('name') != None):
            store.append(item.get('name')['$eq'])

    for item in db['User'].find(user5).explain()['queryPlanner']['parsedQuery']['$and'][0:]:
        if(item.get('name') != None):
            store.append(item.get('name')['$eq'])

    for item in db['User'].find(user6).explain()['queryPlanner']['parsedQuery']['$and'][0:]:
        if(item.get('name') != None):
            store.append(item.get('name')['$eq'])
    return store

clientData()

