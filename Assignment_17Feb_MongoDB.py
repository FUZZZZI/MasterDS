# Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios 
#     it is preferred to use MongoDB over SQL databases?
# Ans.
#     MongoDB is an open source document based NoSQL database management program. 
#     NoSQL is used as an alternative to traditional relational databases.

#     A non-relational database is a database that does not use the tabular schema 
#     of rows and columns found in most traditional database systems.
#     Instead, non-relational databases use a storage model that is optimized for 
#     the specific requirements of the type of data being stored.
#     All the related data can be stored in a single document.

#     Scenrarios to prefer MongoDB oevr SQL database:
#     When Integrating large amounts of diverse data
#     When you have complex data structures that evolve
#     When you need to accommodate massive scale
#     When you are rapidly prototyping

# Q2. State and Explain the features of MongoDB.
# Ans. 
#     1. Ad-hoc queries for optimized, real-time analytics:
#        MongoDB supports field queries, range queries, and regular expression searches. 
#        Queries can return specific fields and also account for user-defined functions.
#     2. Indexing appropriately for better query executions
#     3. Replication for better data availability and stability
#     4. Sharding: the process of splitting larger datasets across multiple distributed collections.
#     5. Load balancing

# Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.
# Ans.
# Connect MongoDB to python
import pymongo
client = pymongo.MongoClient("mongodb+srv://test:pwskills@cluster0.ytqtgyf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
#Test the connection
client
#Create a database
db1 = client["database1"]
#Create a collection
col1 = db1["collection1"]

# Q4. Using the database and the collection created in question number 3, write a code to insert 
#     one record, and insert many records. Use the find() and find_one() methods to print the inserted record.
# Ans.
data1 = {
    "name":"agra", "state":"up", "zip":282001
    }
col1.insert_one(data1)

data2 = {"location":"ewns"}, {"class":"pwskills"}, {"website":"pwskills.com"}
col1.insert_many(data2)

#Print the inserted records
for i in col1.find():
    print(i)
for i in col1.find_one():
    print(i)

# Q5. Explain how you can use the find() method to query the MongoDB database. 
#     Write a simple code to demonstrate this.
# Ans.
#     In mongoDB, the find() method is used to fetch a particular data from the table. 
#     In other words, it is used to select data in a table. It is also used to return 
#     all events to the selected data. The find() method consists of two parameters by 
#     which we can find a particular record.
#     query: This is an optional parameter that defines the selection criteria. 
#     In simple words, it defines a query as what you want to find in a collection.
#     projection: This is an optional parameter that defines what to return if the query 
#     criteria are met successfully. In simple words, it is a type of decision-making 
#     that decides on criteria
for i in col1.find({"state":"up"}):
    print(i)
for i in col1.find({"zip":{"$gte":2800}}):
    print(i)

# Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.
# Ans.
#     The sort() method specifies the order in which the query returns the matching 
#     documents from the given collection. You must apply this method to the cursor 
#     before retrieving any documents from the database.

data3 = {"make":"Nissan", "model":"GTR", "year":2016}, {"make":"BMW", "model":"X5", "year":2020},{"make":"Toyota", "model":"Yaris", "year":2018},{"make":"Ford", "model":"Transit", "year":2017}
col1.insert_many(data3)

#Example
for i in col1.find().sort("year"):
    print(i)
#     Here the data is sorted by "year" field in ascending order.

# Q7. Explain why delete_one(), delete_many(), and drop() is used.
# Ans.
#     delete_one() deletes the first documents that matches with the filter.
#     delete_many() is used when one needs to delete more than one document.
#     drop() method is used to drop a collection from a database.
col1.delete_one({"class":"pwskills"})
for i in col1.find():
    print(i)
#Finally dropping the collection
col1.drop()
