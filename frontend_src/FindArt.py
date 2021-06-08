from tkinter import *
from tkinter import ttk

class FindArtByName(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name = "FindArtByName"
        self.form = Frame(self)
        self.answers = Frame(self)
        self.createform()
        Button(self, text="Go Home", command=lambda:controller.show_frame("Intro")
               ).grid(row=1, column=0)


    def createform(self):
        self.ArtTitle = StringVar()

        Label(self.form, text="Painting Name:"
              ).grid(row=0, column=0, padx=5, pady=5, sticky=E)
        Entry(self.form, textvariable=self.ArtTitle
              ).grid(row=0, column=1, padx=5, pady=5, sticky="we")
        Button(self.form, text="search", command=self.getArt
               ).grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.form.grid(row=0, column=0, sticky="nsew")

    def getArt(self):
        self.form.grid_remove()
        #connect to backend here i guess?
        Label(self.answers, text=f"You searched for: {self.ArtTitle.get()}").grid(column=0, row=0)
        self.answers.tkraise()

        resultframe = Frame(self.answers)

        results = ttk.Treeview(resultframe, columns=('a','b','c'), selectmode=BROWSE)


        sb = Scrollbar(resultframe, orient=VERTICAL, command=results.yview)
        sb.pack(side=RIGHT, fill=Y)

        results.configure(yscrollcommand=sb.set)

        resultframe.grid(row=0, column=0)

        results.column('#0', width=0, stretch=NO)
        results.column('Title', anchor=E, minwidth=0, width=200)
        results.column('Date', anchor=E, minwidth=0, width=200)
        results.column('Artist', anchor=E, minwidth=0, width=200)

        results.heading('#0', text='', anchor=W)
        results.heading('Title', text='Title', anchor=CENTER)
        results.heading('Date', text='Date', anchor=CENTER)
        results.heading('Artist', text='Artist', anchor=CENTER)

        #retrieve and parse results
        results.insert(parent='',index=0, values=("Starry Night","2020-02-01","Andrew Koltko"))
        results.insert(parent='',index=1, values=("Starry Night","2015-05-12","Pablo Picasso"))
        results.insert(parent='',index=2, values=("Starry Night","2009-11-23","Vincent Van Gogh"))
        results.insert(parent='',index=3, values=("Starry Night","1883-06-31","Yoko Ono"))

        results.pack(side=LEFT)
        self.answers.grid(row=1, column=0, sticky="nsew")

class FindArtByArtist(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name="FindArtByArtist"
        self.form = Frame(self)
        self.answers = Frame(self)
        self.createform()
        Button(self, text="Go Home", command=lambda:controller.show_frame("Intro")
               ).grid(row=1, column=0)

    def createform(self):
        self.ArtistName = StringVar()

        Label(self.form, text="Artist Name:"
              ).grid(row=0, column=0, padx=5, pady=5, sticky=E)
        Entry(self.form, textvariable=self.ArtistName
              ).grid(row=0, column=1, padx=5, pady=5, sticky="we")
        Button(self.form, text="search", command=self.getArt
               ).grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.form.grid(row=0, column=0)

    def getArt(self):
        self.form.grid_remove()
        #connect to backend here i guess?
        Label(self.answers, text=f"You searched for: {self.ArtistName.get()}").grid(column=0, row=0)
        self.answers.tkraise()

        resultframe = Frame(self.answers)

        results = ttk.Treeview(resultframe, columns=('a','b','c'), selectmode=BROWSE)


        sb = Scrollbar(resultframe, orient=VERTICAL, command=results.yview)
        sb.pack(side=RIGHT, fill=Y)

        results.configure(yscrollcommand=sb.set)

        resultframe.grid(row=0, column=0)

        results.column('#0', width=0, stretch=NO)
        results.column('Title', anchor=E, minwidth=0, width=200)
        results.column('Date', anchor=E, minwidth=0, width=200)
        results.column('Artist', anchor=E, minwidth=0, width=200)

        results.heading('#0', text='', anchor=W)
        results.heading('Title', text='Title', anchor=CENTER)
        results.heading('Date', text='Date', anchor=CENTER)
        results.heading('Artist', text='Artist', anchor=CENTER)

        #Norman Rockwell
        results.insert(parent='', index=0, values=("Freedom from Want","1943-01-01","Norman Rockwell"))
        results.insert(parent='', index=1, values=("Freedom of Speech","1943-02-01","Norman Rockwell"))
        results.insert(parent='', index=2, values=("Saying Grace","1951-01-01","Norman Rockwell"))
        results.insert(parent='', index=3, values=("The Runaway","1958-01-01","Norman Rockwell"))

        results.pack(side=LEFT)
        self.answers.grid(row=1, column=0, sticky="nsew")
