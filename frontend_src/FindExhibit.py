from tkinter import *

class FindExhibitByName(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name = "FindExhibitByName"
        self.form = Frame(self)
        self.answers = Frame(self)
        #self.createform()
        Button(self, text="Go Home", command=lambda:controller.show_frame("Intro")
               ).grid(row=1, column=0)

    def createform(self):
        pass


class FindExhibitByMuseum(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name = "FindExhibitByMuseum"
        self.form = Frame(self)
        self.answers = Frame(self)
        #self.createform()
        Button(self, text="Go Home", command=lambda:controller.show_frame("Intro")
               ).grid(row=1, column=0)
