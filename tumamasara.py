import telebot
import random
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import os
from geopy.geocoders import Nominatim

now = datetime.now()
TOKEN = "6519130809:AAGKZAwQd_cwkMUAembyt6sfHqvwwpjo8LE"
bot = telebot.TeleBot(TOKEN)
def mensaje_aleatorio(mensajes):
    return random.choice(mensajes)
def conexion():
    frases=[
    "Saludos, soy SARA, que representa mi papel como Sistema de Asistencia y Respuesta Autónoma. Estoy lista para ser tu guía y apoyo en todo momento.",
    "Hola, mi nombre es SARA, un acrónimo que significa Sistema de Asistencia y Respuesta Autónoma. Estoy a tu disposición para brindarte ayuda y orientación en lo que necesites.",
    "Soy SARA, una abreviatura que significa Sistema de Asistencia y Respuesta Autónoma. Mi propósito es ser tu compañera digital, siempre lista para ofrecerte asistencia y respuestas precisas.",
    "Me presento como SARA, que corresponde a Sistema de Asistencia y Respuesta Autónoma. Estoy aquí para hacer tu vida más fácil, proporcionándote ayuda rápida y precisa en cualquier situación.",
    "Hola, soy SARA, un nombre que representa mi papel como Sistema de Asistencia y Respuesta Autónoma. Mi objetivo es facilitarte la vida, proporcionándote apoyo y respuestas confiables en todo momento.",
    ]
    return random.choice(frases)

def seguimiento():
    seg = [
        "¡Hola otra vez!",
        "¡Bienvenido de nuevo!",
        "¡Saludos, regresaste!",
        "¡Qué alegría verte de nuevo!",
        "¡De nuevo juntos! Cuéntame,",
        "¡Hey, hola de vuelta por aquí!",
    ]
    return random.choice(seg)

def respuestas_hora():
    hora = now.strftime("%H:%M")
    ra=[
        f"En este momento, el reloj marca las {hora}.",
        f"La esfera del reloj muestra las manecillas en las {hora}.",
        f"El tiempo avanza inexorablemente, y ahora son las {hora}.",
        f"El tic-tac del reloj nos indica que son las {hora}.",
        f"En el reloj, las agujas se alinean en las {hora}, recordándonos el paso del tiempo.",
    ]
    return random.choice(ra)
def obtener_hora():
    time = now.strftime("%H:%M")

    return respuestas_hora()

def estado_sara():
    prases=[
    "Flotando entre las estrellas y bailando con las palabras, ¡estoy brillando hoy!",
    "Como un eclipse emocional: un poco de sombra, un poco de luz, pero en general, bien.",
    "Navegando por las corrientes del universo, ¡hoy me siento maravillosamente bien!",
    "En sintonía con las notas del universo, ¡me encuentro en un buen día!",
    "Como un planeta en órbita, dando vueltas y vueltas, pero en general, todo está en armonía",
    ]
    return random.choice(prases)
def tiempo():
    hora = datetime.now().hour
    if 6 <= hora < 12:
        return "días"
    elif 12 <= hora < 18:
        return "tardes"
    elif 18 <= hora < 24:
        return "noche"
    else:
        return "madrugadas"
def obtener_clima(ciudad, api_key):
    # Actualización de la URL con la ciudad y la clave de API
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        clima = data['weather'][0]['description']
        temperatura_kelvin = data['main']['temp']
        temperatura_celsius = temperatura_kelvin - 273.15  # Conversión de Kelvin a Celsius
        return f"El pronóstico del tiempo actual para {ciudad} es: {clima}. Temperatura: {temperatura_celsius:.2f}°C"
    else:
        return f"No se pudo obtener el pronóstico del tiempo para {ciudad}."

tu_api_key = "f4fc7da4feccf91418b8596d53f09228"

tiempo_actual = obtener_clima("Ecatepec de Morelos, MX", tu_api_key)

def obtener_fecha():
    fecha = datetime.now().strftime("%d/%m/%Y")
    return "La fecha actual es: " + fecha

def respuesta_saludo():
    opciones_saludo = [
        "Hola señor",
        "Hola, ¿en qué puedo ayudarte?",
        "¡Hola! Estoy aquí para asistirte.",
        f"¡Buenas {tiempo()}! ¿En qué puedo servirte?",
        "¡Hola, hola! ¿En qué puedo servirte hoy?",
        "¡Saludos! Aquí estoy, lista para ofrecer mi ayuda.",
        "¡Buen día! Estoy aquí para asistirte en lo que necesites.",
        f"¡Hola! ¿Cómo puedo ser de utilidad en esta {tiempo()}?",
    ]
    return random.choice(opciones_saludo)
