import os
from flask import Flask 

# create an instance of the class Flask and storing it in a variable called app
# The first argument of the Flask class, is the name of the application's module - our package.
# Since we're just using a single module, we can use __name__ which is a built-in Python variable.
app = Flask(__name__)

# @ is a decorator, which is a function wrapper
# "/" Brings us to the root directory and returns hello world
@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__": #main is the default module in python
    app.run( #We run the app using these arguments
        host=os.environ.get("IP", "0.0.0.0"), #Looks for environment's IP, returns default if none
        port=int(os.environ.get("PORT", "5000")), #5000 is a commonly used port by flask
        debug=True  #Allows for easier debugging when developing
        # SET DEBUG TO FALSE FOR PRODUCTION/ ASSESSMENT SUBMISSION
        )
