# Q1. What is a database? Differentiate between SQL and NoSQL databases.
# Ans.
#     Database is an organised collection of data stored and accessed electronically.

#     SQL is a Relationsla database management system (RDBMS) with features like
#     vertically scalable; predefined schema; not suitable for hierarchial data storage; good for complex queries.

#     NoSQL is a Distributed database management system with features like
#     horizontally scalable; dynamic schema; best suitable for hierarchial data storage;not good for complex queries.

# Q2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
# Ans.
#     DDL is known as data definition language which is subset of SQL. It describes data and 
#     it's relations in a database. DDL are used to CREATE, ALTER, DROP the database objects like 
#     tables, views, users.
#     CREATE: to create objects in the database
#     ALTER: alters the structure the database
#     DROP: delete data from the table not the table itself
#     TRUNCATE: remove all the records from the table and space allocated for it

import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "abc", password="password")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS CARS")
mycursor.execute("CREATE TABLE IF NOT EXISTS EV(Make VARCHAR, RANGE INT(3), BATT_CAP INT(3))")
mycursor.execute("ALTER TABLE CARS.EV ADD PRICE INT(6)")
mycursor.execute("DROP TABLE CARS.EV")
mycursor.execute("TRUNCATE TABLE CARS.EV")

# Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
# Ans.
#     DML is Data Manipulation Language which is used to manipulate data.
#     It is further classified into Procedural and Non-Procedural DML.

#     INSERT :  insert records into a specified table of the database
mycursor.execute("INSERT INTO CARS.EV VALUES("ATLAS",100, 3.45)")
#     UPDATE : updates/modifies existing data within a table. 
mycursor.execute("UPDATE CARS.EV SET RANGE =90 WHERE RANGE =100")
#     DELETE : DELETE query is used to remove existing records from a specified table.
mycursor.execute("DELETE FROM CARS.EV WHERE RANGE=90")

# Q4. What is DQL? Explain SELECT with an example.
# Ans.
#     DQL is a portion of a SQL statement that allows you to get and organise data from a database. 
#     A SELECT statement retrieves zero or more rows from one or more database tables or database views. 
mycursor.execute("SELECT * FROM CARS.EV")

# Q5. Explain Primary Key and Foreign Key.
# Ans.
#     PRIMARY KEY: A primary key is used to ensure that data in the specific column is unique. 
#     A column cannot have NULL values. It is either an existing table column or a column that 
#     is specifically generated by the database according to a defined sequence.

#     FOREIGN KEY: A foreign key is a column or group of columns in a relational database 
#     table that provides a link between data in two tables. It is a column (or columns) 
#     that references a column (most often the primary key) of another table. 

# Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
# Ans.
# Code to connect MYSQL to python:
import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "abc", password="password")

#     A cursor keeps track of the position in the result set, and allows you to 
#     perform multiple operations row by row against a result set, with or without returning to the original table
mycursor = mydb.cursor()
#     execute() command executes the given database operation (query or command).
mycursor.execute("CREATE DATABASE IF NOT EXISTS CARS")

# Q7. Give the order of execution of SQL clauses in an SQL query.
# Ans.
# =============================================================================
#     The order in which the clauses in queries are executed is as follows:
# 
#     1. FROM/JOIN: The FROM and/or JOIN clauses are executed first to determine the data of interest.
#     2. WHERE: The WHERE clause is executed to filter out records that do not meet the constraints.
#     3. GROUP BY: The GROUP BY clause is executed to group the data based on the values in one or more columns.
#     4. HAVING: The HAVING clause is executed to remove the created grouped records that don’t meet the constraints.
#     5. SELECT: The SELECT clause is executed to derive all desired columns and expressions.
#     6. ORDER BY: The ORDER BY clause is executed to sort the derived values in ascending or descending order.
#     7. LIMIT/OFFSET: Finally, the LIMIT and/or OFFSET clauses are executed to keep or skip a specified number of rows.
# =============================================================================













