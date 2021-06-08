from tkinter import *

class FindArtist(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name = "FindArtist"
        self.form = Frame(self)
        self.answers = Frame(self)
        #self.createform()
        Button(self, text="Go Home", command=lambda:controller.show_frame("Intro")
               ).grid(row=1, column=0)
