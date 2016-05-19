from neo4j.v1 import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "Yellowsubmarine49"))
session = driver.session()

def create_user(un):
    session.run("CREATE (u:User {username: {username}})", {"username": un})

def create_message(msg_id):
    session.run("CREATE (m:Message {msg_id: {msg_id}})", {"msg_id": msg_id})

def add_like(user,msg):
    session.run("MATCH (u:User {username:{username}}), (m:Message {msg_id:{msg_id}}) CREATE UNIQUE (u)-[r:LIKES]->(m) RETURN r", {"username":user, "msg_id":msg})

def remove_like(user,msg):
    session.run("MATCH (u:User)-[rel:LIKES]->(m:Message) WHERE u.username={username} AND m.msg_id={msg_id} DELETE rel",{"username":user, "msg_id":msg})

def likes(user,msg):
    result = session.run("MATCH (u:User)-[r:LIKES]->(m:Message) WHERE u.username={username} AND m.msg_id={msg_id} RETURN r",{"username":user, "msg_id":msg})
    result = list(result)
    return len(result) >= 1

def recommendation(user):
    results = session.run("MATCH (u:User)-[:LIKES]->(m:Message)<-[:LIKES]-(u2:User) WHERE u.username = {username} MATCH (u2)-[:LIKES]->(m2:Message) WHERE m2.msg_id <> m.msg_id RETURN m2.msg_id", {"username": user})
    results = list(results)
    return results
