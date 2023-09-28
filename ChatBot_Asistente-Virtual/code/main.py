import tkinter as ttk
from tkinter import*
import speech_recognition as sr 
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import pyjokes
import requests
import yfinance as yf
import pyautogui

class myBot:
    def __init__(self,window):
        self.bienvenida()
        self.wind = window
        self.wind.title('Mi asistente Virtual- ChatBOT')

        # Frame Container
        frame = LabelFrame(self.wind, text = '¿Qué quieres que diga?')
        frame.grid(row=0, column=0,columnspan=3, pady=20)

        # Imput
        Label(frame,text='Ingrese una frase: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus() #parpadea el cursos
        self.name.grid(row=1, column=1)

        # Boton
        ttk.Button(frame, text = 'Speak', command = lambda: self.hablar(self.name.get()) ).grid(row=2,columnspan=2,sticky = W+E)
        #ttk.Button(text = 'ABRIR MENÚ', command = self.abrirMenu).grid(row=5,column=1, sticky = W+E)


        self.img = ttk.PhotoImage(file="fondo.png")
        ttk.Label(self.wind,image=self.img).grid(row=2,column=0)

        ttk.Button(self.wind, text = 'Activar Micrófono', command = self.activarMicrofono ).grid(row=3,columnspan=2)

        # Frame Container 2
        frame2 = LabelFrame(self.wind, text = 'Indique alguna función')
        frame2.grid(row=4, column=0,columnspan=3, pady=10)
        ttk.Button(frame2, text = '¿Qué hora es?', command = self.hora).grid(row=5,column=0,sticky=W+E)
        ttk.Button(frame2, text = '¿Qué día es?', command = self.dia).grid(row=5,column=1,sticky=W+E)
        ttk.Button(frame2, text = 'Contar un chiste', command = self.chiste).grid(row=6,column=0,sticky=W+E)
        ttk.Button(frame2, text = 'Clima', command = self.clima).grid(row=6,column=1,sticky=W+E)
        ttk.Button(frame2, text = 'Screenshot', command = self.capturarPantalla).grid(row=7,column=0,sticky=W+E)
        ttk.Button(frame2, text = 'Calculadora', command = self.calculadora).grid(row=7,column=1,sticky=W+E)

        ttk.Button(frame2, text = 'Buscar en Wiki', command = self.buscarWikipedia).grid(row=8,column=0,sticky=W+E)
        ttk.Button(frame2, text = 'Buscar en Google', command = self.buscarGoogle).grid(row=8,column=1,sticky=W+E)
        ttk.Button(frame2, text = 'Precio Acciones', command = self.precioAcciones).grid(row=9,column=0,sticky=W+E)
        ttk.Button(frame2, text = 'Precio Criptomoneda', command = self.precioCripto).grid(row=9,column=1,sticky=W+E)


        # Tabla
        #self.tree = ttk.Treeview(height=10, columns=2)
        #self.tree.grid(row=3,column = 0, columnspan=2)
        #self.tree.heading('#0', text = 'Name1', anchor = CENTER)
        #self.tree.heading('#1', text = 'Name2', anchor = CENTER)

    def bienvenida(self):
        self.hablar("Bienvenido de nuevo")

    def validation(self):
        return len(self.name.get()) != 0

    def actualizar(self):
        if self.validation():
            self.message['text'] = ''
        else:
            self.message['text'] = 'Ingrese nuevamente el texto'

    def hablar(self,msg):
        #pyttsx3.speak(msg)
        engine = pyttsx3.init()
        #voices = engine.getProperty('voices')       
        engine.setProperty('voice', 'spanish')
        #engine.setProperty('voice', voices[0].id)

        #engine.setProperty('rate', 200)  
        engine.say(text=msg, name="Saludo")
        engine.runAndWait()

    def escuchar(self):
        listener = sr.Recognizer() 
        while True:
            with sr.Microphone() as source:  
                print("Escuchando...")  
                audio = listener.listen(source,phrase_time_limit=4)  
                
                try:
                    print("Reconociendo el audio...")
                    text = listener.recognize_google(audio,language="es-PE").lower() 
                    return text

                except Exception as e: 
                    print("No se pudo reconocer la voz, repite por favor")
                    print(e)  
    

    def activarMicrofono(self):
        self.hablar("Micrófono activado, indíqueme una instrucción")
        instruccion = self.escuchar()
        print(instruccion)
        try:
            if (instruccion.find("hora")>=0):
                self.hora()
            if (instruccion.find("día")>=0):
                self.dia()
            if (instruccion.find("chiste")>=0):
                self.chiste()
            if (instruccion.find("clima")>=0):
                self.clima()
            if (instruccion.find("captura")>=0):
                self.capturarPantalla()
            if (instruccion.find("calcula")>=0):
                self.calculadora()
            if (instruccion.find("wiki")>=0):
                self.buscarWikipedia()
            if (instruccion.find("google")>=0):
                self.buscarGoogle()
            if (instruccion.find("youtube")>=0):
                self.buscarYB()
            if (instruccion.find("acciones")>=0):
                self.precioAcciones()
            if (instruccion.find("criptomoneda")>=0):
                self.precioCripto()
            
        except:
            self.hablar("No se pudo reconocer la voz, repite por favor")
    

    def abrirMenu(self):
        self.menuWindow = Toplevel()
        self.menuWindow.title = "Menú de Opciones"
        
        menuFrame = LabelFrame(self.menuWindow, text = '---MENÚ DE OPCIONES---')
        menuFrame.grid(row=0, column=0,columnspan=3, pady=20)

        Label(menuFrame,text='Indique una opción: ').grid(row=1, column=0)
        ttk.Button(menuFrame, text = 'Speak').grid(row=1,columnspan=2,sticky = W+E)
        
    def hora(self):
        self.hablar(f"La hora es {datetime.datetime.now().strftime('%H:%M')}")

    def dia(self):
        self.hablar(f"El dia de hoy es {datetime.datetime.now().day} del {datetime.datetime.now().month}")
        return 0
    
    def chiste(self):
        chiste = pyjokes.get_joke(language="es", category="neutral")
        self.hablar(chiste)

    def clima(self):
        city_name = "lima"
        API_key = "458ba21b0dc4e5c6d8c8656773f29e5b"
        datos = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&lang=es&units=metric').json()
        temperatura = datos['main']['temp']
        clima = datos['weather'][0]['description']
        self.hablar(f'La temperatura es de {temperatura} celsius')
        self.hablar(f'El clima es {clima}')
    
    def capturarPantalla(self):
        captura = pyautogui.screenshot()
        captura.save("C://Users/Joel Chavez/Desktop/captura.png")
        self.hablar("Captura realizada y guardada en el escritorio")

    def buscarWikipedia(self):
        self.hablar("Dime que quieres que busque en Wikipedia:")
        busca=self.escuchar()
        try:
            wikipedia.set_lang('es')
            busca = busca.replace('busca en wikipedia', '')
            resultado = wikipedia.summary(busca, sentences=3)
            self.hablar(f"Esto es lo que dice wikipedia: {resultado}")
            return 0
        except:
            self.hablar("No entendi bien lo que quieres buscar, vuelve a intentarlo")

    def buscarGoogle(self):
        self.hablar("Dime que quieres que busque en Google:")
        busca= self.escuchar()
        busca = busca.replace('buscar en google', '')
        self.hablar(f"Comenzando busqueda en google")
        pywhatkit.search(busca)
        self.hablar(f"Busqueda exitosa")
    
    def buscarYB(self):
        self.hablar("Dime que quieres que busque en Youtube:")
        busca= self.escuchar()
        busca = busca.replace('busca en youtube', '')
        self.hablar("Comenzando busqueda en youtube")
        pywhatkit.playonyt(busca)
        self.hablar(f"Busqueda exitosa")

    def precioAcciones(self):
        self.hablar("¿De que accion quieres saber su precio?")
        nombre_accion = self.escuchar()
        if "tesla" in nombre_accion:
            nombre = "tesla"
            simbolo = "TSLA"
        elif "amazon" in nombre_accion:
            nombre = "amazon"
            simbolo = "AMZN"
        elif "facebook" in nombre_accion:
            nombre = "facebook"
            simbolo = "FB"
        elif "google" in nombre_accion:
            nombre = "google"
            simbolo = "GOOG"
        elif "apple" in nombre_accion:
            nombre = "apple"
            simbolo = "AAPL"
        try:
            ticker = yf.Ticker(simbolo)
            data = ticker.history(period='1d')
            precio = data['Close'][0]

            self.hablar(f"El precio de {nombre} es de {precio}")
        except:
            self.hablar("No entendi a que accion te refieres")

    def precioCripto(self):
        self.hablar("¿De qué criptomoneda quieres saber su precio?")
        nombre_accion = self.escuchar()
        if "doge coin" in nombre_accion:
            nombre = "doge coin"
            simbolo = "DOGE-USD"
        elif "luna" in nombre_accion:
            nombre = "luna"
            simbolo = "LUNA-USD"
        elif "ethereum" in nombre_accion:
            nombre = "ethereum"
            simbolo = "ETH-USD"
        elif "cardano" in nombre_accion:
            nombre = "ada"
            simbolo = "ADA-USD"
        elif "bitcoin" in nombre_accion:
            nombre = "bitcoin"
            simbolo = "BTC-USD"
        elif "polkadot" in nombre_accion:
            nombre = "polkadot"
            simbolo = "DOT-USD"
        try:
            ticker = yf.Ticker(simbolo)
            data = ticker.history(period='1d')
            precio = data['Close'][0]

            self.hablar(f"El precio de {nombre} es de {precio}")
        except:
            self.hablar("No entendi a que accion te refieres")
    
    def calculadora(self):
        self.hablar("¿Que quieres calcular?")
        flag=True
        operacion_list = self.escuchar().split()
        operador = operacion_list[1]

        try:
            if (operador=='+') or (operador=='mas'):
                resultado = int(operacion_list[0]) + int(operacion_list[2])
            if (operador=='-') or (operador=='menos'):
                resultado = int(operacion_list[0]) - int(operacion_list[2])
            if (operador=='x') or (operador=='por'):
                resultado = int(operacion_list[0]) * int(operacion_list[2])
            if (operador=='/') or (operador=='entre'):
                resultado = float(operacion_list[0]) / float(operacion_list[2])
                flag=False

            if (flag):
                self.hablar(f"El resultado es: {resultado} ")
            else:
                self.hablar("El resultado es: {:.2f}".format(resultado))

        except:
            self.hablar("Al parecer no puedo realizar esta operacion")

if __name__=='__main__':
    window = Tk()
    app = myBot(window)
    window.mainloop()