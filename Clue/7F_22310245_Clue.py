from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "7F_22310245_ClaveSecreta_Batman_Game"  # ✅ clave antes de usar session

# ====================================================
# FUNCIONES DE CASOS
# ====================================================

def caso1():
    """Caso 1 – Los Robins asesinados"""
    historia_inicial = (
        "Batman llega a la baticueva y ve los cuerpos de Dick Grayson, Jason Todd y Tim Drake colgados. "
        "Lleno de tristeza y venganza, debe descubrir quién los mató."
        "Inspecciona los cuerpos y ve que aunque esten colgados en la sala de comandos de la baticueva llega a la conclusion de que no fueron asesinados al momento de colgados y ahi en esa zona." 
        "Procede a investigar Gotham. "
    )

    lugares = {
        "Mansión Wayne": "Batman recuerda que el acertijo descubrio su identidad en una trampa de “adivina quien” para descubrir su verdadera identidad, asi que haber ido ahi a matar a sus hijos adoptivos era algo que seguro pudo haber pasado, sigio investigando y vio que estaba un cinturon lleno de sangre en la sala de la mansion, pero que sospechoso, ya que el informe muestra que murieron por asfixia o golpes en zonas vitales.",
        "Arkham": "Batman fue a la prision de arkham y le pregunto a uno de los policias lo sucedido ya que recuerda que los robins fueron a detener la fuga de prisioneros liderada por el Joker, el policia no recuerda mucho ya que lo noquearon a los pocos minutos en que los robins se estaban enfrentando a los prisioneros, pero recordaba que el joker traia un martillo con el que estaba pegandole a uno de los robins. Batman sabia que el joker conoce la baticueva.",
        "Cementerio de los Wayne": "Batman tiene enterrado a sus padres en el jardin de su mansion asi que fue a investigar ahi, cuando llego vio unos rastros de sangre que iban arrastrandose a la entrada de la baticueva y detras de esos rastros, unos pasos gigantes, se trataba de Bane y ademas uno de los tubos que lo alimentan con el suero de superfuerza tirado ahi, Batman sospecho que los robins lo cortaron y Bane aprovecho para asfixiarlos con eso.",
        "Fábrica abandonada": "Dos caras odiaba a los robins, veia la oportunidad para acabar con ellos, y la fabrica era un buen lugar para acabar con ellos, Batman llego ahi y vio un Batarang tirado y la pistola de dos caras recien usada, ademas de la moneda que siempre carga Dos caras con el, pero los robins no murieron de un disparo pero la sospecha de que dos caras hubiera sido el asesino no estaba descartada.",
        "Corte de los Búhos": "Batman fue a la corte de los buhos, ya que Talon tenia la mision de asesinar a Dick Grayson para poder cumplir con la orden de la corte, la espada de Talon estaba ahi rota, hubo un enfrentamiento ahi, pero batman sospecho que fuera Talon el asesino, ya que el al ser un villano nuevo en la ciudad no ha llegado a encontrar la baticueva como para dejar a los robins ahi colgados."
    }

    armas = ["Cinturón ensangrentado", "Martillo del Joker", "Tubo de suero", "Pistola de Dos Caras", "Espada rota de Talon"]
    personajes = ["El Acertijo", "El Joker", "Bane", "Dos Caras", "Talon"]

    historia_final = (
        "El asesino fue Bane. Las pistas eran claras: el rastro de sangre al cementerio, el tubo de suero roto y los pasos gigantes. "
        "Asfixió a los Robins con su propio sistema de fuerza."
    )

    return {
        "titulo": "Caso 1 - Los Robins asesinados",
        "introduccion": historia_inicial,
        "lugares": lugares,
        "armas": armas,
        "personajes": personajes,
        "solucion": {"asesino": "Bane", "arma": "Tubo de suero", "lugar": "Cementerio de los Wayne", "historia": historia_final}
    }


