from flask import Flask, flash, render_template, request,redirect,url_for,session
import sqlite3

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("base.html")
    
@app.route('/register', methods=['POST','GET'])
def register_page():
    return render_template("register.html")

@app.route('/login', methods=['GET','POST'])
def login_page():
        return render_template("login.html")

@app.route('/dashboard', methods=["GET","POST"])
def dashbord():
    return render_template("dashbord.html")

@app.route('/about')
def about_page():
    return render_template("about.html")

@app.route('/Get your job')
def get_page():
    return render_template("job lisiting.html")



@app.route('/home')
def login():
    return render_template("home.html")
        
if __name__ == "main":
    app.run(debug=True)