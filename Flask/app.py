from flask import Flask, request,render_template

app =Flask(__name__)

############################################

@app.route('/')
def home_get():
    return render_template('home.html')

@app.route('/',methods=['POST'])
def home_post():
    pass

@app.route('/history')
def history_get():
    return render_template('history.html')

############################################

if __name__ == '__main__':
    app.run()