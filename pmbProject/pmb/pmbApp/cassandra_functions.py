from cassandra.cluster import Cluster
import uuid

cluster = Cluster()
session = cluster.connect()

def init_db():
  session.execute("""
  CREATE KEYSPACE IF NOT EXISTS messageboard
  WITH REPLICATION={ 'class': 'SimpleStrategy', 'replication_factor' : 1 };
  """)
  session.execute("USE messageboard")
  session.execute("""
  CREATE TABLE IF NOT EXISTS messages (
    message_id uuid PRIMARY KEY,
    message_content text,
    message_sender text
  )
  """)

def view_messages_c():
  return session.execute("SELECT * FROM messages")

def send_message_c(m_id,text, username):
  session.execute("""
  INSERT INTO messages (message_id, message_content, message_sender) 
  VALUES (%s, %s, %s)
  """,
  (m_id, text, username))

def edit_message_c(m_id, newtext):
  session.execute("""
  UPDATE messages
  SET message_content = %s
  WHERE message_id = %s
  """, (newtext, uuid.UUID(m_id)))

def delete_message_c(m_id):
  session.execute("""
  DELETE FROM messages
  WHERE message_id = {0}
  """.format(m_id))
