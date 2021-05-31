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
        self.bg_image = self.bg_image.resize((600, 300), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        # Create the Frame
        # Imports code fro tkinker (Frame)
        # self.(can be named anything)
        self.game_frame = Frame(parent, bg = background_color)
        # Organizes widgets in a table in the parent widge
        self.game_frame.grid()

        self.image_label = Label(self.game_frame, image = self.bg_image)
        self.image_label.grid(row=1)

        # Create the entry box
        self.entry_box = Entry(self.game_frame)
        self.entry_box.place(x=160, y=245)

        # Create a Button
        self.continue_button = Button(self.game_frame, text="Enter", bg="skyblue", font=("Roman"), command=self.name_collection)
        self.continue_button.place(x=370, y=240)

    # When user types name it goes here
    def name_collection(self):
        # Assigned to name
        name = self.entry_box.get()
        # Adds name to list
        print(name)
        self.game_frame.destroy()
        Game(root)


class Game:
  def __init__(self, parent):

    background_color = "Grey30"
    self.game_frame = Frame(parent, bg = background_color, padx=245, pady=65)
    self.game_frame.grid()

    self.question_label = Label(self.game_frame, font=("Tw Cen MT", "16"), bg=background_color)
    self.question_label.grid(row=1, padx=10, pady=10)

    self.var1 = IntVar()

    self.rb1 = Radiobutton(self.game_frame, text="Get out of bed", font=("Skia","12"), bg=background_color, value=1, padx=10, pady=10, variable=self.var1, indicator = 0, background = "skyblue")
    self.rb1.grid(row=2, sticky=W)

    self.rb2 = Radiobutton(self.game_frame, text="Sleep in for five more minutes", font=("Roman","12"), bg=background_color, value=1, padx=10, pady=10, variable=self.var1, indicator = 0, background = "skyblue")
    self.rb2.grid(row=3, sticky=W)

    self.rb3 = Radiobutton(self.game_frame, font=("Helvetica","12"), bg=background_color, value=1, padx=10, pady=10, variable=self.var1, indicator = 0, background = "skyblue")
    self.rb1.grid(row=4, sticky=W)

    self.game_instance = Button(self.game_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="whitesmoke")
    self.game_instance.grid(row=8, padx=5, pady=1)

    self.score_label = Label(self.game_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_color)
    self.score_label.grid(row=8, padx=10, pady=1)


# Start of program
if __name__ == "__main__":
  root = Tk() # Creating a window
  root.title("Ninkendo Games")
  game_instance = GameStarter(root) # Object calls the Class
  root.mainloop() # Keep looping so window stays on