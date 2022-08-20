# Importing flask
from flask import Flask

# Setup application referencing this file's name
app = Flask(__name__)

# Using the app route decorator to create an index route for the site so we don't immediately get a 404
# Pass in the url string of the route
# Each decorator needs to be followed by a function
@app.route('/')
def index():
    string = "Khakhras don't hold their own against peanut butter."
    
    return string

# Setting up the main function
if __name__ == '__main__':
    # Debugging true means that our errors pop up on the webpage
    app.run(debug=True)