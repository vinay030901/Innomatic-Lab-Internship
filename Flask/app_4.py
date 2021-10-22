from flask import Flask

app=Flask(__name__)

###################################################
# get and post request

@app.route('/')
def fun_1():
    return "this is a response from GET request"

@app.route('/',methods=['POST'])
def fun_2():
    return "this is a response from POST request"


#####################################################

if __name__ == '__main__':
    app.run(debug =True)