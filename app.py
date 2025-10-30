from flask import Flask, render_template, request

import forms

app=Flask(__name__)
 
@app.route('/')
def home():
    return "Hello, World"


@app.route('/Alumnos', methods=['GET','POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.email.data
    return render_template('Alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em)

@app.route('/figuras', methods=['GET','POST'])
def figuras():
    base=0
    altura=0
    apotema=0
    lado=0
    radio=0
    res=0
    tipofigura=""

    figuras_clase=forms.FigurasForm(request.form)

    if request.method=='POST':
        tipofigura = request.form.get('tipofigura')

        if tipofigura=="triangulo":
                base=figuras_clase.base.data
                altura=figuras_clase.altura.data
                res = (base*altura)/2

        if tipofigura=="rectangulo":
                base=figuras_clase.base.data
                altura=figuras_clase.altura.data
                res = base*altura

        if tipofigura=="circulo":
                radio=figuras_clase.radio.data
                res = 3.1416*radio*radio

        if tipofigura=="pentagono":
                lado=figuras_clase.lado.data
                apotema=figuras_clase.apotema.data
                res = lado*5*apotema/2
    
    
    return render_template('figuras.html', form=figuras_clase, tipofigura=tipofigura, res=res, base=base, altura=altura, apotema=apotema, lado=lado, radio=radio)
    
 
@app.route('/index')
def index():

    titulo="IEVN1003 - PWA"
    listado=["Opera 1", "Opera 2", "Opera 3", "Opera 4"]

    return render_template("index.html", titulo=titulo, listado=listado)
 
@app.route('/operas', methods=['GET','POST'])
def operas():
    resultado = 0
    if request.method=='POST':
        x1 = request.form.get('n1')
        x2 = request.form.get('n2')
        resultado = x1+x2
    return render_template('operas.html', resultado=resultado)


@app.route('/distancia')
def distancia():
    return render_template('distancia.html')
 

@app.route('/about')
def about():
    return "<h1>This is the about page.<h>"
 

@app.route("/user/<string:user>")
def user(user):
    return "Hola"+ user
 

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero {}".format(n)
 

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return "ID {} nombre: {}",format(id,username)
 

@app.route("/suma/<float:n1>/<float:n2>")
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)
 
 
@app.route("/prueba")
def prueba():
    return '''
    <h1>Prueba de HTML</h1>
<p>Esto es un parrafo</p>
<ul>
    <li>Elemento 1</li>
    <li>Elemento 2</li>
    <li>Elemento 3</li>
</ul>
'''
 
if __name__ == '__main__':
    app.run(debug=True)