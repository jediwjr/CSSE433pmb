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

#### Data Model [3]

<!--(
##### Keyspace [2]
The outermost grouping of data, similar to a schema in a relational database. All tables go inside a keyspace. A keyspace is the defining container for replication.

##### Table [2]
A table stores data based on a primary key, which consists of a partition key and optional clustering columns.
  * A partition key defines the node on which the data is stored.
  * A clustering column defines the order of data stored in a row.
  * A primary key is used to access the data in the table.
  ![alt text](http://docs.datastax.com/en/landing_page/doc/landing_page/images/table.png "Table In Cassandra")
)-->
Data modeling is a process that involves identifying the entities (items to be stored) and the relationships between entities. To create your data model, identify the patterns used to access data and the types of queries to be performed. These two ideas inform the organization and structure of the data, and the design and creation of the database's tables. Indexing the data can improve performance in some cases, so decide which columns will have secondary indexes.

Data modeling in Cassandra uses a query-driven approach, in which specific queries are the key to organizing the data. Queries are the result of selecting data from a table; schema is the definition of how data in the table is arranged. Cassandra's database design is based on the requirement for fast reads and writes, so the better the schema design, the faster data is written and retrieved.

In contrast, relational databases normalize data based on the tables and relationships designed, and then writes the queries that will be made. Data modeling in relational databases is table-driven, and any relationships between tables are expressed as table joins in queries.

Cassandra's data model is a partitioned row store with tunable consistency. Tunable consistency means for any given read or write operation, the client application decides how consistent the requested data must be. Rows are organized into tables; the first component of a table's primary key is the partition key; within a partition, rows are clustered by the remaining columns of the key. Other columns can be indexed separately from the primary key. Because Cassandra is a distributed database, efficiency is gained for reads and writes when data is grouped together on nodes by partition. The fewer partitions that must be queried to get an answer to a question, the faster the response. Tuning the consistency level is another factor in latency, but is not part of the data modeling process.

Cassandra data modeling focuses on the queries. Throughout this topic, the example of Pro Cycling statistics demonstrates how to model the Cassandra table schema for specific queries. The conceptual model for this data model shows the entities and relationships.
![alt text](http://docs.datastax.com/en/cql/3.3/cql/images/cyclist-conceptual.png )
The entities and their relationships are considered during table design. Queries are best designed to access a single table, so all entities involved in a relationship that a query encompasses must be in the table. Some tables will involve a single entity and its attributes, like the first example shown below. Others will involve more than one entity and its attributes, such as the second example. Including all data in a single Cassandra table contrasts with a relational database approach, where the data would be stored in two or more tables and foreign keys would be used to relate the data between the tables. Because Cassandra uses this single table-single query approach, queries can perform faster.

One basic query (Q1) for Pro Cycling statistics is a list of cyclists, including each cyclist's id, firstname, and lastname. To uniquely identify a cyclist in the table, an id using UUID is used. For a simple query to list all cyclists a table that includes all the columns identified and a partition key (K) of id is created. The diagram below shows a portion of the logical model for the Pro Cycling data model.

**Query 1: Find a cyclist's name with a specified id**

![alt text](http://docs.datastax.com/en/cql/3.3/cql/images/cyclist-logical-Q1.png)

A related query (Q2) searches for all cyclists by a particular race category. For Cassandra, this query is more efficient if a table is created that groups all cyclists by category. Some of the same columns are required (id, lastname), but now the primary key of the table includes category as the partition key (K), and groups within the partition by the id (C). This choice ensures that unique records for each cyclist are created.

**Query 2: Find cyclists given a specified category**

![alt text](http://docs.datastax.com/en/cql/3.3/cql/images/cyclist-logical-Q2.png)

These are two simple queries; more examples will be shown to illustrate data modeling using CQL.
Notice that the main principle in designing the table is not the relationship of the table to other tables, as it is in relational database modeling. Data in Cassandra is often arranged as one query per table, and data is repeated amongst many tables, a process known as denormalization. Relational databases instead normalize data, removing as much duplication as possible. The relationship of the entities is important, because the order in which data is stored in Cassandra can greatly affect the ease and speed of data retrieval. The schema design captures much of the relationship between entities by including related attributes in the same table. Client-side joins in application code is used only when table schema cannot capture the complexity of the relationships.


## Installation [4]
##### Tarball installation of Cassandra 3.x on Linux-based platform
**Prerequisites**
  * Linux-based platform
  * Lastest version of Java platform
  * Python 2.7

**Procedure**
In a terminal window

1. Check the version of Java is installed (latest version of Oracle Java 8 is recommended)
    ```bash
    $ java -version
    ```
    
2. Download the Cassandra 3.x form Datastax Distribution:

    ```bash
    $ curl -L http://downloads.datastax.com/datastax-ddc/datastax-ddc-version_number-bin.tar.gz | tar xz
    ```  
    or from Planet Cassandra http://www.planetcassandra.org/cassandra  
    
    Please **replace 3.x to the version number you want to install**

3. Untar the file:

   ```bash
   $ tar -xvzf datastax-ddc-version_number-bin.tar.gz
   ```

4. To configure Cassandra, go to the install/conf directory:

    ```bash
    $ cd datastax-ddc-version_number/conf
    ```

5. Start Cassandra in a single-node cluster:

    ```bash
    $ cd install_location
    $ bin/cassandra ## use -f to start Cassandra in the foreground
    ```

6. Verify that Cassandra is running:

    ```bash
    $ cd install_location
    $ bin/nodetool status
    ```
    ```bash
    Datacenter: datacenter1
    =======================
    Status=Up/Down 
    |/ State=Normal/Leaving/Joining/Moving
    --  Address             Load       Tokens  Owns    Host ID                               Rack
    UN  127.0.0.147.66 KB   47.66 KB   256     100%    aaa1b7c1-6049-4a08-ad3e-3697a0e30e10  rack1
    ```

For installation on a specific opeartion system, please refer [installation manual].

   

[1]: http://cassandra.apache.org
[2]: http://docs.datastax.com/en/landing_page/doc/landing_page/dataModeling.html
[3]: http://docs.datastax.com/en/cql/3.3/cql/ddl/dataModelingApproach.html
[4]: http://docs.datastax.com/en/cassandra/3.x/cassandra/install/installTarball.html
[installation manual]: http://docs.datastax.com/en/cassandra/3.x/cassandra/install/installTOC.html