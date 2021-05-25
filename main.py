#Import Tkinker
from tkinter import *
import random
from PIL import ImageTk, Image

names = []
global questions_answers
XP = 0
questions_answers = {
# Key & Value
  1 : ["In a cabin somewhere in the woods... You wake up, what do you do?",
       "Go Outside",
       "Check Stats",
       "Check Inventory",
       "Same",
       2],
  2 : ["Hello There! My name is Cedric at yer service",
        "Who are you again?",
        "Oh I remember you... you were dyslexic guy",
        "Stare at him",
        "Same",
       3],
  3 : ["The town is on Fire!",
        "Walk Away",
        "Play Dead",
        "Run into the blaze",
        "Help the people",
        "Same",
       4],
}

def randomiser():
  global qnum
  qnum = random.randint(1,3)
  if qnum not in names:
    names.append(qnum)
  elif qnum in names:
    ramdomiser()

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
        self.quiz_frame = Frame(parent, bg = background_color)
        # Organizes widgets in a table in the parent widge
        self.quiz_frame.grid()

        self.image_label = Label(self.quiz_frame, image = self.bg_image)
        self.image_label.grid(row=1)

        # Create the entry box
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=1)

        # Create a Button
        self.continue_button = Button(self.quiz_frame, text="Enter", bg="skyblue", command=self.name_collection)
        self.continue_button.grid(row=2)

    # When user types name it goes here
    def name_collection(self):
        # Assigned to name
        name = self.entry_box.get()
        # Adds name to list
        names.append(name)
        print(names)
        self.quiz_frame.destroy()
        Quiz(root)

def name_collection(self):
  name = self.entry_box.get()
  names.append(name)
  self.quiz_frame.destroy()
  Quiz(root)

class Game:
  def __init__(self,parent):

    background_color="Grey30"
    self.game_frame=Frame(parent, bg = background_color, padx=40, pady=40)
    self.game_frame.grid()

    self.question_label=Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT", "16"), bg=background_color)
    self.question_label.grid(row=1, padx=10, pady=10)

    self.var1 = IntVar()

    self.rb1 = Radiobutton(self.game_frame, text=questions_answers[qnum][1], font=("Helvetica","12"), bg=background_color, value=1, padx=10, pady=10, variable=self.var1, indicator = 0, background = "skyblue")
    self.rb1.grid(row=2, sticky=W)

    self.rb2 = Radiobutton(self.game_frame, text=questions_answers[qnum][2], font=("Helvetica","12"), bg=background_color, value=1, padx=10, pady=10, variable=self.var1, indicator = 0, background = "skyblue")
    self.rb2.grid(row=3, sticky=W)

    self.rb3 = Radiobutton(self.game_frame, text=questions_answers[qnum][3], font=("Helvetica","12"), bg=background_color, value=1, padx=10, pady=10, variable=self.var1, indicator = 0, background = "skyblue")
    self.rb1.grid(row=4, sticky=W)

    self.game_instance = Button(self.game_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="whitesmoke")
    self.game_instance.grid(row=8, padx=5, pady=1)

    self.score_label=Label(self.game_frame, text="SCORE", font=("Tw Cen MT", "16"), bg=background_color)
    self.score_label.grid(row=8, padx=10, pady=1)


# Start of program
randomiser()
if __name__ == "__main__":
  root = Tk() # Creating a window
  root.title("Ninkendo Games")
  game_instance = GameStarter(root) # Object calls the Class
  root.mainloop() # Keep looping so window stays on
