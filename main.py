#Import Tkinker
from tkinter import *
from PIL import ImageTk, Image

# Title Page
class GameStarter:
  def __init__(self, parent):
        
    # Image Background
    self.bg_image = Image.open("title_image.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)
        
    # Uses Grid Frame
    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row=1)

    # Entry box
    self.entry_box = Entry(self.game_frame)
    self.entry_box.place(x=160, y=300)

    # Button
    self.continue_button = Button(self.game_frame, text="Enter", bg="grey70", font=("Skia"), command=self.name_collection)
    self.continue_button.place(x=370, y=295)

  # Name Collection
  def name_collection(self):
    name = self.entry_box.get()
    print(name)
    self.game_frame.destroy()
    Scenario1(root)

# Opening Dialogue (OD)
class Scenario1:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s1.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row=1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value=1, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb1.place(x=30, y=133)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value=2, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb2.place(x=30, y=198)

    # Option 3
    self.rb3 = Radiobutton(self.game_frame, value=3, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb3.place(x=30, y=264)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text="Confirm", font=("Skia", "12", "bold"), bg="grey70", fg="white", command=self.test_program)
    self.game_instance.place(x=465, y=340)

  # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario2(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario3(root)
    elif choice == 3:
      self.game_frame.destroy()
      Scenario4(root)
    else:

# (OD) Reponse 1 
class Scenario2:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s2.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row=1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value=1, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb1.place(x=30, y=159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value=2, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb2.place(x=30, y=251)

    # Back Button
    self.game_instance = Button(self.game_frame, text="Back", font=("Skia", "12", "bold"), bg="grey70", fg="white", command=self.previous_page)
    self.game_instance.place(x=30, y=340)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text="Confirm", font=("Skia", "12", "bold"), bg="grey70", fg="white")
    self.game_instance.place(x=465, y=340)
    
  # Back_Page
  def previous_page(self):
    self.game_frame.destroy()
    Scenario1(root)

# (OD) Reponse 2
class Scenario3:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s3.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row=1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value=1, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb1.place(x=30, y=159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value=2, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb2.place(x=30, y=251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text="Confirm", font=("Skia", "12", "bold"), bg="grey70", fg="white", command=self.test_program)
    self.game_instance.place(x=465, y=340)
      
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario2(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario3(root)

# (OD) Reponse 3
class Scenario4:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s4.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row=1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value=1, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb1.place(x=30, y=159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value=2, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb2.place(x=30, y=251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text="Confirm", font=("Skia", "12", "bold"), bg="grey70", fg="white", command=self.test_program)
    self.game_instance.place(x=465, y=340)
      
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario2(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario3(root)


# Start of program
if __name__ == "__main__":
  root = Tk() # Creating a window
  root.title("Ninkendo Games")
  game_instance = GameStarter(root) # Object calls the Class
  root.mainloop() # Keep looping so window stays on