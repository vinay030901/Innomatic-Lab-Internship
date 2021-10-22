# step -1 import
from flask import Flask

# step 2- object of flask class
app = Flask(__name__)

# data users
reg_users = ['vinay','champ','Innu','Bro']

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

@app.route('/user/Vinay')
def user_1():
    return "welcome Vinay"

@app.route('/user/<user_name>')# dynammic routing
def user_profile(user_name):
    if user_name in reg_users:
        return "welcome {}".format(user_name)
    else:
        return "user not found, kindly register"

# step4: start the application
if __name__=="__main__":
    app.run(debug=True)