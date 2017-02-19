from flask import Flask, redirect, render_template, request, url_for, session

from data import DatabaseManager
dbm = DatabaseManager.create_users()

dbm.register_user("pacqqu@gmail.com","Justin Pacquing","password")

app = Flask(__name__)
app.secret_key = 'w0we33'

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
        return redirect('/dashboard')
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
    return render_template("index.html")
    
@app.route("/addclothing",methods=["GET"])
def cloth():
    return render_template("cloth.html")

@app.route('/logoff')
def logoff():
    if session.get('user', None):
        session['user'] = 0
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