def caso2():
    """Caso 2 – Muerte de Alfred"""
    historia_inicial = (
        "Batman encuentra el cuerpo de Alfred tirado en la baticueva, con señales de tortura."
        "Lleno de tristeza, jura encontrar al culpable."
        "Inspecciona el cuerpo de Alfred y parece que fue torturado, tiene heridas de balas, golpes en zonas vitales, marcas en el cuello de asfixia y cortadas en las muñequas."
        "Procede a investigar Gotham."
    )

    lugares = {
        "Mansión Wayne": "Batman recuerda que el acertijo tenia en la mira a Alfred para descubrir la identidad de batman y sospecha que jugo “adivina quien” para descubrir su verdadera identidad, parece que cada vez que Alfred contestaba algo que el acertijo no queria que respondiera lo torturaba para que soltara la informacion, y no era solo una sospecha ya que estaba el baston del acertijo ahi tirado lleno de sangre.",
        "Arkham": "Batman fue a la prision de arkham ya que Alfred le gustaba visitar a su amigo Gordon ahi un rato, hubo una fuga en la prision, Gordon dijo que Alfred fue corriendo a ayudar a unos policias que se quedaron ahi entre la fuga y lo perdio de vista, Batman vio unos dientes de Killer  croc tirados y llenos de sangre, sospecho que las cortadas en las muñecas de Alfred eran de las mordidas de killer croc, pero algo no encajaba, Killer croc no pudo haberlo llevado a la baticueva.",
        "Cementerio de los Wayne": " Alfred todos los dias le llevaba flores a las tumbas de los Wayne, asi que Batman fue a investigar ahi, vio unas plantas raras que habian crecido ahi y unas ramas cortadas, parece que poison ivy pudo haber usado esas ramas para asfixiar a Alfred, fue a buscar la entrada de la baticueva que estaba en el cementerio y estaba sellada, pero poison ivy pudo abrir la tierra y llevar a Alfred a traves de la tierra a la baticueva.",
        "Fábrica abandonada": "Dos caras odiaba a Alfred ya que antes de convertirse en dos caras era un policia famoso, Alfred lo delato de ser un policia corrupto, Dos caras pudo haber secuestrado a Alfred y llevarlo a la fabrica, ademas estaba la pistola de Dos caras tirada y recien usada, y pudo aventarlo a la baticueva para que nadie sospechara que fue el.",
        "Corte de los Búhos": "Batman fue a la corte de los buhos, Alfred lo estaba ayudando a investigar asi que pudo haber ido, pero para sospecha de batman habia un cuchillo ensangrentado ahi y una corbata rota junto a el cuchillo, pero estaba lleno de barro, pudo haber sido clayface que engaño a Alfred disfrazandose de Talon y poder haberlo asesinado ahi, Clayface al ser un cambia formas pudo haber descubierto la baticueva engañando a la gente."
    }

    armas = ["Bastón del Acertijo", "Dientes de Killer Croc", "Ramas de Poison Ivy", "Pistola de Dos Caras", "Cuchillo ensangrentado"]
    personajes = ["El Acertijo", "Killer Croc", "Poison Ivy", "Dos Caras", "Clayface"]

    historia_final = (
        "El asesino fue El acertijo, las multiples pruebas de que fue torturado estaban claras, era un trabajo que llevaba tiempo y que no pudo haber sido un enfrentamiento rapido y no planeado, por lo que fue asesinado en la mansion wayne y el golpe de gracia fue el baston del acertijo."
    )

    return {
        "titulo": "Caso 2 - Alfred Pennyworth",
        "introduccion": historia_inicial,
        "lugares": lugares,
        "armas": armas,
        "personajes": personajes,
        "solucion": {"asesino": "El Acertijo", "arma": "Bastón del Acertijo", "lugar": "Mansión Wayne", "historia": historia_final}
    }


