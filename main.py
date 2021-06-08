#Import Tkinker
from tkinter import *
import random
from PIL import ImageTk, Image


# Title Page
class GameStarter:
    def __init__(self, parent):
        
        # Image Background
        self.bg_image = Image.open("title_image.jpg")
        self.bg_image = self.bg_image.resize((600, 300), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        
        self.game_frame = Frame(parent)
        
        # Uses Grid Format
        self.game_frame.grid()

        # Background Image Location
        self.image_label = Label(self.game_frame, image = self.bg_image)
        self.image_label.grid(row=1)

        # Entry box
        self.entry_box = Entry(self.game_frame)
        self.entry_box.place(x=160, y=245)

        # Button
        self.continue_button = Button(self.game_frame, text="Enter", bg="grey70", font=("Roman"), command=self.name_collection)
        self.continue_button.place(x=370, y=240)

    # Name Collection
    def name_collection(self):
        # Assigned to name
        name = self.entry_box.get()
        # Adds name to list
        print(name)
        self.game_frame.destroy()
        Scenario1(root)

# First Scenario
class Scenario1:
  def __init__(self, parent):

    background_color = "Grey30"

    self.game_frame = Frame(parent, bg = background_color, padx=91, pady=4)
    self.game_frame.grid()

    # Description/Question
    self.question_label = Label(self.game_frame, text="In a cabin somewhere in the woods...", font=("Roman", "12"), fg="white", bg = background_color, padx=50, pady=30)
    self.question_label.grid(row=1, padx=10, pady=10)

    self.var1 = IntVar()

    # Button 1
    self.rb1 = Radiobutton(self.game_frame, text="Get out of bed", font=("Skia","10"), bg="grey50", fg="white", value=1, padx=5, pady=5, variable=self.var1, indicator = 0)
    self.rb1.grid(row=2, sticky=W)

    # Button 2
    self.rb2 = Radiobutton(self.game_frame, text="Sleep in for five more minutes", font=("Roman","10"), bg="grey50", fg="white", value=2, padx=5, pady=5, variable=self.var1, indicator = 0)
    self.rb2.grid(row=3, sticky=W)

    # Button 3
    self.rb3 = Radiobutton(self.game_frame, text="Pretend to be dead", font=("Helvetica","10"), bg="grey50", fg="white", value=3, padx=5, pady=5, variable=self.var1, indicator = 0)
    self.rb3.grid(row=4, sticky=W)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text="Confirm", font=("Helvetica", "12", "bold"), bg="grey70", fg="white")
    self.game_instance.grid(row=5, padx=10, pady=10)


class Scenario2:
  def __init__(self, parent):

    background_color = "Grey30"

    self.game_frame = Frame(parent, bg = background_color, padx=91, pady=4)
    self.game_frame.grid()

    self.question_label = Label(self.game_frame, text="In a cabin somewhere in the woods...", font=("Roman", "12"), background="grey70",  padx=50, pady=35)
    self.question_label.grid(row=1, padx=10, pady=10)

    self.var1 = IntVar()

    #Button 1
    self.rb1 = Radiobutton(self.game_frame, text="Get out of bed", font=("Skia","12"), bg=background_color, value=1, padx=10, pady=10, variable=self.var1, indicator = 0, background = "grey70")
    self.rb1.grid(row=2, sticky=W)

    #Button 2
    self.rb2 = Radiobutton(self.game_frame, text="Sleep in for five more minutes", font=("Roman","12"), bg=background_color, value=2, padx=10, pady=10, variable=self.var1, indicator = 0, background = "grey70")
    self.rb2.grid(row=3, sticky=W)

    self.rb3 = Radiobutton(self.game_frame, text="Pretend to be dead", font=("Helvetica","12"), bg=background_color, value=3, padx=10, pady=10, variable=self.var1, indicator = 0, background = "grey70")
    self.rb3.grid(row=4, sticky=W)

    self.game_instance = Button(self.game_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="grey70")
    self.game_instance.grid(row=5, padx=10, pady=10)



# Start of program
if __name__ == "__main__":
  root = Tk() # Creating a window
  root.title("Ninkendo Games")
  game_instance = GameStarter(root) # Object calls the Class
  root.mainloop() # Keep looping so window stays on