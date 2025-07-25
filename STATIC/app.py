from flask import Flask,render_template,send_from_directory

#static_folder= (used to retrieve data from folder if its not called static)
#static_url_path = (to display in the url as its retrived from static folder but actually its retrived from reports)

app=Flask(__name__,static_folder='reports',static_url_path="/static")

@app.route('/')
def home():
    return render_template("base.html")

#getting the path for from the url 

@app.route("/reports/<path:inputPath>")
def getPath(inputPath):
    return send_from_directory("reports",inputPath)


app.run(host="0.0.0.0",port=5000,debug=True)