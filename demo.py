from flask import *
app=Flask(__name__)  #current file demo.py

@app.route("/")      #this is / route
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/gallary")
def gallary():
    return "Our Collection"

if __name__=="__main__":      #main file
    app.run(debug=True,port=4000)