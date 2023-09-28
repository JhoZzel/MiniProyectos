import imghdr
import tkinter as ttk
import pyttsx3
from tkinter import*




myWindow = ttk.Tk()
myWindow.geometry("400x400")
myWindow.title("Asistente Virtual UNI")

img = ttk.PhotoImage(file="fondo.png")
ttk.Label(myWindow,image=img).grid(row=0,column=0)

et1 = ttk.Label(myWindow, text="label1",bg="red",width=10,height=5)
et2 = ttk.Label(myWindow, text="label2",bg="green",width=10,height=5)

et1.grid(row=0, column=0)
et2.grid(row=1, column=1)

et3 = ttk.Label(myWindow, text="label3",bg="red",width=10,height=5)
et4 = ttk.Label(myWindow, text="label4",bg="green",width=10,height=5)
et3.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=0.2)
et4.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.2)



myWindow.mainloop()