from cassandra.cluster import Cluster

cluster = Cluster(['137.112.104.138'], 9042)
session = cluster.connect()

def init_db():
  #if cluster == None:
  #	cluster = Cluster()
  #	session = cluster.connect()
  session.execute("""
  CREATE KEYSPACE IF NOT EXISTS messageboard
  WITH REPLICATION={ 'class': 'SimpleStrategy', 'replication_factor' : 1 };
  """)
  session.execute("USE messageboard")
  session.execute("""
  CREATE TABLE IF NOT EXISTS messages (
    message_id uuid PRIMARY KEY,
    message_content text
  )
  """)

def view_messages_c():
  return session.execute("SELECT * FROM messages")

def send_message_c(m_id,text):
  session.execute("""
  INSERT INTO messages (message_id, message_content) 
  VALUES (%s, %s)
  """,
(m_id,text))
