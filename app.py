from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
