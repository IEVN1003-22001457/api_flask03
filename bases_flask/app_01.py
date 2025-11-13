from flask import Flask, render_template, request

from flask import make_response, jsonify
import json

import datetime

import bases_flask.forms as forms

app=Flask(__name__)
 
@app.route('/')
def home():
    return "Hello, World"


@app.route('/pizza', methods=['GET','POST'])
def pizza():
    mostrarVen = False
# ---------------------------------------- Cargado del formulario y cookies
    form = forms.PizzasForm(request.form)
 
    pedido_actual_str = request.cookies.get('pedido_actual', '[]')
    pedido_actual = json.loads(pedido_actual_str)
   
    ventas_str = request.cookies.get('ventas_dia', '[]')
    ventas = json.loads(ventas_str)
 
   
    ventasAgrupadas = {}
    total_dia = 0
    for venta in ventas:
        nombre = venta.get('nombre')
        total = venta.get('total')
        total_dia += total
        ventasAgrupadas[nombre] = ventasAgrupadas.get(nombre, 0) + total
   
# ---------------------------------------- Formulario
    if request.method == 'POST':
     
        action = request.form.get("action")
 
        if action == 'agregar':
            precios_tamanio = {'chica': 40, 'mediana': 80, 'grande': 120}
           
            tamanio = request.form.get('Tamanio')
            ingredientesLista = request.form.getlist('Ingredientes')
            num_pizzas = form.NumPizzas.data
           
            if tamanio and num_pizzas:
                costTmnio = precios_tamanio.get(tamanio)
                costIngre = len(ingredientesLista) * 10
                subtotal = (costTmnio + costIngre) * num_pizzas
                pizzaOrdenada = {"tamanio": tamanio, "ingredientes": ingredientesLista, "num_pizzas": num_pizzas, "subtotal": subtotal}
                pedido_actual.append(pizzaOrdenada)
 
        elif action == 'terminar':
            total_pedido = 0
            for item in pedido_actual:
                total_pedido += item.get('subtotal')
            newVenta = {"nombre": form.Nombre.data, "direccion": form.Direccion.data, "telefono": form.Telefono.data, "fecha": form.Fecha.data, "total": total_pedido}
            ventas.append(newVenta)
 
            ventasAgrupadas = {}
            total_dia = 0
            for venta in ventas:
                nombre = venta.get('nombre')
                total = venta.get('total')
                total_dia += total
                ventasAgrupadas[nombre] = ventasAgrupadas.get(nombre, 0) + total
           
            pedido_actual = []
            form = forms.PizzasForm()
 
        elif action == 'quitar_ultimo':
            if pedido_actual:
                pedido_actual.pop()

        elif action == 'mostrarVen':
            mostrarVen = True
            
        elif action == 'borrarVen':
            ventas = []
            ventasAgrupadas = {}
            total_dia = 0
            mostrarVen = False
   
    response = make_response(render_template('pizza.html', form=form, pedido=pedido_actual, ventas_agrupadas=ventasAgrupadas, total_dia=total_dia, mostrarVen=mostrarVen))
   
    response.set_cookie('pedido_actual', json.dumps(pedido_actual))
    response.set_cookie('ventas_dia', json.dumps(ventas))

    return response
    

@app.route('/Alumnos', methods=['GET','POST'])
def alumnos():
    mat=0
    nom=""
    ape=""
    em=""
    estudiantes=[]
    datos={}
    tem=[]

    alumnos_clase=forms.UserForm(request.form)
    if request.method=='POST' and alumnos_clase.validate():
        mat=alumnos_clase.matricula.data
        nom=alumnos_clase.nombre.data
        ape=alumnos_clase.apellido.data
        em=alumnos_clase.email.data
        datos={'matricula':mat, 'nombre':nom, 'apellido':ape, 'email':em}

        datos_str = request.cookies.get('estudiante')
        if not datos_str:
         return "No hay cookie"
        tem = json.loads(datos_str)
        estudiantes = tem
        estudiantes.append(datos)

    response = make_response( render_template('Alumnos.html', form=alumnos_clase, mat=mat, nom=nom, ape=ape, em=em))

    response.set_cookie('estudiante', json.dumps(estudiantes))

    return response

@app.route('/get_cookie')
def get_cookie():
     datos_str = request.cookies.get('estudiante')
     if not datos_str:
         return "No hay cookie"
     datos = json.loads(datos_str)
     return jsonify(datos)

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