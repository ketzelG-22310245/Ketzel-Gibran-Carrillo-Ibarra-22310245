#Ketzel Gibran Carrillo Ibarra 22310245

import numpy as np

# Base de películas (simples ejemplos)
peliculas = [
    ("Acción pura", [1, 0, 0, 0, 0]),
    ("Comedia", [0, 1, 0, 0, 0]),
    ("Romance", [0, 0, 1, 0, 0]),
    ("Terror", [0, 0, 0, 1, 0]),
    ("Ciencia ficción", [0, 0, 0, 0, 1]),
    ("Acción + Comedia", [1, 1, 0, 0, 0]),
    ("Comedia + Romance", [0, 1, 1, 0, 0]),
    ("Acción + Sci-Fi", [1, 0, 0, 0, 1]),
    ("Romance + Terror", [0, 0, 1, 1, 0]),
    ("Terror + Sci-Fi", [0, 0, 0, 1, 1]),
]

X = np.array([p[1] for p in peliculas])

# Preferencias iniciales del usuario (para entrenar el modelo base)
y = np.array([0.9, 0.5, 0.1, 0.0, 0.8, 0.7, 0.3, 1.0, 0.0, 0.6])

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class PerceptronRecomendador:
    def __init__(self, input_size, lr=0.1, epochs=100):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.lr = lr
        self.epochs = epochs

    def predict(self, x):
        return sigmoid(np.dot(x, self.weights) + self.bias)

    def train(self, X, y):
        for epoch in range(self.epochs):
            for xi, target in zip(X, y):
                pred = self.predict(xi)
                error = target - pred
                # Ajuste de pesos
                self.weights += self.lr * error * xi
                self.bias += self.lr * error

# Entrenar perceptrón
p = PerceptronRecomendador(input_size=5, lr=0.1, epochs=200)
p.train(X, y)

# === Interacción con el usuario ===
print("\nCalifica del 1 (no me gusta) al 10 (me encanta) cada género:\n")

accion = float(input("Acción (1-10): ")) / 10
comedia = float(input("Comedia (1-10): ")) / 10
romance = float(input("Romance (1-10): ")) / 10
terror = float(input("Terror (1-10): ")) / 10
scifi = float(input("Ciencia Ficción (1-10): ")) / 10

preferencias_usuario = np.array([accion, comedia, romance, terror, scifi])

# Calcular afinidad con cada película
afinidades = []
for nombre, vector in peliculas:
    score = p.predict(preferencias_usuario * vector)
    afinidades.append((nombre, score))

# Ordenar de mayor a menor afinidad
afinidades.sort(key=lambda x: x[1], reverse=True)

# Mostrar solo el TOP 3
print("\n🎬 Top 3 Recomendaciones basadas en tus gustos:\n")
for i, (nombre, score) in enumerate(afinidades[:3], start=1):
    print(f"{i}. {nombre} (Afinidad: {score:.2f})")
