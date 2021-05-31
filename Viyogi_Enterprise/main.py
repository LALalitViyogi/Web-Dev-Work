from logging import debug
from flask import Flask,render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/contact')
def cont():
    return render_template('contact.html')

@app.route('/signup', methods = ['POST'])
def signup():
    name = request.form['name']
    print("The email address is '" + name + "'")
    return redirect('/')

@app.route('/product')
def products():
    return render_template('product.html')

@app.route('/project')
def projects():
    return render_template('project.html')

if "__name__"=="__main__":
    app.run(debug=True)