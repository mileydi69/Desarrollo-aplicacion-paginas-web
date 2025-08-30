from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal que renderiza el inicio
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'Hola, {nombre}!'

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/contacto')
def contact():
    return 'Contactame en mi correo:'
    return render_template('contact.html')

# Ruta para mostrar el formulario
@app.route('/form')
def show_form():
    return render_template('form.html')


# Ruta para procesar los datos del formulario
@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    nombre = request.form.get('nombre')
    
    return render_template('result.html', nombre_recibido=nombre) 

if __name__ == '__main__':
    app.run(debug=True)