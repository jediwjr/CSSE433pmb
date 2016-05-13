from neo4j.v1 import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "Yellowsubmarine49"))
session = driver.session()

def create_user(un):
    session.run("CREATE (u:User {username: {username}})", {"username": un})

def create_message(msg_id):
    session.run("CREATE (m:Message {msg_id: {msg_id}})", {"msg_id": msg_id})

def add_like(user,msg):
    session.run("MATCH (u:User {username:{username}}), (m:Message {msg_id:{msg_id}}) CREATE UNIQUE (u)-[:LIKES]->(m)", {"username":user, "msg_id":msg})

def remove_like(user,msg):
    session.run("MATCH (u:User)-[rel:LIKES]->(m:Message) WHERE u.username={username} AND m.msg_id={msg_id} DELETE rel",{"username":user, "msg_id":msg})

def likes(user,msg):
    result = session.run("MATCH (u:User)-[:LIKES]->(m:Message) WHERE u.username={username} AND m.msg_id={msg_id}",{"username":user, "msg_id":msg})
    return result != None
