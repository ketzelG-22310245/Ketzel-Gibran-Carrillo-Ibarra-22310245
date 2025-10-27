#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, session, url_for
import json
import os
import time

app = Flask(__name__)
app.secret_key = "akinator-flask-secret-porfavorcámbialo"
ARCHIVO = "arbol_peliculas.json"

# ------------------ CARGAR / CREAR ÁRBOL INICIAL (TU ÁRBOL COMPLETO) ------------------
def cargar_arbol():
    if not os.path.exists(ARCHIVO) or os.stat(ARCHIVO).st_size == 0:
        arbol_inicial = {
            "pregunta": "¿Tu película es de acción?",
            "si": {
                "pregunta": "¿Tu película es de superhéroes?",
                "si": {
                    "pregunta": "¿Tu película es de DC?",
                    "si": {"pelicula": "Superman"},
                    "no": {
                        "pregunta": "¿Tu película es de Marvel?",
                        "si": {"pelicula": "Iron Man"},
                        "no": {"aprende": True}
                    }
                },
                "no": {
                    "pregunta": "¿Tu película es de automóviles?",
                    "si": {"pelicula": "Rápidos y Furiosos"},
                    "no": {"aprende": True}
                }
            },
            "no": {
                "pregunta": "¿Tu película es de comedia?",
                "si": {
                    "pregunta": "¿Tu película es de comedia romántica?",
                    "si": {"pelicula": "Anyone but You"},
                    "no": {
                        "pregunta": "¿Tu película es de Adam Sandler?",
                        "si": {"pelicula": "Son como niños"},
                        "no": {
                            "pregunta": "¿Tu película tiene un protagonista mudo?",
                            "si": {"pelicula": "Mr. Bean"},
                            "no": {"aprende": True}
                        }
                    }
                },
                "no": {
                    "pregunta": "¿Tu película es de romance?",
                    "si": {
                        "pregunta": "¿Tu película ocurre en un barco?",
                        "si": {"pelicula": "Titanic"},
                        "no": {
                            "pregunta": "¿Tu película es sobre un científico?",
                            "si": {"pelicula": "La teoría del todo"},
                            "no": {
                                "pregunta": "¿Tu película es un romance triste?",
                                "si": {"pelicula": "Bajo la misma estrella"},
                                "no": {"aprende": True}
                            }
                        }
                    },
                    "no": {
                        "pregunta": "¿Tu película es un musical?",
                        "si": {
                            "pregunta": "¿Tu película es sobre jazz?",
                            "si": {"pelicula": "La La Land"},
                            "no": {
                                "pregunta": "¿Tu película es sobre un circo?",
                                "si": {"pelicula": "The Greatest Showman"},
                                "no": {
                                    "pregunta": "¿Tu película es sobre un artista?",
                                    "si": {"pelicula": "Rocketman"},
                                    "no": {"aprende": True}
                                }
                            }
                        },
                        "no": {
                            "pregunta": "¿Tu película es de ciencia ficción?",
                            "si": {
                                "pregunta": "¿Tu película tiene sables láser?",
                                "si": {"pelicula": "Star Wars: A New Hope"},
                                "no": {
                                    "pregunta": "¿Tu película tiene gusanos gigantes?",
                                    "si": {"pelicula": "Dune"},
                                    "no": {
                                        "pregunta": "¿Tu película es cyberpunk?",
                                        "si": {"pelicula": "Akira"},
                                        "no": {"aprende": True}
                                    }
                                }
                            },
                            "no": {"aprende": True}
                        }
                    }
                }
            }
        }
        guardar_arbol(arbol_inicial)
        return arbol_inicial

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return json.load(f)


# ------------------ GUARDAR ------------------
def guardar_arbol(arbol):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(arbol, f, ensure_ascii=False, indent=4)


# ------------------ UTILIDAD: OBTENER NODO ACTUAL SEGÚN EL CAMINO ------------------
def obtener_nodo_actual(arbol, camino):
    nodo = arbol
    for r in camino:
        # r debe ser "si" o "no"
        nodo = nodo.get(r, {})
    return nodo


# ------------------ RUTAS FLASK ------------------
@app.route("/")
def index():
    # iniciar/reiniciar la sesión de juego
    session["camino"] = []
    return render_template("index.html")