def caso3():
    """Caso 3 – Muerte de Barbara Gordon"""
    historia_inicial = (
        "Batman halla a Barbara Gordon muerta en la baticueva, con la espalda rota y heridas de bala."  
        "Debe descubrir quién la mató."
        "Inspecciona el cuerpo de Barbara y ve que no solo tiene multiples disparos, ademas tiene la espalda quebrada a mas no poder." 
        "Procede a investigar Gotham."
    )

    lugares = {
        "Mansión Wayne": " Barbara es una gran amiga de Batman por lo que de seguro estaba de visita ahi cuando Catwoman se metio a la mansion a robarle a Bruce Wayne, por lo que el intento de detenerla termino en tragedia, el latigo de catwoman estaba tirado en el sofa de la sala, lo mas seguro que al tratar de esconder el cuerpo de Barbara descubrio la entrada de la Baticueva y dejo el cuerpo ahi.",
        "Arkham": "Batman fue a la prision de arkham ya que Barbara visitaba a su padre Gordon todos los dias, pero lamentablemente hubo una fuga de prisioneros y entre ellos estaba el pinguino el cual uso a Barbara de rehen para poder escaparse, Batman vio una pistola que le habian robado a un policia, sospecho que al momento de poder escapar de la prision le disparo a Barbara ya que ya no le servia, pero todavia habia la duda de la espalda rota.",
        "Cementerio de los Wayne": "Barbara tenia una identidad secreta, ella era Batgirl, por lo que norlmalmente entraba a la baticueva por el cementerio de los wayne, Batman fe a investigar y vio un mazo roto, pudo haber sido usado para romperle la espalda a Barbara, mas adelante estaba un gorro de bufon tirado, Harley queen, penso Batman, pero ella no era tan inteligente para poder entrar a la baticueva y dejar ahi tirada a Barbara.",
        "Fábrica abandonada": "Barbara estaba investigando a Mr. frio y sabia que estaba escondido en la fabrica abandonada de Gotham por lo que Batman sigio los pasos que habia dejado Barbara y encontro el arma de frio de Mr frio descargada, penso Batman que pudo haber congelado la espalda de Barbara y asi poderla romper facilmente, y ya cuando llego Batman a la baticueva ya no habria rastros de que fue congelada.",
        "Corte de los Búhos": "Barbara ya habia tenido varos enfrentamientos junto a Nightwing como Batwoman contra Talon, porlo que esta vez decidio enfrentarse a Talon ella sola y pudo haber acabado en tragedia, Talon es un asesino experto e artes marciales por lo que le pudo haber roto la espalda y para acabar con el sufrimiento de Barbara rapido le disparo con la pistola que estaba tirada junto a una butaca de la corte de los buhos."
    }

    armas = ["Látigo de Catwoman", "Pistola robada", "Mazo roto", "Arma de Mr. Frío", "Pistola de Talon"]
    personajes = ["Catwoman", "El Pingüino", "Harley Quinn", "Mr. Frío", "Talon"]

    historia_final = (
        "El asesino fue Talon, Barbara no pudo ella sola contra el asesino de los buhos, por lo que le rompio la espalda y la remato con la pistola, Talon conocia la baticueva por lo que la dejo ahi como advertencia de no volver a enfrentarse a la corte de los Buhos."
    )

    return {
        "titulo": "Caso 3 - Barbara Gordon",
        "introduccion": historia_inicial,
        "lugares": lugares,
        "armas": armas,
        "personajes": personajes,
        "solucion": {"asesino": "Talon", "arma": "Pistola de Talon", "lugar": "Corte de los Búhos", "historia": historia_final}
    }


def caso4():
    """Caso 4 – Muerte de Jason Todd"""
    historia_inicial = (
        "Batman encuentra el cuerpo de Jason Todd con la cabeza destrozada." 
        "Debe descubrir quién lo mató."
        "Inspecciona el cuerpo de Jason y noto que tenia pintura roja como un labial y maquillaje blanco, sospechando de quien es el asesino procede a investigar Gotham."
    )

    lugares = {
        "Mansión Wayne": "Jason tenia una relacion extraña con Harley queen, el sentia algo por ella y trataba de ayudarla a dejar el lado malo, por lo que Batman sospecho que la llevo a la mansion para ayudarla ya que ella sabia que Jason era Robin, vio el martillo gigante de Harley ahi tirado, pero no parecia que estaba con sangre.",
        "Arkham": "Ese dia Jason fue a Arkham ya que habia una fuga de prisioneros liderada por Catwoman,  Batman estuvo inspeccionando el lugar y vio un pedazo de ropa de Robin junto al latigo de catwoman, pero esa arma no es lo suficientemente fuerte como para romperle destrozarle la cabeza.",
        "Cementerio de los Wayne": "Cuando Jason se enoja le gusta ir al cementerio de los Wayne para estar solo, por lo que Batman fue a investigar si algo sucedio ahi, vio unas plantas raras que habian crecido ahi y unas ramas cortadas, parece que poison ivy pudo haber usado esas ramas para golpear a Jason, fue a buscar la entrada de la baticueva que estaba en el cementerio y estaba sellada, pero poison ivy pudo abrir la tierra y llevar a Jason a traves de la tierra a la baticueva.",
        "Fábrica abandonada": " El joker estaba tramando algo en la fabrica y Jason fue a investigar en ese momento mientras Batman estaba persiguiendo a el pinguino, Batman llego y vio un tubo metalico lleno de sangre y pedazos de cabello ahi, y unos batarangs de Robin ahi, podria haber sido el el asesino.",
        "Corte de los Búhos": "Talia Al Ghul estaba en la mira de Jason ya que ella estaba llegando a un pacto con la corte de los buhos, Batman no estaba seguro de que Jason fuera ese dia a la corte ya que estaba ocupado con la fuga de prisioneros de Arkham y buscando al joker en la fabrica abandonada, solo vio una pistola que se veia que fue usada recientemente y una foto de Talia Al Ghul con Jason."
    }

    armas = ["Martillo de Harley", "Látigo de Catwoman", "Ramas de Poison Ivy", "Tubo metálico", "Pistola de Talia Al Ghul"]
    personajes = ["Harley Quinn", "Catwoman", "Poison Ivy", "El Joker", "Talia Al Ghul"]

    historia_final = (
        "El asesino fue el joker, ya que el maquillaje blanco y rojo que tenia Jason era de un payaso en este caso el joker, y las pruebas eran claras, golpeo a Jason con el tubo ensangrentado hasta matarlo y la prueba era el cabello  y los batarangs en la fabrica abandonada." 
        "Y como prueba de su obra dejo el regalo de la muerte de robin a batman."
    )

    return {
        "titulo": "Caso 4 - Jason Todd",
        "introduccion": historia_inicial,
        "lugares": lugares,
        "armas": armas,
        "personajes": personajes,
        "solucion": {"asesino": "El Joker", "arma": "Tubo metálico", "lugar": "Fábrica abandonada", "historia": historia_final}
    }


