# Q1. Explain GET and POST methods.
# Ans.
#     GET and POST are HTTP methods used to send data from a client (such as a web browser) to a server.
# GET
#     It is used to request data from a server in the form of a URL query string.
#     The data sent using GET method is visible in the URL, and can be bookmarked 
#     or shared easily.
#     GET requests are usually used for retrieving data such as web pages, images, 
#     or other resources.

# POST
#     It is used to send data that is not visible in the URL, such as form data.
#     The data sent using POST method is not visible in the URL, and is sent as a 
#     message body with the request.
#     POST requests are usually used for submitting data such as login credentials, 
#     comments, or other form data.

# Q2. Why is request used in Flask?
# Ans.
#     In Flask, the request object is used to access the data submitted in an HTTP 
#     request. When a user sends a request to a Flask application, the request 
#     object is automatically created and populated with information about the 
#     request, such as the HTTP method used (e.g., GET or POST), the request 
#     headers, and any data submitted with the request.

# Q3. Why is redirect() used in Flask?
# Ans.
#     In Flask, the redirect() function is used to redirect the user to a different 
#     URL. This is commonly used in web applications to redirect the user after 
#     a successful form submission, to a login page after they logout, or to a 
#     different page based on certain conditions.

# Ex:
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # redirect the user to the 'hello' page
    return redirect(url_for('hello'))

@app.route('/hello')
def hello():
    return 'Hello, World!'

# Q4. What are templates in Flask? Why is the render_template() function used?
# Ans.
#     In Flask, templates are used to separate the presentation layer of a web 
#     application from the business logic layer. Templates are files that contain 
#     HTML, CSS, and JavaScript code that define the structure and layout of a web 
#     page. Flask uses a templating engine called Jinja2, which allows for dynamic 
#     content to be rendered in templates.

#     The render_template() function is used to render templates in Flask. It takes 
#     the name of the template file as an argument and returns the rendered HTML. 
#     The function searches for the template file in the templates folder of the 
#     Flask application by default.

# Q5. Create a simple API. Use Postman to test it. Attach the screenshot of the 
#     output in the Jupyter Notebook.
# Ans.
from flask import Flask, request ,render_template , jsonify

app = Flask(__name__)

@app.route('/', requests=["GET"])
def get_details():
    name = request.args.get('y')
    print(name)
    result = f'Hi this is {name}'
    return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")

#Output screenshot is at below location:
https://github.com/FUZZZZI/MasterDS/blob/main/Assignment_20Feb_Flask2/Feb20%20Solution%20Pic.jpg