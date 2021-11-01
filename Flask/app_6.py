from flask import Flask,render_template,request
app=Flask(__name__)

##########################################################

@app.route('/') # decorator concept in python
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET','POST'])
def user():
    if request.method == 'POST':
        name=request.form.get('in_1')# we use get function for try and accept, so if we don't have the available value for in_1, then
        # it would not get terminated. It will return null instead of abnormally terminating the code
        return "Thanks {}! for registering".format(name)
        # return "Thanks {}! for registering".format(request.form['in_1'])
    return "this is about us page"


##########################################################
if __name__ == '__main__':
    app.run(debug =True)