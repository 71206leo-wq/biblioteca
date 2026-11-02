import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', titulo='Home', mensaje='Bienvenido a la página de inicio de la biblioteca')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html', titulo='Servicios', mensaje='Estos son nuestros servicios')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contactos', mensaje='Aqui esta nuestra info de contacto')


@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html', titulo='Catálogo', mensaje='Bienvenido al catálogo de la biblioteca')


@app.route('/img/<path:filename>')
def imagen(filename):
    return send_from_directory(os.path.join(app.root_path, 'img'), filename)


if __name__ == '__main__':
    app.run(debug=True, port = 8000)
    