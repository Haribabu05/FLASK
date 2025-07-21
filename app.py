from flask import Flask,render_template

#create an instance of an web server
app = Flask(__name__)

#creating an endpoint
@app.route('/')
def home():
    return "Hello World!!!"

@app.route('/hi')
def hi():
    return render_template("base.html",user={"name":"hari","id":"3456"})

app.run(host='0.0.0.0',port=50100,debug=True)

