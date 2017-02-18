from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/menu",methods=["GET"])
def menu():
    return render_template("index.html")
    
@app.route("/addclothing",methods=["GET"])
def cloth():
    return render_template("cloth.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