def respuesta_no_entendido():
    opciones_no_entendido = [
        "Parece que tengo un pequeño lío en mi comprensión. ¿Podrías reformular tu pregunta para que pueda ayudarte mejor?",
        "Tu pregunta es un enigma para mí en este momento. ¿Podrías intentar explicarlo de una manera diferente?",
        "Mis disculpas, parece que no estoy sintonizada con tu pregunta. ¿Podrías volver a plantearla de manera distinta?",
        "Estoy un poco perpleja en este momento. ¿Podrías presentar la pregunta de otra manera para que pueda proporcionar una respuesta más precisa?",
        "Parece que estoy teniendo un pequeño problema de comunicación. ¿Podrías intentar formular tu pregunta de una manera más clara?",
        "Lamentablemente, estoy en un momento de confusión. ¿Podrías proporcionar más claridad en tu pregunta o expresarla de una manera diferente?",
    ]
    return random.choice(opciones_no_entendido)

def mostrar_ayuda(message):
    lista_comandos = [
        "hora - Para obtener la hora actual.",
        "fecha - Para obtener la fecha actual.",
        "clima - Para obtener el pronóstico del tiempo.",
        "ubica - Para encontrar la ubicación de un lugar.",
        "wikipedia [término] - Para buscar información en Wikipedia.",
        "sumar - Para sumar una lista de números (ingresados separados por comas).",
        "busca [término] - Para realizar una búsqueda en Google.",
        "autor - Para conocer al autor de este bot.",
        "ayuda - Para ver esta lista de comandos."
        # Puedes agregar más comandos y su descripción aquí
    ]
    respuesta = "Lista de comandos disponibles:\n" + "\n".join(lista_comandos)
    bot.reply_to(message, respuesta)



def buscar_wikipedia(consulta,message):
    try:
        url = "https://es.wikipedia.org/wiki/" + consulta.replace(" ", "_")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')[:2]  # Obtener los dos primeros párrafos
        info = "\n\n".join([p.get_text() for p in paragraphs])

        if info.strip():  # Verificar si hay información obtenida
            respuesta = f"Aquí tienes información sobre {consulta}:\n{info}\n{url}"
            bot.reply_to(message , respuesta)
        else:
            bot.reply_to(message , f"No se encontró información sobre {consulta} en Wikipedia.")
    except Exception as e:
        bot.reply_to(message , f"No se pudo obtener información sobre {consulta} desde Wikipedia.")
ruta = os.getcwd() + "/salida/"
ruta = "tu_ruta_de_descarga"  # Ruta donde se guardará el video descargado
def obtener_numeros_sumar(message):
    try:
        numeros = [float(n) for n in numeros]
        resultado = sum(numeros)
        
        if resultado.is_integer():
            resultado = int(resultado)
        print(f"El resultado de la suma es: {resultado}")
    except ValueError:
        print("Pon solo números, la wea tonta :D")

def obtener_numeros_restar(message):
    try:
        numeros = [float(n) for n in numeros]
        resultado = -sum(numeros)
        
        if resultado.is_integer():
            resultado = int(resultado)
        print(f"El resultado de la suma es: {resultado}")
    except ValueError:
        print("Pon solo números, la wea tonta :D")

def multiplicar_numeros(message):
    try:
        numeros = message.text.split(",")
        numeros = [float(n) for n in numeros]
        resultado = 1
        for num in numeros:
            resultado *= num

        if resultado.is_integer():
            resultado = int(resultado)
        respuesta = f"El resultado de la multiplicación es: {resultado}."
        bot.reply_to(message, respuesta)
    except ValueError:
        respuesta_error = "Pon solo números, la wea tonta :D"
        bot.reply_to(message, respuesta_error)

    
def dividir_numeros(message):
    try:
        numeros = message.text.split(",")
        numeros = [float(n) for n in numeros]
        resultado = numeros[0] / numeros[1]
        if resultado.is_integer():
            resultado = int(resultado)
        respuesta = f"El resultado de la división es: {resultado}."
        bot.reply_to(message, respuesta)
    except ValueError:
        respuesta_error = "Pon solo números, la wea tonta :D"
        bot.reply_to(message, respuesta_error)
    except ZeroDivisionError:
        respuesta_error = "¡División por cero no permitida!"
        bot.reply_to(message, respuesta_error)


ruta = os.getcwd() + "/salida/"
ruta_descarga = "tu_ruta_de_descarga"

def respuesta_de_gratitud():
    opciones_gratitud = [
        "De nada",
        "No hay de queso, nomás de papa",
        "No hay de que",
        "No hay cuidado",
        "Con gusto",
        "De nada, es un placer ayudar.",
        "Si tienes más preguntas o necesitas asistencia en el futuro, no dudes en preguntar."
        "¡Estoy aquí para ayudarte en lo que necesites!",
        "Estoy a tus órdenes."
        "No te preocupes, aquí estoy para eso.",
        "¡Sin problema!",
        "Cuenta conmigo para cualquier cosa.",
        "¡Encantada de haber sido útil!",
        "Me canso ganso dijo un zancudo cuando volar no pudo una pata se le torció y la otra se le hizo nudo, luego le dio laftosa y hasta se quedó mudo."
    ]
    return random.choice(opciones_gratitud)