@app.route("/jugar", methods=["GET"])
def jugar():
    arbol = cargar_arbol()
    camino = session.get("camino", [])
    nodo = obtener_nodo_actual(arbol, camino)

    # Si nodo indica aprender (aprende: True)
    if nodo.get("aprende", False):
        # mostrar formulario para aprender
        # Si el nodo no tiene 'pelicula', lo tratamos como nuevo aprendizaje
        pelicula_antigua = nodo.get("pelicula", None)
        return render_template("aprende.html", pelicula_antigua=pelicula_antigua)

    # Si nodo propone una película candidata
    if "pelicula" in nodo:
        return render_template("jugar.html", pregunta=None, pelicula=nodo["pelicula"])

    # Si es una pregunta
    if "pregunta" in nodo:
        return render_template("jugar.html", pregunta=nodo["pregunta"], pelicula=None)

    # Si algo no encaja, reiniciamos sesión y mostramos mensaje de error suave
    session["camino"] = []
    return render_template("final.html", mensaje="Nodo inválido en el árbol. Reinicié la partida.")


@app.route("/respuesta", methods=["POST"])
def respuesta():
    # recibir 'si' o 'no' desde el formulario
    r = request.form.get("respuesta")
    if r not in ("si", "no"):
        # invalid input -> redirigir a jugar
        return redirect(url_for("jugar"))

    camino = session.get("camino", [])
    camino.append(r)
    session["camino"] = camino
    return redirect(url_for("jugar"))


@app.route("/adivino", methods=["POST"])
def adivino():
    # Cuando el sistema propone una película y el usuario responde si/no
    correcto = request.form.get("correcto")
    if correcto == "si":
        # Adivinó
        # limpiar camino para nueva partida si el usuario vuelve
        session["camino"] = []
        return render_template("final.html", acierto=True)
    else:
        # no adivinó -> ir a aprender
        return render_template("aprende.html", pelicula_antigua=None)


@app.route("/aprender", methods=["POST"])
def aprender():
    """
    Este endpoint procesa el formulario de aprendizaje enviado desde aprende.html.
    Mantiene la misma lógica que tu función 'aprender' de la versión consola,
    adaptada para tomar datos del formulario y actualizar el nodo correspondiente en el árbol.
    """
    arbol = cargar_arbol()
    camino = session.get("camino", [])
    nodo = obtener_nodo_actual(arbol, camino)

    # Datos del formulario
    pelicula_correcta = request.form.get("pelicula", "").strip()
    pregunta_nueva = request.form.get("pregunta", "").strip()
    respuesta_correcta = request.form.get("respuesta", "").strip()  # "si" o "no"

    # Validaciones básicas
    if not pelicula_correcta or not pregunta_nueva or respuesta_correcta not in ("si", "no"):
        # volver a la pantalla aprender con mensaje (opcional)
        return render_template("aprende.html", error="Rellena todos los campos correctamente.", pelicula_antigua=nodo.get("pelicula"))

    pelicula_antigua = nodo.get("pelicula", None)

    # Construcción del nuevo sub-árbol según la respuesta (igual que tu lógica consola)
    if respuesta_correcta == "si":
        nuevo = {
            "pregunta": pregunta_nueva,
            "si": {"pelicula": pelicula_correcta},
            "no": {"pelicula": pelicula_antigua} if pelicula_antigua else {"aprende": True}
        }
    else:
        nuevo = {
            "pregunta": pregunta_nueva,
            "si": {"pelicula": pelicula_antigua} if pelicula_antigua else {"aprende": True},
            "no": {"pelicula": pelicula_correcta}
        }

    # Reemplazamos el contenido del nodo en el árbol por el nuevo sub-árbol
    nodo.clear()
    nodo.update(nuevo)

    # Guardar árbol actualizado
    guardar_arbol(arbol)

    # limpiar camino para nueva partida
    session["camino"] = []

    # mostrar pantalla final indicando que aprendió
    return render_template("final.html", acierto=False, pelicula=pelicula_correcta)


# Ruta opcional para reiniciar manualmente el árbol (útil en desarrollo)
@app.route("/_reset_tree", methods=["POST"])
def reset_tree():
    if os.path.exists(ARCHIVO):
        os.remove(ARCHIVO)
    cargar_arbol()
    session["camino"] = []
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)