import json
from flask import Flask, render_template, request, flash
import flask
from numpy import imag, indices

from controllers import images



app = Flask(__name__)

@app.route('/home')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/principal')
def principal():
    persona = images.get_data()
    imagen = persona['URL'].tolist()
    id = persona['ID'].tolist()
    return render_template('principal.html', personas = imagen,ids = id)

@app.route('/calificacion')
def calificacion():
    persona = images.get_data()
    imagen = persona['URL'].tolist()
    id = persona['ID'].tolist()
    Afro = persona['Afro-American_percentage'].tolist()
    Europa = persona['European_percentage'].tolist()
    Indigena = persona['Indigenous_percentage'].tolist()
    return render_template('calificacion.html', personas = imagen,ids = id, A=Afro, E=Europa, I=Indigena)

@app.route('/guardar')
def guardar():
    datos = images.get_registro().to_json()
    return render_template('guardar.html', tabla = datos)

@app.route('/guardar/<string:userinfo>',methods=['POST'])
def redireccion(userinfo):
    info = json.loads(userinfo)
    images.guardar_datos(info)
    return('/guardar')
    

if __name__ == '__main__':
    app.run(debug=True)