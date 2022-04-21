from flask import Flask, render_template, abort, redirect
app = Flask(__name__)	

@app.route('/')
def inicio():
    return render_template("biblioteca.html")

@app.route('/biblioteca')
def biblioteca():
    return render_template("biblioteca.html")

@app.route('/categorias')
def categorias():
    return render_template("categorias.html")

@app.route('/error')
def error():
    return abort(404)

@app.route('/contacto')
def contacto():
    return redirect("/contacto")


app.run("0.0.0.0",5000,debug=True)