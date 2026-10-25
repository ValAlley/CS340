from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

print("Hello! This is the AAC!")

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    # It is best practice to pass credentials as arguments rather than hardcoding them
    def __init__(self, username='aacuser', password='1234'):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. 
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    # Implement the C in CRUD.
    def create(self, data):
        if data is not None:
            # Fixed variable typo and collection reference
            insert_result = self.collection.insert_one(data)
            
            if insert_result.acknowledged:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, data parameter is empty")

    # Implement the R in CRUD.
    def read(self, searchData=None):
        if searchData is not None:
            # Fixed collection reference
            data = list(self.collection.find(searchData))
            return data
        else:
            raise Exception("Search criteria cannot be empty")
            
    # Implement the U in CRUD
    def update(self, query, updateData):
        if query is not None and updateData is not None:
            # Changed to update_many and returning modified_count
            result = self.collection.update_many(query, {"$set": updateData})
            return result.modified_count
        else: # Added missing colon
            raise Exception("Nothing to update, query or updateData is empty")
            
    # Implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            # Changed to delete_many and returning deleted_count
            result = self.collection.delete_many(deleteData)
            return result.deleted_count
        else: # Added missing colon
            raise Exception("Nothing to delete, deleteData is empty")