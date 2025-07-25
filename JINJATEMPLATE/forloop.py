from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('filters.html', users=[
        {"name":"Abc", "age": 35},
        {"name":"Def", "age": 24},
        {"name":"Ghi", "age": 56},
        {"name":"Jkl", "age": 18}
    ])

app.run(host='0.0.0.0',port=50100,debug=True)

