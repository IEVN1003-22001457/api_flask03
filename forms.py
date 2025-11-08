from wtforms import Form
from wtforms import StringField, FloatField, EmailField, PasswordField, IntegerField, RadioField
from wtforms import validators
from wtforms.validators import DataRequired

import datetime

class UserForm(Form):
    matricula = IntegerField("Matricula", 
                [validators.DataRequired(message="La matrícula es obligatoria")])
    
    nombre    = StringField('Nombre', 
                [validators.DataRequired(message="El campo es requerido")])
    
    apellido  = StringField('Apellido', 
                [validators.DataRequired(message="El campo es requerido")])
    
    edad = IntegerField('Edad',
                [validators.DataRequired(message="La edad es obligatoria")])


    email = EmailField('Email',
                [validators.Email(message="El campo es requerido")])

class FigurasForm(Form):
    tipofigura = StringField("Tipo de Figura", 
                [validators.DataRequired(message="El tipo de figura es obligatorio")])
    base = IntegerField("Base", 
                [validators.DataRequired(message="La matrícula es obligatoria")])
    altura = IntegerField("Altura", 
                [validators.DataRequired(message="La matrícula es obligatoria")])
    radio = IntegerField("Radio", 
                [validators.DataRequired(message="El radio es obligatorio")])
    apotema = IntegerField("Apotema", 
                [validators.DataRequired(message="El apotema es obligatorio")])
    lado = IntegerField("Lado", 
                [validators.DataRequired(message="El lado es obligatorio")])
    
class PizzasForm(Form):
    Nombre = StringField("Nombre", 
            [validators.DataRequired(message="El nombre es obligatorio")])
    Direccion = StringField("Dirección", 
            [validators.DataRequired(message="La dirección es obligatoria")])
    Telefono = StringField("Teléfono", 
            [validators.DataRequired(message="El teléfono es obligatorio")])

    Fecha = StringField("Fecha", 
            default=datetime.date.today().strftime('%Y-%m-%d'))

    NumPizzas = IntegerField("Numero de Pizzas", 
            [validators.Optional(), validators.NumberRange(min=1, message="Debe ser al menos 1")], 
            default=1)