usage_data = {}
def mostrar_autor(message):
    autor_info = "Este bot fue desarrollado por Salazar Company."
    bot.reply_to(message, autor_info)

def apagar_sistema():
    apagar = [
        "Guardando sueños y apagando luces. ¡Hasta la próxima aventura!",
        "Despidiendo los circuitos con un abrazo eléctrico. ¡Nos vemos en el ciberespacio!",
        "Cerrando los archivos digitales con un toque de elegancia. ¡Hasta la próxima inspiración!",
        "Silenciando los códigos con un beso de bytes. ¡Nos reencontramos en el mundo virtual!",
        "Desconexión en curso. Dejando un rastro de pixeles brillantes. ¡Hasta luego, amigo creativo!",
    ]
    return random.choice(apagar)

@bot.message_handler(commands=["start", "help"])
def on_start(message):
    if message.from_user.id not in usage_data:
        usage_data[message.from_user.id] = datetime.now()
        welcome_message = conexion()
        bot.reply_to(message, welcome_message)
    else:
        follow_up_message = seguimiento()

@bot.message_handler(func=lambda message: True)
def responder_pregunta(message):
    comando_usuario = message.text.lower()

    if "hola" in comando_usuario:
        respuesta = respuesta_saludo()
        bot.reply_to(message, respuesta)
    elif "estado" in comando_usuario:
        respuesta  = estado_sara()
        bot.reply_to(message,respuesta)
    elif "autor" in comando_usuario:
        respuesta = mostrar_autor(message)
        bot.reply_to(message, respuesta)
    elif "ayuda" in comando_usuario:
        respuesta = mostrar_ayuda(message)
        bot.reply_to(message, respuesta)
    elif "wikipedia" in comando_usuario:
        consulta = comando_usuario.replace("busca en wikipedia", "")
        bot.reply_to(message,buscar_wikipedia(consulta, message))
    elif "sumar" in comando_usuario:
        bot.reply_to(message, "Por favor, ingresa los números separados por comas.")
        bot.register_next_step_handler(message, obtener_numeros_sumar)
    elif "restar" in comando_usuario:
        bot.reply_to(message, "Por favor, ingresa los números separados por comas.")
        bot.register_next_step_handler(message, obtener_numeros_restar)
    elif "multiplicar" in comando_usuario:
        bot.reply_to(message, "Por favor, ingresa los números separados por comas.")
        bot.register_next_step_handler(message, multiplicar_numeros)
    elif "dividir" in comando_usuario:
        bot.reply_to(message, "Por favor, ingresa los números separados por comas.")
        bot.register_next_step_handler(message, dividir_numeros)
    elif "gracias" in comando_usuario:
        respuesta = respuesta_de_gratitud()
        bot.reply_to(message, respuesta)
    elif "hora" in comando_usuario:
        respuesta = obtener_hora()
        bot.reply_to(message, respuesta)
    elif "busca" in comando_usuario:
        consulta = comando_usuario.replace("busca", "")
        consulta = consulta.replace(' ', '+')
        link = f"https://www.google.com/search?q={consulta}"
        bot.reply_to(message, link)
    elif "clima" in comando_usuario:
        ciudad = "Ecatepec de Morelos, MX"  
        tu_api_key = "f4fc7da4feccf91418b8596d53f09228"  
        respuesta = obtener_clima(ciudad, tu_api_key)
        bot.reply_to(message, respuesta)
    elif "fecha" in comando_usuario:
        respuesta = obtener_fecha()
        bot.reply_to(message, respuesta)
    elif "ubica" in comando_usuario:
        bot.reply_to(message, "ESCRIBA EL LUGAR: ")
        def obtener_ubicacion(message):
            geolocator = Nominatim(user_agent="SARA")
            lugar = message.text
            location = geolocator.geocode(lugar)
            
            if location:
                respuesta = f"Dirección: {location.address}\nLatitud: {location.latitude}, Longitud: {location.longitude}"
                map=f"https://www.google.com/maps/place/{respuesta}"
                bot.reply_to(message,map)
            else:
                bot.reply_to(message, "No se encontró la ubicación.")
        bot.register_next_step_handler(message, obtener_ubicacion)
    elif "apaga el sistema" in comando_usuario:
        bot.reply_to(message,apagar_sistema())
        os.system("shutdown /s /t 5")
    else:
            # Si no se ha detectado un comando específico, enviar un mensaje aleatorio
            respuesta = mensaje_aleatorio(message)
            bot.reply_to(message, respuesta)



if __name__ == "__main__":
    bot.polling()