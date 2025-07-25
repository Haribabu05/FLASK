from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',user={'name':'hari','age':15})

app.run(host='0.0.0.0',port=50100,debug=True)

