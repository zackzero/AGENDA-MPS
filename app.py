from flask import Flask, render_template, request, flash, redirect
import sqlite3
import os


app = Flask(__name__)
app.config['SECRET_KEY']= "SECRETA"
@app.route("/")
def home():
    return render_template("/login.html")

@app.route("/cadastrar")
def cadastrar():
    return render_template("/register.html")

@app.route("/register", methods=['POST','GET'])
def register():
    con=sqlite3.connect('usuarios.db')
    c=con.cursor()
    if request.method=='POST':
        if(request.form["name"]!="" and request.form["passWord"]!=""):
            name=request.form["name"]
            passWord=request.form["passWord"]
            statement=f"SELECT * from pessoas WHERE nome='{name}' AND senha='{passWord}';"
            c.execute(statement)
            data=c.fetchone()
            if data:
                return render_template("error.html")
            else:
                if not data:
                    c.execute("INSERT INTO pessoas (nome,senha) VALUES (?,?)",(name,passWord))
                    con.commit()
                    con.close()
                return render_template('login.html')
            
    elif request.method=='GET':
        return render_template('register.html')
                
                
@app.route("/login", methods=['POST','GET'])
def login():
    if request.method=='POST':
        name =request.form['name']
        passWord=request.form['passWord']
        con=sqlite3.connect('usuarios.db')
        c=con.cursor()
        statement=f"SELECT * from pessoas WHERE nome='{name}' AND senha='{passWord}';"
        c.execute(statement)
        if not c.fetchone():
            return render_template('login.html')
        else:
            return render_template('acesso.html')
    
    else:
        request.method =='GET'
        return render_template('login.html')
                
        

if __name__ in '__main__':
    app.run(debug=True)