#Import Tkinker
from tkinter import *
import random
from PIL import ImageTk, Image



# Set of instructions for creating an object (class)
class GameStarter:
  # The conctructer (init function)
    def __init__(self, parent):

        background_color = "Grey30"

        self.bg_image = Image.open("title_image.jpg")
        self.bg_image = self.bg_image.resize((420, 220), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        # Create the Frame
        # Imports code fro tkinker (Frame)
        # self.(can be named anything)
        self.quiz_frame = Frame(parent, bg = background_color,
        padx=60, pady=10)
        # Organizes widgets in a table in the parent widge
        self.quiz_frame.grid()

        self.image_label = Label(self.quiz_frame, image = self.bg_image)
        self.image_label.grid(row=1)

        # Create the entry box
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=30, pady=60)

        # Create a Button
        self.continue_button = Button(self.quiz_frame, text="Click Here", bg="cyan", command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)

    # When user types name it goes here
    def name_collection(self):
        # Assigned to name
        name = self.entry_box.get()
        # Adds name to list
        names.append(name)
        print(names)
        self.quiz_frame.destroy()
        Quiz(root)


# Start of program
if __name__ == "__main__":
  root = Tk() # Creating a window
  root.title("Ninkendo Games")
  game_instance = GameStarter(root) # Object calls the Class
  root.mainloop() # Keep looping so window stays on