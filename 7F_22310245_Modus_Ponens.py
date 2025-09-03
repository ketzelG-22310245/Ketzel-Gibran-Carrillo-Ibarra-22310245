# Regla: Si una persona hace ejercicio regularmente, entonces mejora su salud cardiovascular.
def modus_ponens(ejercicio):
    if ejercicio:  # P
        return "La salud cardiovascular mejora."  # Q
    else:
        return "No se puede concluir nada."

# Caso: María hace ejercicio
print(modus_ponens(True))