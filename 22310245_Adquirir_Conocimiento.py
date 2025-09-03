import tkinter as tk
from tkinter import simpledialog
import json
import os

# -------------------------------
# 1. Base de conocimiento
# -------------------------------

BASE_DATOS = "conocimiento.json"

# Cargar conocimiento si existe, si no crear base inicial
if os.path.exists(BASE_DATOS):
    with open(BASE_DATOS, "r") as f:
        base_conocimiento = json.load(f)
else:
    base_conocimiento = {
        "hola": "¡Hola! ¿Cómo estás?",
        "como estas": "Estoy bien, gracias. ¿Y tú?",
        "de que te gustaria hablar": "Podemos hablar de lo que quieras: tecnología, música, películas..."
    }

def guardar_base():
    with open(BASE_DATOS, "w") as f:
        json.dump(base_conocimiento, f, indent=4)

# -------------------------------
# 2. Función para mostrar mensajes en burbujas
# -------------------------------

def mostrar_mensaje(texto, remitente="bot"):
    """
    Crea una burbuja de mensaje (usuario o bot) y la añade al chat.
    """
    frame_msg = tk.Frame(chat_frame, bg="#f0f0f0")

    if remitente == "usuario":
        burbuja = tk.Label(frame_msg, text=texto, bg="#DCF8C6",  # Verde claro tipo WhatsApp
                           font=("Arial", 10), wraplength=300, justify="left",
                           anchor="e", padx=10, pady=5, bd=1, relief="solid")
        burbuja.pack(anchor="e", padx=5, pady=2)  # A la derecha
    else:
        burbuja = tk.Label(frame_msg, text=texto, bg="#E6E6E6",  # Gris claro para el bot
                           font=("Arial", 10), wraplength=300, justify="left",
                           anchor="w", padx=10, pady=5, bd=1, relief="solid")
        burbuja.pack(anchor="w", padx=5, pady=2)  # A la izquierda

    frame_msg.pack(fill="x", anchor="w", pady=2)
    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1.0)  # Scroll automático al final

# -------------------------------
# 3. Función principal del chatbot
# -------------------------------

def enviar():
    entrada = entrada_usuario.get().strip().lower()  # Texto del usuario
    if not entrada:
        return

    mostrar_mensaje("Tú: " + entrada, "usuario")
    entrada_usuario.set("")  # limpiar entrada

    if entrada in base_conocimiento:
        respuesta = base_conocimiento[entrada]
        mostrar_mensaje("Bot: " + respuesta, "bot")
    else:
        mostrar_mensaje("Bot: No sé qué responder a eso.", "bot")
        nueva_respuesta = simpledialog.askstring("Aprender", f"👉 ¿Qué debería contestar cuando digan '{entrada}'?")

        if nueva_respuesta:
            base_conocimiento[entrada] = nueva_respuesta
            guardar_base()
            mostrar_mensaje("Bot: Gracias, lo recordaré para la próxima.", "bot")

# -------------------------------
# 4. Interfaz gráfica con Tkinter
# -------------------------------

ventana = tk.Tk()
ventana.title("ChatBot estilo WhatsApp")
ventana.geometry("500x500")
ventana.configure(bg="#f0f0f0")

# Contenedor con scroll
chat_canvas = tk.Canvas(ventana, bg="#f0f0f0")
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=chat_canvas.yview)
chat_frame = tk.Frame(chat_canvas, bg="#f0f0f0")

# Configurar scroll
chat_frame.bind("<Configure>", lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all")))
chat_canvas.create_window((0, 0), window=chat_frame, anchor="nw")
chat_canvas.configure(yscrollcommand=scrollbar.set)

chat_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Entrada de texto
entrada_usuario = tk.StringVar()
entrada_entry = tk.Entry(ventana, textvariable=entrada_usuario, font=("Arial", 12))
entrada_entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

# Botón enviar
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)
boton_enviar.pack(side=tk.RIGHT, padx=10, pady=10)

# Enviar con Enter
ventana.bind("<Return>", lambda event: enviar())

ventana.mainloop()
