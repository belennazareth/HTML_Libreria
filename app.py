from flask import Flask, render_template, abort, redirect
import os

from functions import checkLibrary
app = Flask(__name__)

books = checkLibrary()	

@app.route('/')
def inicio():
    return render_template("biblioteca.html",books=books)

@app.route('/biblioteca')
def biblioteca():
    return render_template("biblioteca.html", books=books)

@app.route('/error')
def error():
    return abort(404)

@app.route('/libro/<isbn>')
def libro(isbn):
    try:
        return render_template("libro.html",isbn=isbn,books=books)
    except:
        return abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
    return render_template("categoria.html", categoria=categoria, books=books)

@app.route('/contacto')
def contacto():
    return render_template("contacto.html")


#app.run("0.0.0.0",5000,debug=True)
port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)