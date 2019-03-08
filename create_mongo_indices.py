import pymongo

client = pymongo.MongoClient()
c = client['watercaller']
print(c.users.create_index('email', unique=True))
print(c.requests.creat_index('table_id', unique=True))
