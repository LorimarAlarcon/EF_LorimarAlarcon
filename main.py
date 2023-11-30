from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros_pintura = int(request.form['tarros_pintura'])

        precio_tarro = 9000
        total_sin_descuento = tarros_pintura * precio_tarro

        if 18 <= edad < 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - total_descuento

        return render_template('ejercicio1.html', nombre=nombre, edad=edad, total_sin_descuento=total_sin_descuento,
                               total_descuento=total_descuento, total_con_descuento=total_con_descuento)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        usuarios = {'juan': 'admin', 'pepe': 'user'}

        if usuario in usuarios and usuarios[usuario] == contraseña:
            mensaje = f"Bienvenido {'Administrador' if usuario == 'juan' else 'Usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', usuario=usuario, mensaje=mensaje)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)












