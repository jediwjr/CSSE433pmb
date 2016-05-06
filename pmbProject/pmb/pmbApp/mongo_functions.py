import pymongo
from pymongo import MongoClient
import hashlib
client = MongoClient()
db = client.messageboard
def get_user(username, password):
  users = db['users']
  user = users.find_one({"username": username, "password": password})
  return user

def add_user(username, password):
  users = db['users']
  user = {"username": username,
          "password": password}
  result = users.insert_one(user).inserted_id
  return result
