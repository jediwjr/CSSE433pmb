CREATE KEYSPACE IF NOT EXISTS inventory WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1}
/* Create a KEYSPACE in Cassandra if the keyspace name does not exist. To simplify, we will just use simple strategy and use only 1 replication factor. */
use inventory; /* switch to 'inventory' keyspace */
CREATE TABLE IF NOT EXISTS parts (part_number text, description text, compatibility set<text>, price int, manufacturer text, PRIMARY KEY(part_number));
/* create a parts table */
INSERT INTO parts (part_number, description, compatibility, price, manufacturer) VALUES ('FRU324534', '128G NVMe PCIe M.2 SSD', {'W540', 'W541'}, 127, 'Samsung') IF NOT EXISTS ;
INSERT INTO parts (part_number, description, compatibility, price, manufacturer) VALUES ('FRU235123', '2133MHz DDR3 16GB Memory', {'DIMM'}, 70, 'Samsung') IF NOT EXISTS ;
INSERT INTO parts (part_number, description, compatibility, price, manufacturer) VALUES ('FRU324531', '2133MHz DDR3 16GB Memory', {'DIMM'}, 65, 'Corsair') IF NOT EXISTS ;
INSERT INTO parts (part_number, description, compatibility, price, manufacturer) VALUES ('FRU385271', 'DVD-ROM', {'T530','T540','W540'}, 30, 'Lenovo') IF NOT EXISTS ;
/* insert data into part table */
/* This is how parts table looks like */
 part_number | compatibility            | description              | manufacturer | price
-------------+--------------------------+--------------------------+--------------+-------
   FRU235123 |                 {'DIMM'} | 2133MHz DDR3 16GB Memory |      Samsung |    70
   FRU324531 |                 {'DIMM'} | 2133MHz DDR3 16GB Memory |      Corsair |    65
   FRU385271 | {'T530', 'T540', 'W540'} |                  DVD-ROM |       Lenovo |    30
   FRU324534 |         {'W540', 'W541'} |   128G NVMe PCIe M.2 SSD |      Samsung |   127

CREATE TABLE IF NOT EXISTS manufacturers (name text, home_page_url text, NASDAQ_code text,customer_service_number text, PRIMARY KEY(name));
/* create manufacturers table */
INSERT INTO manufacturers (name, home_page_url, NASDAQ_code, customer_service_number) VALUES ('Samsung', 'http://www.samsung.com/us/', 'SSNLF', '800-726-7864') IF NOT EXISTS ;
INSERT INTO manufacturers (name, home_page_url, NASDAQ_code, customer_service_number) VALUES ('Corsair', 'http://www.corsair.com/en-us', 'CRSR', '888-222-4346') IF NOT EXISTS ;
INSERT INTO manufacturers (name, home_page_url, NASDAQ_code, customer_service_number) VALUES ('Lenovo', 'http://www.lenovo.com/us/en/', 'LNVGY', '855-253-6686') IF NOT EXISTS ;
/* insert manufacturers' inforamtion into manufacturers table */

SELECT * FROM manufacturers
/* show all manufacuters' info */
name    | customer_service_number | home_page_url                | nasdaq_code
---------+-------------------------+------------------------------+-------------
 Corsair |            888-222-4346 | http://www.corsair.com/en-us |        CRSR
 Samsung |            800-726-7864 |   http://www.samsung.com/us/ |       SSNLF
  Lenovo |            855-253-6686 | http://www.lenovo.com/us/en/ |       LNVGY


