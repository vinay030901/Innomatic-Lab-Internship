from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Home Page Vinay"

@app.route('/user/<user_name>')
def fun(user_name):
    return "good morning {}, welcome to this web page".format(user_name)
if __name__=="__main__":
    app.run(debug=True)