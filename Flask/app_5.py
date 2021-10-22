from flask import Flask,request

app=Flask(__name__)

###################################################
# get and post request


@app.route('/',methods=['POST','GET'])
#def fun_2():
#   return "this is a response from POST request"
def fun_2():
    if request.method =="POST":
        return "this is a response from POST request"
    return "this is a response from GET request"

#####################################################

if __name__ == '__main__':
    app.run(debug =True)