from logging import debug
from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import json

app = Flask(__name__)

contact_us="contact_us.db"

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/contact')
def cont():
    return render_template('contact.html')

@app.route('/signup', methods = ['POST'])
def signup():
    name = request.form['name']
    mail = request.form['email']
    print("The Name is "+ str(name),end="\n")
    print("And Email is "+ str(mail),end="\n")
    return redirect('/product')

@app.route('/product')
def products():
    img=["viyogi_notes.png","adi_image_logo.png","viyogi_notes.png","adi_image_logo.png","viyogi_notes.png","adi_image_logo.png","viyogi_notes.png","adi_image_logo.png"]
    product=["Viyogi Notes","Adi Images","Covid Data","Express-Calcy","Aditya Centre","V-Data Tool","seventh","eighth"]
    link=["http://www.google.com/","http://www.github.com/","#","#","#","#","#","#"]
    color=["255,138,101","255,202,40","102,187,106","41,182,246","240,98,146","159,168,218","60,150,85","197,225,165"]
    return render_template('product.html',products=product,links=link,colors=color,imgs=img ,len=len(img))

@app.route('/project')
def projects():
    return render_template('project.html')

@app.route('/skills')
def skill():
    return render_template('skills.html')

@app.route('/assessments')
def assess():
    return render_template('assessments.html')

if "__name__"=="__main__":
    app.run(debug=True)