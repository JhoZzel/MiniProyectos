
import speech_recognition as sr
import pyttsx3
import pyaudio

listener = sr.Recognizer() 
def Escuchar1():
    while True:
        with sr.Microphone() as source:  
            print("Escuchando...")  
            audio = listener.listen(source,phrase_time_limit=4)  

            try:
                print("Reconociendo el audio...")
                text = listener.recognize_google(audio,language="es-PE").lower() 
                print(text)

            except Exception as e: 
                print("No se pudo reconocer la voz, repite por favor")
                print(e)  

Escuchar1()
