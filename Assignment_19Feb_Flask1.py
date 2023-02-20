# Q1. What is Flask Framework? What are the advantages of Flask Framework?
# Ans.
#     Flask is a web application framework written in Python. This means flask 
#     provides you with tools, libraries and technologies that allow you to build 
#     a web application. This web application can be some web pages, a blog, a
#     wiki or go as big as a web-based calendar application or a commercial website.

#     It is classified as a microframework because it does not require particular 
#     tools or libraries. It has no database abstraction layer, form validation, 
#     or any other components where pre-existing third-party libraries provide common functions.

#     Flask API can be used to create your own web API using Flask.

#     Advantages:- Scalable; Flexible; Easy to negotiate; Lightweight; Documentation

# Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the 
#     screenshot of the output in Jupyter Notebook.
from flask import Flask
app = Flask(__name__)               
@app.route("/")                 #route from a server location            
def hello_world():
    return "Hello, World!!"
if __name__=="__main__":
    app.run(host="0.0.0.0")
    
#     Below is the screenshot of required output in local machine browser.
https://github.com/FUZZZZI/MasterDS/blob/main/Snap208.jpg
# Q3. What is App routing in Flask? Why do we use app routes?
# Ans.
#     App Routing means mapping the URLs to a specific function that will handle 
#     the logic for that URL. 

#     Modern web frameworks use the routing technique to help a user remember 
#     application URLs. It is useful to access the desired page directly without 
#     having to navigate from the home page.

# Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
#     route to show the following details:
#     Company Name: ABC Corporation
#     Location: India
#     Contact Detail: 999-999-9999
#     Attach the screenshot of the output in Jupyter Notebook.
# Ans.
from flask import Flask
app = Flask(__name__)               
@app.route("/welcome")                 #route from a server location            
def message1():
    return "Welcome to ABC Corporation"
@app.route("/")
def comp_details():
    while True:
        str = "Company Name: ABC Corporation<br>Location: india<br>Contact Detail: 999-999-9999"
        return str
if __name__=="__main__":
    app.run(host="0.0.0.0")

#     Below is the screenshot of required output in local machine browser.
https://github.com/FUZZZZI/MasterDS/blob/main/Snap170.jpg

# Q5. What function is used in Flask for URL Building? Write a Python code to 
#     demonstrate the working of the url_for() function.
# Ans.
#     To build a URL to a specific function, we use the url_for() function. 
#     It accepts the name of the function as its first argument and any number 
#     of keyword arguments, each corresponding to a variable part of the URL rule.
#     Unknown variable parts are appended to the URL as query parameters.

from flask import Flask, url_for
app = Flask(__name__)               
@app.route("/hello")                 #route from a server location            
def hello_world():
    return "Hello, World1!!"
with app.test_request_context():
    print(url_for('hello_world', next="/"))
if __name__=="__main__":
    app.run(host="0.0.0.0")

