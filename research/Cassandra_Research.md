 <h1 align='center'> Cassandra </h1> 
## Intruduction
Cassandra is an open-source decentralized database with scalability and high availability without compromising performance. Cassandra's data model offers the convenience of column indexes with the performance of log-structured updates, strong support for denormalization and materialized views, and powerful built-in caching. Furthermore, Cassandra supports MapReduce and query language. 


#### Main Features [1]

##### Fault Tolerant
Data is automatically replicated to multiple nodes for fault-tolerance. Replication across multiple data centers is supported. Failed nodes can be replaced with no downtime.

##### Decentralized
There are no single points of failure. There are no network bottlenecks. Every node in the cluster is identical.

##### Performant
Cassandra consistently outperforms popular NoSQL alternatives in benchmarks and real applications, primarily because of fundamental architectural choices.

##### Durable
Cassandra is suitable for applications that can't afford to lose data, even when an entire data center goes down.

##### Query Language
CQL provides an API to Cassandra that is simpler than the Thrift API. The Thrift API and legacy versions of CQL expose the internal storage structure of Cassandra. CQL adds an abstraction layer that hides implementation details of this structure and provides native syntaxes for collections and other common encodings.

```sql
CREATE KEYSPACE research_demo
  WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };

USE reseach_demo;

CREATE TABLE research_table (id uuid, Last text, First text, PRIMARY KEY(id));

INSERT INTO research_table (id, Last, First) VALUES ('36b6c939-2459-4c24-a1ed-84269ebcd7a1', 'Anderson', 'Thomas');

SELECT * FROM research_table;
```







[1]: http://cassandra.apache.org