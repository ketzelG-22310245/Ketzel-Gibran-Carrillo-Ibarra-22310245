from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# ==== DATOS DEL JUEGO (Historias del PDF “Main plot (1).pdf”) ====

# Personajes (asesinos)
personajes = [
    "Bane",
    "El Acertijo",
    "Talon",
    "El Joker",
    "El Pingüino"
]

# Lugares
lugares = [
    "Mansión Wayne",
    "Arkham",
    "Cementerio de los Wayne",
    "Fábrica abandonada",
    "Corte de los Búhos"
]

# Armas
armas = [
    "Tubo de suero",
    "Bastón del Acertijo",
    "Pistola",
    "Tubo metálico",
    "Paraguas"
]

# ==== HISTORIAS ====
# 🔹 Aquí puedes editar, cambiar o agregar tus historias.
# Cada historia está definida por un asesino, un arma, un lugar y su narrativa.
historias = [
    {
        "asesino": "Bane",
        "arma": "Tubo de suero",
        "lugar": "Cementerio de los Wayne",
        "historia": "Los Robins fueron hallados colgados en la baticueva. Las pistas conducían al cementerio de los Wayne: rastros de sangre, pasos gigantes y un tubo de suero roto. Bane los asfixió con su propio sistema de fuerza antes de arrastrarlos a la cueva."
    },
    {
        "asesino": "El Acertijo",
        "arma": "Bastón del Acertijo",
        "lugar": "Mansión Wayne",
        "historia": "Alfred fue torturado hasta la muerte en la Mansión Wayne. El bastón del Acertijo, lleno de sangre, fue encontrado junto a su cuerpo. Las heridas y marcas de tortura confirmaron que fue un crimen planeado, no una pelea improvisada."
    },
    {
        "asesino": "Talon",
        "arma": "Pistola",
        "lugar": "Corte de los Búhos",
        "historia": "Barbara Gordon, Batgirl, fue encontrada en la baticueva. Tras investigar, Batman descubrió que Talon la enfrentó en la Corte de los Búhos. Le rompió la espalda y la remató con una pistola como advertencia a Batman."
    },
    {
        "asesino": "El Joker",
        "arma": "Tubo metálico",
        "lugar": "Fábrica abandonada",
        "historia": "Jason Todd fue hallado muerto, con pintura blanca y roja en el rostro. En la fábrica abandonada, Batman halló un tubo ensangrentado y cabellos de Jason. El Joker lo golpeó hasta la muerte y dejó su cuerpo como 'regalo' macabro."
    },
    {
        "asesino": "El Pingüino",
        "arma": "Paraguas",
        "lugar": "Arkham",
        "historia": "Jim Gordon fue encontrado colgado en la baticueva, con restos de un paraguas ensangrentado. En Arkham, Batman halló varios paraguas rotos sin munición. El Pingüino lo golpeó y asfixió durante una fuga de prisioneros."
    }
]

# Variable global del caso aleatorio actual
caso_actual = None


# ==== RUTAS ====

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/start')
def start():
    global caso_actual
    caso_actual = random.choice(historias)
    return render_template('juego.html', personajes=personajes, lugares=lugares, armas=armas)

@app.route('/resultado', methods=['POST'])
def resultado():
    global caso_actual
    asesino = request.form['asesino']
    arma = request.form['arma']
    lugar = request.form['lugar']

    if (asesino == caso_actual['asesino'] and
        arma == caso_actual['arma'] and
        lugar == caso_actual['lugar']):
        return render_template('resultado.html', correcto=True, historia=caso_actual['historia'])
    else:
        return render_template('resultado.html', correcto=False, historia=caso_actual['historia'])

@app.route('/creditos')
def creditos():
    return render_template('creditos.html')

@app.route('/exit')
def salir():
    return "Juego cerrado. Puedes cerrar esta pestaña."

if __name__ == '__main__':
    app.run(debug=True)