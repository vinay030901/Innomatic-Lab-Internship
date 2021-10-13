# step -1 import
from flask import Flask

# step 2- object of flask class
app = Flask(__name__)

# step 3: define the routes and bind them to do some logic
##in google.com/search or google.com/about us
# google.com is domain while search and about us are routes
@app.route('/')# our first route
def func_1():# explain the route in function
    # now let's write the logic what will happen at the route
    return "Welcome to home page"# this is our response

@app.route('/about us')
def func_2():
    return "this is our about us page"

# step4: start the application
if __name__=="__main__":
    app.run()