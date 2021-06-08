from tkinter import *
import sys
from PIL import ImageTk, Image
import FindArt as art
import FindExhibit as exh
import FindArtist as artist

class ArtFinder(Tk):
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        Tk.__init__(self, *args, **kwargs)

        self.bind('<Escape>', sys.exit)
        self.title("Seattle Art Finder")

        # creating a container
        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Intro, art.FindArtByName, art.FindArtByArtist,
                  exh.FindExhibitByName, exh.FindExhibitByMuseum,
                  artist.FindArtist):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[frame.name] = frame

        self.current_frame = "Intro"
        self.show_frame("Intro")

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        self.frames[self.current_frame].grid_remove()
        self.frames[cont].grid(row=0, column=0, sticky="nsew")
        self.current_frame = cont


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


if __name__ == '__main__':
    app = ArtFinder()
    app.mainloop()
