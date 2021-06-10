from tkinter import *
from tkinter import ttk

class FindArtByName(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name = "FindArtByName"
        self.form = Frame(self)
        self.answers = Frame(self)
        self.createform()
        self.controller = controller
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

        self.form.grid(row=0, column=0)

    def getArt(self):
        self.form.grid_remove()

        Label(self.answers, text=f"You searched for: {self.ArtTitle.get()}").grid(column=0, row=0)

        #need a subframe under answers for scrollbar to play nice
        resultframe = Frame(self.answers)
        resulttree = ttk.Treeview(resultframe, columns=('Title','Date','Artist'), selectmode=BROWSE)

        sb = Scrollbar(resultframe, orient=VERTICAL, command=resulttree.yview)
        sb.pack(side=RIGHT, fill=Y)

        resulttree.configure(yscrollcommand=sb.set)
        resultframe.grid(row=0, column=0)
        resulttree.column('#0', width=0, stretch=NO)
        resulttree.column('Title', anchor=E, minwidth=0, width=200)
        resulttree.column('Date', anchor=E, minwidth=0, width=200)
        resulttree.column('Artist', anchor=E, minwidth=0, width=200)
        resulttree.heading('#0', text='', anchor=W)
        resulttree.heading('Title', text='Title', anchor=CENTER)
        resulttree.heading('Date', text='Date', anchor=CENTER)
        resulttree.heading('Artist', text='Artist', anchor=CENTER)

        rownum = 0
        querystr = "select title, creationdate, name from artwork w "
        querystr += "join artist r on w.artistid=r.artistid"
        querystr += f" where title like '%{self.ArtTitle.get()}%'"
        results = self.controller.askdb.runQuery(querystr)
        for row in results:
            resulttree.insert(parent='',index=rownum, values=[i for i in row])
            rownum += 1

        resulttree.pack(side=LEFT)
        self.answers.grid(row=0, column=0)

class FindArtByArtist(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name="FindArtByArtist"
        self.form = Frame(self)
        self.answers = Frame(self)
        self.createform()
        self.controller = controller
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

        resulttree = ttk.Treeview(resultframe, columns=('Title','Date','Artist'), selectmode=BROWSE)


        sb = Scrollbar(resultframe, orient=VERTICAL, command=resulttree.yview)
        sb.pack(side=RIGHT, fill=Y)

        resulttree.configure(yscrollcommand=sb.set)

        resultframe.grid(row=0, column=0)

        resulttree.column('#0', width=0, stretch=NO)
        resulttree.column('Title', anchor=E, minwidth=0, width=200)
        resulttree.column('Date', anchor=E, minwidth=0, width=200)
        resulttree.column('Artist', anchor=E, minwidth=0, width=200)

        resulttree.heading('#0', text='', anchor=W)
        resulttree.heading('Title', text='Title', anchor=CENTER)
        resulttree.heading('Date', text='Date', anchor=CENTER)
        resulttree.heading('Artist', text='Artist', anchor=CENTER)


        rownum = 0
        querystr = "select title, creationdate, name from artwork w "
        querystr += "join artist r on w.artistid=r.artistid"
        querystr += f" where name like '%{self.ArtistName.get()}%'"
        results = self.controller.askdb.runQuery(querystr)
        for row in results:
            resulttree.insert(parent='',index=rownum, values=[i for i in row])
            rownum += 1

        resulttree.pack(side=LEFT)
        self.answers.grid(row=0, column=0, sticky="nsew")
