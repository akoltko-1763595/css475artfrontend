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
         ).grid(row=2, column=0, pady = 5)
        self.pages = {"login":self.loginPage,
                      "main":self.adminMainPage,
                      "artist":self.addArtistPage,
                      "collector":self.addCollectorPage,
                      "venue":self.addVenuePage,
                      "artwork":self.addArtworkPage,
                      "exhibit":self.addExhibitPage,
                      "exhibitcontents":self.addArtToExhibitPage,
                      "style":self.addArtStylePage}
        self.current_frame = None
        self.openpage("login")
        self.main.grid(row=0, column=0)

    def openpage(self, page):
        for child in self.main.winfo_children():
            child.destroy() #I had to search 'destroy all children' to find this answer
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
        eu = Entry(login, textvariable=u)
        eu.focus()
        eu.grid(column=1, row=1, pady=5, sticky=W)
        Label(login, text="Password:"
        ).grid(row=2, column=0, pady=5, sticky=E)
        e = Entry(login, textvariable=p, show="*")
        e.grid(column=1, row=2, pady=5, sticky=W)
        e.bind("<Return>", lambda x:self.checkLogin(u.get(),p.get()))
        Button(login, text="Log In", command=lambda:self.checkLogin(u.get(),p.get())
         ).grid(row=3, column=0, columnspan=2, pady=5)
        return login

    def checkLogin(self, u, p):
        with open("adminpw.json") as ld:
            logins = json.load(ld)
            if u in logins and logins[u]==p:
                self.openpage("main")
                Button(self, text="Go to Admin Page", command=lambda:self.openpage("main")
                        ).grid(row=1, column=0, pady=5)
            else:
                messagebox.showerror(message="Incorrect Username or Password, Please Try Again")

    def adminMainPage(self):
        main = Frame(self.main)
        Label(main, text="What Would You Like To Do?"
        ).grid(row=0, column=0, columnspan=7, padx=5, pady=5)
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
        Button(main, text="Add Art to an Exhibit", command=lambda:self.openpage("exhibitcontents")
         ).grid(row=1, column=5, padx=5, pady=5)
        Button(main, text="Add an Art Style", command=lambda:self.openpage("style")
         ).grid(row=1, column=6, padx=5, pady=5)
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

    def addArtist(self, name, dob, addl_info):
        maxid = self.controller.askdb.runQuery("select max(ownerid) from owners")[0][0]
        query = f"Insert into Artist Values ({maxid+3},'{name.get()}','{dob.get()}','{addl_info.get()}');"
        self.controller.askdb.runStatement(query)
        messagebox.showinfo("Success!","Your Artist was added!")
        self.openpage("main")

    def addCollectorPage(self):
        collector = Frame(self.main)
        name=StringVar()
        dob=StringVar()
        Label(collector, text="Add Collector Values Below"
        ).grid(row=0, column=0, columnspan=2)
        Label(collector, text="Name:"
        ).grid(row=1, column=0, sticky=E, pady=5)
        Entry(collector, textvariable=name
        ).grid(row=1, column=1, sticky=W, pady=5)
        Label(collector, text="Date of Birth (yyyy/mm/dd):"
        ).grid(row=2, column=0, sticky=E, pady=5)
        Entry(collector, textvariable=dob
        ).grid(row=2, column=1, sticky=W, pady=5)
        Button(collector, text="Add Collector", command=lambda:self.addCollector(name, dob)
         ).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        return collector

    def addCollector(self, name, dob):
        maxid = self.controller.askdb.runQuery("select max(ownerid) from owners")[0][0]
        query = f"Insert into Collector Values ({maxid+3},'{name.get()}','{dob.get()}');"
        self.controller.askdb.runStatement(query)
        messagebox.showinfo("Success!","Your Collector was added!")
        self.openpage("main")

    def addVenuePage(self):
        venue = Frame(self.main)
        name = StringVar()
        hours = StringVar()
        location = StringVar()
        addl_info = StringVar()
        Label(venue, text="Add Venue Values Below"
        ).grid(row=0, column=0, columnspan=2, pady=5)
        Label(venue, text="Name:"
        ).grid(row=1, column=0, pady=5, sticky=E)
        Entry(venue, textvariable=name
        ).grid(row=1, column=1, sticky=W, pady=5)
        Label(venue, text="Hours:"
        ).grid(row=2, column=0, pady=5, sticky=E)
        Entry(venue, textvariable=hours
        ).grid(row=2, column=1, sticky=W, pady=5)
        Label(venue, text="Location:"
        ).grid(row=3, column=0, pady=5, sticky=E)
        Entry(venue, textvariable=location
        ).grid(row=3, column=1, sticky=W, pady=5)
        Label(venue, text="Additional Information:"
        ).grid(row=4, column=0, pady=5, sticky=E)
        Entry(venue, textvariable=addl_info
        ).grid(row=4, column=1, sticky=W, pady=5)
        Button(venue, text="Add Venue", command=lambda:self.addVenue(name, hours, location, addl_info)
         ).grid(row=5, column=0, columnspan=2, pady=5)
        return venue

    def addVenue(self, name, hours, location, addl_info):
        maxid = self.controller.askdb.runQuery("select max(ownerid) from owners")[0][0]
        query = f"Insert into Venue Values ({maxid+3},'{name.get()}','{hours.get()}','{location.get()}','{addl_info.get()}');"
        self.controller.askdb.runStatement(query)
        messagebox.showinfo("Success!","Your Venue was added!")
        self.openpage("main")

    def addArtworkPage(self):
        artwork = Frame(self.main)
        title = StringVar()
        creationdate = StringVar()
        value = StringVar()
        artistid = StringVar()
        size = StringVar()
        material = StringVar()
        addl_info = StringVar()
        venueid = StringVar()
        style = StringVar()
        period = StringVar()
        owner = StringVar()

        Label(artwork, text="Add Artwork Values Below"
        ).grid(row=0, column=0, columnspan=2, pady=5)
        Label(artwork, text="Title:"
        ).grid(row=1, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=title
        ).grid(row=1, column=1, sticky=W, pady=5)
        Label(artwork, text="Creation Date:"
        ).grid(row=2, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=creationdate
        ).grid(row=2, column=1, sticky=W, pady=5)
        Label(artwork, text="Value:"
        ).grid(row=3, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=value
        ).grid(row=3, column=1, sticky=W, pady=5)
        Label(artwork, text="Artist ID:"
        ).grid(row=4, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=artistid
        ).grid(row=4, column=1, sticky=W, pady=5)
        Label(artwork, text="Size:"
        ).grid(row=5, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=size
        ).grid(row=5, column=1, sticky=W, pady=5)
        Label(artwork, text="Material:"
        ).grid(row=6, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=material
        ).grid(row=6, column=1, sticky=W, pady=5)
        Label(artwork, text="Additional Information:"
        ).grid(row=7, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=addl_info
        ).grid(row=7, column=1, sticky=W, pady=5)
        Label(artwork, text="Venue ID:"
        ).grid(row=8, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=venueid
        ).grid(row=8, column=1, sticky=W, pady=5)
        Label(artwork, text="Art Style:"
        ).grid(row=9, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=style
        ).grid(row=9, column=1, sticky=W, pady=5)
        Label(artwork, text="Period:"
        ).grid(row=10, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=period
        ).grid(row=10, column=1, sticky=W, pady=5)
        Label(artwork, text="Owner ID:"
        ).grid(row=11, column=0, pady=5, sticky=E)
        Entry(artwork, textvariable=owner
        ).grid(row=11, column=1, sticky=W, pady=5)
        Button(artwork, text="Create Artwork",
                command=lambda:self.addArtwork(title, creationdate, value, artistid,
                                                  size, material, addl_info, venueid,
                                                  style, period, owner)
        ).grid(row=12, column=0, columnspan=2, pady=5)
        return artwork

    def addArtwork(self, title, creationdate, value, artistid, size, material,
                    addl_info, venueid, style, period, owner):
        query = f"Insert into Artwork values ('{title.get()}','{creationdate.get()}','{value.get()}'"
        query += f",{artistid.get()},'{size.get()}','{material.get()}','{addl_info.get()}',{venueid.get()},'{style.get()}','{period.get()}');"
        #Add in artistID, venueID, and ArtStyle checks.
        #Possibly dynamic? Seems expensive
        #Add in dropdowns? Search functionality? Unless it's cached it's to pricey
        self.controller.askdb.runStatement(query)
        query = f"Insert into art_ownership values ({owner.get()},'{title.get()}','{creationdate.get()}',{artistid.get()});"
        self.controller.askdb.runStatement(query)
        self.openpage("main")

    def addExhibitPage(self):
        exhibit = Frame(self.main)
        name = StringVar()
        description = StringVar()
        start = StringVar()
        end = StringVar()
        venue = StringVar()

        Label(exhibit, text="Add Exhibit Values Below"
        ).grid(row=0, column=0, columnspan=2)
        Label(exhibit, text="Name:"
        ).grid(row=1, column=0, sticky=E, pady=5)
        Entry(exhibit, textvariable=name
        ).grid(row=1, column=1, sticky=W, pady=5)
        Label(exhibit, text="Description:"
        ).grid(row=2, column=0, sticky=E, pady=5)
        Entry(exhibit, textvariable=description
        ).grid(row=2, column=1, sticky=W, pady=5)
        Label(exhibit, text="Start Date (yyyy/mm/dd):"
        ).grid(row=3, column=0, sticky=E, pady=5)
        Entry(exhibit, textvariable=start
        ).grid(row=3, column=1, sticky=W, pady=5)
        Label(exhibit, text="End Date (yyyy/mm/dd):"
        ).grid(row=4, column=0, sticky=E, pady=5)
        Entry(exhibit, textvariable=end
        ).grid(row=4, column=1, sticky=W, pady=5)
        Label(exhibit, text="Venue ID:"
        ).grid(row=5, column=0, sticky=E, pady=5)
        Entry(exhibit, textvariable=venue
        ).grid(row=5, column=1, sticky=W, pady=5)

        Button(exhibit, text="Add Exhibit",
        command=lambda:self.addExhibit(name, description, start, end, venue)
        ).grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        return exhibit
        #frame create Exhibit

    def addExhibit(self, name, desc, start, end, venue):
        query = f"Insert into exhibit values ('{name.get()}','{desc.get()}','{start.get()}','{end.get()}',{venue.get()});"
        self.controller.askdb.runStatement(query)
        for child in self.main.winfo_children():
            child.destroy() #I had to search 'destroy all children' to find this answer
        self.pages["exhibitcontents"](venue.get(), name.get(), start.get()).grid(row=0, column=0)

    def addArtToExhibitPage(self, outvenue='', outname='', outstart=''):
        econtents = Frame(self.main)
        venue = StringVar()
        venue.set(outvenue)
        name = StringVar()
        name.set(outname)
        start = StringVar()
        start.set(outstart)
        title = StringVar()
        date = StringVar()
        artist = StringVar()

        Label(econtents, text="Add Art and Exhibit Values Below"
        ).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        Label(econtents, text="Venue ID:"
        ).grid(row=1, column=0, pady=5, sticky=E)
        Entry(econtents, textvariable=venue
        ).grid(row=1, column=1, pady=5, sticky=W)
        Label(econtents, text="Exhibit Name:"
        ).grid(row=2, column=0, pady=5, sticky=E)
        Entry(econtents, textvariable=name
        ).grid(row=2, column=1, pady=5, sticky=W)
        Label(econtents, text="Start Date:"
        ).grid(row=3, column=0, pady=5, sticky=E)
        Entry(econtents, textvariable=start
        ).grid(row=3, column=1, pady=5, sticky=W)
        Label(econtents, text="Artwork Title:"
        ).grid(row=4, column=0, pady=5, sticky=E)
        Entry(econtents, textvariable=title
        ).grid(row=4, column=1, pady=5, sticky=W)
        Label(econtents, text="Creation Date:"
        ).grid(row=5, column=0, pady=5, sticky=E)
        Entry(econtents, textvariable=date
        ).grid(row=5, column=1, pady=5, sticky=W)
        Label(econtents, text="Artist ID:"
        ).grid(row=6, column=0, pady=5, sticky=E)
        Entry(econtents, textvariable=artist
        ).grid(row=6, column=1, pady=5, sticky=W)

        Button(econtents, text="Add to Exhibit",
        command=lambda:self.addArtToExhibit(venue, name, start, title, date, artist, False)
        ).grid(row=7, column=0, padx=5, pady=5)
        Button(econtents, text="Add to Exhibit and Continue",
        command=lambda:self.addArtToExhibit(venue, name, start, title, date, artist, True)
        ).grid(row=7, column=1, padx=5, pady=5)
        return econtents

    def addArtToExhibit(self, venue, name, start, title, date, artist, addmore):
        query = f"insert into exhibit_contents values({venue.get()},'{name.get()}','{start.get()}'"
        query += f",'{title.get()}','{date.get()}',{artist.get()});"
        self.controller.askdb.runStatement(query)
        if addmore:
            for child in self.main.winfo_children():
                child.destroy() #I had to search 'destroy all children' to find this answer
            self.pages["exhibitcontents"](venue.get(), name.get(), start.get()).grid(row=0, column=0)
        else:
            self.openpage("main")

    def addArtStylePage(self):
        artstyle = Frame(self.main)

        name = StringVar()
        period = StringVar()
        addl_info = StringVar()

        Label(artstyle, text="Add Art Style Values Below"
        ).grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        Label(artstyle, text="Style Name:"
        ).grid(row=1, column=0, pady=5, sticky=E)
        Entry(artstyle, textvariable=name
        ).grid(row=1, column=1, pady=5, sticky=W)
        Label(artstyle, text="Period:"
        ).grid(row=2, column=0, pady=5, sticky=E)
        Entry(artstyle, textvariable=period
        ).grid(row=2, column=1, pady=5, sticky=W)
        Label(artstyle, text="Additional Information:"
        ).grid(row=3, column=0, pady=5, sticky=E)
        Entry(artstyle, textvariable=addl_info
        ).grid(row=3, column=1, pady=5, sticky=W)

        Button(artstyle, text="Add Art Style", command=lambda:self.addArtStyle(name, period, addl_info)
        ).grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        return artstyle

    def addArtStyle(self, name, period, addl_info):
        query = f"insert into Art_Style values ('{name.get()}','{period.get()}','{addl_info.get()}');"
        self.controller.askdb.runStatement(query)
        self.openpage("main")
