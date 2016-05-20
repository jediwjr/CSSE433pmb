from cassandra.cluster import Cluster
import uuid

cluster = Cluster(['137.112.40.137'])
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
    lon text,
    lat text,
    message_sender text
  )
  """)

def view_messages_c():
  return session.execute("SELECT * FROM messages")

def get_messages_c(msg_ids):
  msgs = []
  for msg in msg_ids:
    msgs.append(session.execute("SELECT * FROM messages WHERE message_id = {0}".format(msg))[0])
  return msgs

def send_message_c(m_id,text, username, lat, lon, time):
  session.execute("""
  INSERT INTO messages (message_id, message_content, lon, lat, message_sender)
  VALUES (%s, %s, %s, %s, %s)
  USING TTL %s;
  """,
  (m_id, text,lon,lat, username,time))

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
