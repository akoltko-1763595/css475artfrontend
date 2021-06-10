from tkinter import *
import sys
import pyodbc
from PIL import ImageTk, Image
import FindArt as art
import FindExhibit as exh
import FindArtist as artist
import AdminActions as admin

class ArtFinder(Tk):
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        Tk.__init__(self, *args, **kwargs)

        self.bind('<Escape>', sys.exit)
        self.title("Seattle Art Finder")

        # creating a container
        self.container = Frame(self)
        self.container.pack(side = "top", fill = "both", expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (Intro, art.FindArtByName, art.FindArtByArtist,
                  exh.FindExhibitByName, exh.FindExhibitByMuseum,
                  artist.FindArtist, admin.AdminPage):
            frame = F(self.container, self)
            self.frames[frame.name] = F

        self.current_frame = None
        self.show_frame("Intro")

        username = ''
        password = ''
        with open('dbpw.txt','r') as pw:
            lines = pw.readlines()
            username = lines[0].strip()
            password = lines[1].strip()

        self.askdb = askDatabase(username, password)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        if self.current_frame is not None:
            self.current_frame.grid_remove()
            self.current_frame.destroy()
        self.current_frame = self.frames[cont](self.container, self)
        self.current_frame.grid(row=0, column=0, sticky="nsew")


class Intro(Frame):
    def __init__(self, root, controller):
        Frame.__init__(self, root)
        self.name = "Intro"

        #title
        photo = ImageTk.PhotoImage(Image.open("Title.jpg"))
        self.title = Label(self, image=photo)
        self.title.image = photo
        self.title.grid(row=0, column=0, columnspan=2)

        #Find an Artwork
        Label(self, text="Looking for a Art Piece?").grid(row=1, column=0, columnspan=2, pady=5)
        Button(self, text="Search by Name", command=lambda:controller.show_frame("FindArtByName")
               ).grid(row=2, column=0, pady=5, padx=5, sticky=E)
        Button(self, text="Search by Artist", command=lambda:controller.show_frame("FindArtByArtist")
               ).grid(row=2, column=1, pady=5, padx=5, sticky=W)

        #Look at Exhibits
        Label(self, text="Looking for an Exhibit?").grid(row=3, column=0,
              columnspan=2, pady=5)
        Button(self, text="Search by Museum",
               command=lambda:controller.show_frame("FindExhibitByMuseum")).grid(
               row=4, column=0, pady=5, padx=5, sticky=E)
        Button(self, text="Search by Exhibit Name", command=lambda:controller.show_frame("FindExhibitByName")
               ).grid(row=4, column=1, pady=5, padx=5, sticky=W)

        #Find an Artist
        Label(self, text="Looking for an Artist?").grid(row=5, column=0, columnspan=2, pady=5)
        Button(self, text="Find an Artist", command=lambda:controller.show_frame("FindArtist")
               ).grid(row=6, column=0, columnspan=2, pady=5)
        Button(self, text="I'm an Editor", command=lambda:controller.show_frame("AdminPage")
               ).grid(row=6, column=1, sticky=E, padx=5, pady=5)


class askDatabase():
    def __init__(self, u, p):
        server = 'seattleart.cjhbuvf3dom6.us-west-2.rds.amazonaws.com,1433'
        database = 'SeattleArt'
        cnxnstr = 'DRIVER={ODBC Driver 17 for SQL Server};'
        cnxnstr += 'SERVER='+server+';'
        cnxnstr += 'DATABASE='+database+';'
        cnxnstr += 'UID='+u+';PWD='+p+';'
        self.cnxn = pyodbc.connect(cnxnstr)
        self.cursor = self.cnxn.cursor()

    def runQuery(self, query):
        try:
            rows = self.cursor.execute(query).fetchall()
            return rows
        except:
            print(query)
            sys.exit(1)

    def runStatement(self, stmt):
        try:
            self.cursor.execute(stmt)
            self.cnxn.commit()
        except:
            print(stmt)
            sys.exit(1)


if __name__ == '__main__':
    app = ArtFinder()
    app.mainloop()
