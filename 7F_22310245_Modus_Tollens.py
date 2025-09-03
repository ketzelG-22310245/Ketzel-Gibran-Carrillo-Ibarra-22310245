# Regla: Si un dispositivo tiene batería cargada, entonces enciende.
def modus_tollens(encendido):
    if not encendido:  # ¬Q
        return "El dispositivo NO tiene batería cargada."  # ¬P
    else:
        return "El dispositivo tiene batería cargada."

# Caso: El dispositivo NO enciende
print(modus_tollens(False))