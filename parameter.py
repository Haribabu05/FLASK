from flask import Flask,render_template,request

#create an instance of an web server
parameters = Flask(__name__)

#localhost:50100/search?uname=abcd&city=xyz
@parameters.route('/search')
def home():
    #requesting arguments(parameters) from the parameters then storing it in dictioninary
    q=request.args.to_dict()
    #return a particular variable
    return "Hello {0}".format(q.get("name"))

parameters.run(host='0.0.0.0',port=50100,debug=True)

