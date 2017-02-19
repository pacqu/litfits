import json, jinja2, time, os
from flask import Flask, redirect, render_template, request, url_for, session

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/images/uploads')

from data import DatabaseManager
dbm = DatabaseManager.create()

dbm.register_user("pacqqu@gmail.com","Justin Pacquing","password")

app = Flask(__name__)
app.secret_key = 'w0we33'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=["GET","POST"])
def home():
    if session.get('user', None):
        return redirect('/menu')
    if request.method == "POST":
        sub = request.form['submit']
        if sub == "register":
            return redirect('/register')
        elif sub == "login":
            return redirect('/login')
    else:
        return render_template("home.html")

@app.route('/register', methods=["GET","POST"])
def register():
    if session.get('user', None):
        return redirect('/menu')
    if request.method == "POST":
        fullname = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['confirmPassword']
        if  password == cpassword:
            if dbm.register_user(email, fullname, password):
                session['user']=email
                return redirect('/menu')
            else:
                return redirect('/register')
        else:
            return render_template("register.html")
    else:
        return render_template("register.html")

@app.route('/login', methods=["GET","POST"])  
def login():
    if session.get('user', None):
        return redirect('/menu')
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        if dbm.is_user_authorized(email,password):
            session['user'] = email
            return redirect(url_for('menu'))
        else:
            return render_template("login.html")
    else:
      return render_template("login.html")


@app.route("/menu",methods=["GET"])
def menu():
    if session.get('user', None):
         return render_template("index.html")
    else:
        return redirect('/')
    
@app.route("/addclothing",methods=["GET"])
def cloth():
    if session.get('user', None):
        return render_template("choosecat.html")
    else:
        return redirect('/')
    

@app.route("/addtop",methods=["GET","POST"])
def top():
    if session.get('user', None):
        if request.method == "POST":
            email = session['user']
            name = request.form['name']
            clothpic = request.files['photo']
            category = 'Top'
            subcategory = request.form['TopKind']
            dbm.register_cloth(name, email, category, subcategory)
            test = dbm.fetch_all_clothes()
            print test
            clothpic.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
            redir = '/clothpage/' + name
            return redirect(redir)
        else:
            return render_template("addtop.html")
    else:
        return redirect('/')

@app.route("/addbot",methods=["GET","POST"])
def bot():
    if session.get('user', None):
        if request.method == "POST":
            email = session['user']
            name = request.form['name']
            clothpic = request.files['photo']
            category = 'Bottom'
            subcategory = request.form['BotKind']
            dbm.register_cloth(name, email, category, subcategory)
            #test = dbm.fetch_all_clothes()
            #print test
            clothpic.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
            redir = '/clothpage/' + name
            return redirect(redir)
        else:
            return render_template("addbot.html")
    else:
        return redirect('/')
        

@app.route("/addother",methods=["GET","POST"])
def other():
    if session.get('user', None):
        if request.method == "POST":
            email = session['user']
            name = request.form['name']
            clothpic = request.files['photo']
            category = 'Other'
            subcategory = request.form['OtherKind']
            dbm.register_cloth(name, email, category, subcategory)
            #test = dbm.fetch_all_clothes()
            #print test
            clothpic.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
            redir = '/clothpage/' + name
            return redirect(redir)
        else:
            return render_template("addother.html")
    else:
        return redirect('/')

@app.route("/clothpage/<cloth>", methods=["GET"])
def clothpage(cloth=""):
    if session.get('user', None):
        return render_template("clothpage.html",cloth = cloth)
    else:
        return redirect('/')

@app.route("/closet", methods=["GET"])
def closet():
    if session.get('user', None):
        return render_template("closet.html")
    else:
        return redirect('/')
    
@app.route('/logoff', methods=["GET"])
def logoff():
    if session.get('user', None):
        session['user'] = 0
    return redirect('/')

@app.route('/getcloth/<cloth>', methods=["GET"])
def getcloth(cloth=""):
    piece = dbm.get_cloth(cloth)
    return json.JSONEncoder().encode(piece)

@app.route('/getcloset')
def getcloset():
    u = session['user']
    closet = dbm.get_closet(u)
    return json.JSONEncoder().encode(closet)
    

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
