from flask import Flask
app = Flask(__name__)

@app.route('/')
def fun():
    return "Hello World"

@app.route('/products')
def products():
    return "this is the product page"
if __name__=='__main__':
    app.run(debug  = True)