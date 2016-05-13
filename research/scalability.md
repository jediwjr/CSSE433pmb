#Scalability Issues In Database Design
Jiaren Wu, Zhihao Xue, Steven Rasp
####Scalability In Cassandra
The Apache Cassandra database is an open source, distributed, column-based, NoSQL database management system. It claims to provide linear scalability, low latency, and fault-tolerance both locally and on the cloud. It not only provides replication on clusters, it also supports replications across multiple data centers.  
Cassandra clusters work in a peer-to-peer (or “master-less”) ring structure, which means that there is no master or slave nodes across the ring structure. Each node in the ring has the same role and responsibility. And all nodes communicate with each other via a gossip protocol. Furthermore, each ring structure can be a node on a higher level ring.  
Cassandra is linear scalable which mean that the capacity can be increased by adding new nodes or data centers. It scales up and down automatically without any changes in your application's source because there are no "special" nodes.  .  
The overall architecture will depend on whether the simple strategy or network topology strategy is used. Under the simple strategy, sharding will automatically be handled by Cassandra's partitioner. The partitioner by default will randomly hash data into each node, but can be configured to follow an order. So each node would end up with the same amount of data. We can also set a replication factor, which would produce copies of each row. So if we have three nodes and a replication factor of two, each node ends up with 33% of the data based on the sharding, but then ends up getting copies from the previous node in the ring, so that each node should end up holding 66% of the data. 
The network topology strategy can lead to more complex options. Each cluster of nodes would be a data center, and the data centers would form a larger ring. We would then have options like sharding between data centers, so that one data center ends up with all the data for, say, a certain geographic area, and each node in that data center would hold a replica of the data. Since we don't have a large area to cover, we currently plan to stick to the simple strategy, but if we were to scale up we would want to switch to the network topology strategy as we got bigger. 
We also have to consider the impact of the read and write level. These values determine how many nodes we have to be able to access to successfully perform an operation. The options Cassandra offers for read and write level are one, quorum, and all. For level one, the operation only has to be able to successfully perform the operation on one node for the operation to succeed. This means that more nodes can fail before the application experiences problems, but also makes the data only eventually consistent, since the data will get sent to any nodes that need it, but not necessarily at the time of write since a node could be down. Quorum means that a majority of nodes need to respond to the operation for it to be considered successful. All means that every node involved needs to respond. The last two lead to consistent reads for our three node cluster, since under a majority, two of the three would need to write data, and so the data is guaranteed to be there, while for a consistency level of all, all three nodes would get the write from the very beginning. 
 

This brief tutorial will teach you set up a 3 node cluster with Cassandra.

1.You need to know all the IP address of the node. If you are using Ubuntu, following command will show the network interfaces of your machine.

/sbin/ifconfig  

The address of eth0 is the IP address we are going to use.

For example, there are 3 node with following IP address:

Node 1: 192.0.0.1
Node 2: 192.0.0.2
Node 3: 192.0.0.3

2.Before we begin to configure each node, you should close Cassandra in all the nodes. 

sudo ps auwx | grep cassandra
replace PID with the PID of cassandra
sudo kill -9 PID

3 Find the location of cassandra.yaml file.

sudo vim /etc/cassandra/cassandra.yaml

The information that you need to change is same for all nodes. Here is the example configuration for node 1.

seed_provider:
 - seeds: "192.0.0.1, 192.0.0.2, 192.0.0.3”

# Setting listen_address to 0.0.0.0 is always wrong.
listen_address: 192.0.0.1

#Address to broadcast to other Cassandra nodes
broadcast_address: 192.0.0.1

rpc_address: 0.0.0.0

broadcast_rpc_address: 192.0.0.1


After you configured all the node, start Cassandra and you are good to go.
 
sudo service Cassandra start