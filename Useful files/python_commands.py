from cassandra.cluster import Cluster

cluster = Cluster()						#A
session = cluster.connect('demo')		#B

#A create a new cluster instance
#B connect to demo keyspace in our cluster

sesssion.execute('''
	insert into users (lastname, age, city, email, firstname) values ('Jones', 35, 'Austin', 'bob@example.com', 'Bob')
	''') #C
#C insert a user named Bob Jones, 35, live in Austin and email addres is bob@exmple.com

result = session.execute("select * from users where lastname='Jones' ")[0]	#D

#D Retrive all user infromation from user table

session.execute("update users set age = 36 where lastname = 'Jones'")	#E
#E Update Bob's age after his birthday

session.execute("delete from users where lastname = 'Jones'")	#F
#F Delete user whose lastname is Jones from DB

