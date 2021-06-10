from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json

class AdminPage(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name = "AdminPage"
        self.main = Frame(self)
        self.controller = controller
        Button(self, text="Go Home", command=lambda:controller.show_frame("Intro")
               ).grid(row=1, column=0, pady = 5)
        self.pages = {"login":self.loginPage,
                      "main":self.adminMainPage,
                      "artist":self.addArtistPage,
                      "collector":self.addCollectorPage,
                      "venue":self.addVenuePage,
                      "artwork":self.addArtworkPage,
                      "exhibit":self.addExhibitPage,
                      "style":self.addArtStylePage}
        self.current_frame = None
        self.openpage("login")
        self.main.grid(row=0, column=0)
        Button(self, text="Go to Admin Page", command=lambda:self.openpage("main")
               ).grid(row=1, column=0, pady=5)

    def openpage(self, page):
        for child in self.main.winfo_children():
            child.destroy() #I had to search 'destry all children' to find this answer
        self.pages[page]().grid(row=0, column=0)

    def loginPage(self):
        #frame login
        login = Frame(self.main)
        Label(login, text="Please Enter your Username and Password"
              ).grid(row=0, column=0, columnspan=2)
        u = StringVar()
        p = StringVar()
        Label(login, text="Username:"
              ).grid(row=1, column=0, pady=5, sticky=E)
        Entry(login, textvariable=u
              ).grid(column=1, row=1, pady=5, sticky=W)
        Label(login, text="Password:"
              ).grid(row=2, column=0, pady=5, sticky=E)
        Entry(login, textvariable=p, show="*"
              ).grid(column=1, row=2, pady=5, sticky=W)
        Button(login, text="Log In", command=lambda:self.checkLogin(u.get(),p.get())
               ).grid(row=3, column=0, columnspan=2, pady=5)
        return login

    def checkLogin(self, u, p):
        with open("adminpw.json") as ld:
            logins = json.load(ld)
            if u in logins and logins[u]==p:
                self.openpage("main")
            else:
                messagebox.showerror(message="Incorrect Username or Password, Please Try Again")

    def adminMainPage(self):
        main = Frame(self.main)
        Label(main, text="What Would You Like To Do?"
              ).grid(row=0, column=0, columnspan=6, padx=5, pady=5)
        Button(main, text="Add an Artist", command=lambda:self.openpage("artist")
               ).grid(row=1, column=0, padx=5, pady=5)
        Button(main, text="Add a Collector", command=lambda:self.openpage("collector")
               ).grid(row=1, column=1, padx=5, pady=5)
        Button(main, text="Add a Venue", command=lambda:self.openpage("venue")
               ).grid(row=1, column=2, padx=5, pady=5)
        Button(main, text="Add an Artwork", command=lambda:self.openpage("artwork")
               ).grid(row=1, column=3, padx=5, pady=5)
        Button(main, text="Add an Exhibit", command=lambda:self.openpage("exhibit")
               ).grid(row=1, column=4, padx=5, pady=5)
        Button(main, text="Add an Art Style", command=lambda:self.openpage("style")
               ).grid(row=1, column=5, padx=5, pady=5)
        return main
        #frame post-login

    def addArtistPage(self):
        artist = Frame(self.main)
        name=StringVar()
        dob=StringVar()
        addl_info=StringVar()
        Label(artist, text="Add Artist Values Below"
              ).grid(row=0, column=0, columnspan=2)
        Label(artist, text="Name:"
              ).grid(row=1, column=0, sticky=E, pady=5)
        Entry(artist, textvariable=name
              ).grid(row=1, column=1, sticky=W, pady=5)
        Label(artist, text="Date of Birth (yyyy/mm/dd):"
              ).grid(row=2, column=0, sticky=E, pady=5)
        Entry(artist, textvariable=dob
              ).grid(row=2, column=1, sticky=W, pady=5)
        Label(artist, text="Additional Information:"
              ).grid(row=3, column=0, sticky=E, pady=5)
        Entry(artist, textvariable=addl_info
              ).grid(row=3, column=1, sticky=W, pady=5)
        Button(artist, text="Add Artist", command=lambda:self.addArtist(name, dob, addl_info)
               ).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        return artist
        #frame add artist

    def addArtist(self, name, dob, addl_info):
        maxid = self.controller.askdb.runQuery("select max(ownerid) from owners")[0][0]
        query = f"Insert into Artist Values ({maxid+3},'{name.get()}','{dob.get()}','{addl_info.get()}');"
        self.controller.askdb.runStatement(query)
        messagebox.showinfo("Success!","Your Artist was added!")
        self.openpage("main")

    def addCollectorPage(self):
        collector = Frame(self.main)
        return collector
        #frame add collector

    def addVenuePage(self):
        venue = Frame(self.main)
        return venue
        #frame add venue

    def addArtworkPage(self):
        artwork = Frame(self.main)
        return artwork
        #frame add artwork

    def addExhibitPage(self):
        exhibit = Frame(self.main)
        return exhibit
        #frame create Exhibit

    def addArtStylePage(self):
        artstyle = Frame(self.main)
        return artstyle
        #frame create art style