def caso5():
    """Caso 5 – Muerte de Jim Gordon"""
    historia_inicial = (
        "Batman encuentra el cuerpo de Jim Gordon colgado en la baticueva. Tiene heridas en el cuello y golpes en todo el cuerpo."
        "Inspecciona el cuerpo de Jim Gordon y noto que habia pedazos de un paraguas en la camisa toda ensangrentada de Gordon." 
        "Sospechando quien es el asesino procede a investigar Gotham."
    )

    lugares = {
        "Mansión Wayne": "Gordon habia ido a interrogar a Bruce Wayne a su mansion, no encontro a Bruce ya que batman estaba en una mision, batman vio la ventana rota por lo que sospecho que alguien se metio a robar mientras el estaba ahi y lo mato por tratar de detenerlo, llega a la chimenea y ve el latigo de catwoman tirado ahi.",
        "Arkham": "Hubo una fuga de prisioneros en Arkham por lo que de seguro Gordon fue a detener el escape, Batman fue a investigar y encontro varias pistolas de gangsters ahi, parece que el pinguino llevo a su equipo a liberar villanos de ahi, habia varios paraguas del pinguino tirados y sin municion, sospecho que el pinguino uso un paraguas para golpear a gordon y luego asfixiarlo contra la pared.",
        "Cementerio de los Wayne": "Batman fue al cementerio ya que Gordon se siente culpable por no poder resolver el misterio de los asesinos de Bruce, y aprovecho a visitar el lugar cuando fue a interrogar a Bruce, encontro un tubo de los que alimentan de supersuero a bane tirado y unos pasos grandes, pero ni un rastro de Gordon por la zona.",
        "Fábrica abandonada": " Dos caras llevaba a sus victimas a la fabrica abandonada y les quemaba la mitad de la cara con el acido de la fabrica, Gordon ya llevaba tiempo investigandolo por lo que Batman fue a ver si Gordon habia ido ahi antes de que lo mataran, vio la pistola recien usada de dos caras pero Gordon no murio de algun disparo.",
        "Corte de los Búhos": "Gordon le habia llegado una invitacion a la corte de los buhos, ya que estos ya habian reclutado policias corruptos a su favor ya que estos ya tenian bajo su control la mitad de la ciudad, Batman fue a ver si Gordon fue a la corte y ahi fue asesinado, llego y vio unos batarangs de robin y a unos miembros de la corte de los buhos atados, Talon habia escapado y dejado su espada ahi tirada. Gordon no murio de cortes de espada."
    }

    armas = ["Látigo de Catwoman", "Paraguas del Pingüino", "Tubo de Bane", "Pistola de Dos Caras", "Espada de Talon"]
    personajes = ["Catwoman", "El Pingüino", "Bane", "Dos Caras", "Talon"]

    historia_final = (
        "El asesino fue el pinguino, el pedazo de paraguas era evidente, Gordon ya habia detenido a varios gangsters del pinguino y de seguro ya estaba harto de el que lo mato, llevo el cadaver a la baticueva y lo colgo como advertencia de que lo dejaran en paz."
    )

    return {
        "titulo": "Caso 5 - Jim Gordon",
        "introduccion": historia_inicial,
        "lugares": lugares,
        "armas": armas,
        "personajes": personajes,
        "solucion": {"asesino": "El Pingüino", "arma": "Paraguas del Pingüino", "lugar": "Arkham", "historia": historia_final}
    }


