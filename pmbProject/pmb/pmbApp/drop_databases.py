from cassandra.cluster import Cluster
import pymongo
from pymongo import MongoClient
from neo4j.v1 import GraphDatabase, basic_auth

cluster = Cluster(['137.112.40.137'])
session = cluster.connect()
session.execute("USE messageboard")
session.execute("DROP TABLE messages")

client = MongoClient('137.112.104.138')
db = client.messageboard
db.users.drop()

driver = GraphDatabase.driver("bolt://137.112.40.137", auth=basic_auth("neo4j", "Yellowsubmarine49"))
session = driver.session()
session.run("MATCH (n) DETACH DELETE n")
