import os
import json
from flask import Flask, render_template

# create an instance of the class Flask and storing it in a variable called app
# The first argument of the Flask class, is the name of the application's
# module - our package.
# Since we're just using a single module, we can use __name__ which is a
# built-in Python variable.
app = Flask(__name__)


# @ is a decorator, which is a function wrapper
# "/" Brings us to the root directory and returns what is in the index function
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    # The line below opens company.json as read only and assigns the contents
    # to a variable called json_data
    with open("data/company.json", "r") as json_data:
        # Set data to the data in json_data
        data = json.load(json_data)
    # return render_template("about.html", page_title="About",
    # list_of_numbers=[1,2,3]) - this was to illustrate our for loop
    # We want our list returned to us, and we called it company, to send to
    # the html template with the data
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":     # main is the default module in python
    app.run(               # We run the app using these arguments
        host=os.environ.get("IP", "0.0.0.0"),
        # ^ Looks for environment's IP, returns default if none
        port=int(os.environ.get("PORT", "5000")),
        # ^ 5000 is a commonly used port by flask
        debug=True     # Allows for easier debugging when developing
        # SET DEBUG TO FALSE FOR PRODUCTION/ ASSESSMENT SUBMISSION
        )