# ====================================================
# LISTA DE CASOS Y VARIABLES GLOBALES
# ====================================================

casos = [caso1, caso2, caso3, caso4, caso5]
caso_actual = None
lugares_visitados = set()

# ====================================================
# RUTAS DEL JUEGO
# ====================================================

@app.route('/')
def menu():
    session.clear()
    return render_template('menu.html')

@app.route('/start')
def start():
    """Selecciona un caso aleatorio y muestra la introducción"""
    caso_func = random.choice(casos)
    caso = caso_func()

    session['caso'] = caso
    session['lugares_visitados'] = []

    return render_template(
        'intro.html',
        titulo=caso["titulo"],
        introduccion=caso["introduccion"]
    )

@app.route('/lugares')
def lista_lugares():
    """Muestra lista de lugares para investigar"""
    caso = session.get('caso')
    if not caso:
        return redirect(url_for('menu'))

    lugares_visitados = session.get('lugares_visitados', [])
    todos_visitados = len(lugares_visitados) == len(caso["lugares"])

    return render_template(
        'lugares.html',
        titulo=caso["titulo"],
        lugares=caso["lugares"],
        lugares_visitados=lugares_visitados,
        todos_visitados=todos_visitados
    )

@app.route('/investigar/<lugar>')
def investigar(lugar):
    """Muestra descripción del lugar"""
    caso = session.get('caso')
    if not caso:
        return redirect(url_for('menu'))

    descripcion = caso['lugares'].get(lugar, "No hay información disponible sobre este lugar.")
    return render_template('investigar.html', lugar=lugar, descripcion=descripcion)

@app.route('/marcar_visitado/<lugar>', methods=['POST'])
def marcar_visitado(lugar):
    """Marca un lugar como visitado"""
    caso = session.get('caso')
    if not caso:
        return '', 204

    lugares_visitados = session.get('lugares_visitados', [])
    if lugar not in lugares_visitados and lugar in caso['lugares']:
        lugares_visitados.append(lugar)
        session['lugares_visitados'] = lugares_visitados
    return '', 204

@app.route('/juego')
def juego():
    """Solo accesible si ya visitó todos los lugares"""
    caso = session.get('caso')
    if not caso:
        return redirect(url_for('menu'))

    lugares_visitados = session.get('lugares_visitados', [])
    if len(lugares_visitados) < len(caso["lugares"]):
        return redirect(url_for('lista_lugares'))

    return render_template(
        'juego.html',
        titulo=caso["titulo"],
        personajes=caso["personajes"],
        lugares=caso["lugares"].keys(),
        armas=caso["armas"]
    )

@app.route('/resultado', methods=['POST'])
def resultado():
    caso = session.get('caso')
    if not caso:
        return redirect(url_for('menu'))

    asesino = request.form['asesino']
    arma = request.form['arma']
    lugar = request.form['lugar']

    correcto = (
        asesino == caso['solucion']['asesino'] and
        arma == caso['solucion']['arma'] and
        lugar == caso['solucion']['lugar']
    )

    fondos_resultado = {
        "Caso 1 - Los Robins asesinados": "resultado_robins.jpg",
        "Caso 2 - Alfred Pennyworth": "resultado_alfred.jpg",
        "Caso 3 - Barbara Gordon": "resultado_barbara.jpg",
        "Caso 4 - Jason Todd": "resultado_jason.jpg",
        "Caso 5 - Jim Gordon": "resultado_gordon.jpg"
    }

    titulo_caso = caso.get("titulo", "")
    imagen_resultado = fondos_resultado.get(titulo_caso, "credits.jpg")

    return render_template(
        "resultado.html",
        correcto=correcto,
        caso=caso,
        imagen_resultado=imagen_resultado
    )

@app.route('/creditos')
def creditos():
    return render_template('creditos.html')

@app.route('/exit')
def salir():
    session.clear()
    return "Juego cerrado. Puedes cerrar esta pestaña."


if __name__ == '__main__':
    app.run(debug=True)