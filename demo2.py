from flask import Flask
web=Flask(__name__)

@web.route("/")
def first():
    return "<h1>first page</h1>"

@web.route("/contact")
def contact():
    return "<h2>Contact page</h2>"

if __name__=="__main__":
    web.run(debug=True)