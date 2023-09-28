from tkinter import *

root = Tk()

class PokemonClass(object):
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.WelcomeLabel = Label(root, text="Welcome! Pick your Pokemon!",
                                  bg="Black", fg="White")
        self.WelcomeLabel.pack(fill=X)

        self.CharButton = Button(root, text="Charmander", bg="RED", fg="White",
                                 command=self.CharClick)
        self.CharButton.pack(side=LEFT, fill=X)

        self.SquirtButton = Button(root, text="Squirtle", bg="Blue", fg="White")
        self.SquirtButton.pack(side=LEFT, fill=X)

        self.BulbButton = Button(root, text="Bulbasaur", bg="Dark Green",
                                 fg="White")
        self.BulbButton.pack(side=LEFT, fill=X)

    def CharClick(self):
        print ("You like Charmander!")
        global CharSwitch
        CharSwitch = 'Yes'

CharSwitch = 'No'

if CharSwitch == 'Yes':
    CharPhoto = PhotoImage(file="char.png")
    ChLabel = Label(root, image=CharPhoto)
    ChLabel.pack()

k = PokemonClass(root)
root.mainloop()