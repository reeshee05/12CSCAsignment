# Import Tkinker
from tkinter import *
import random
from PIL import ImageTk, Image

# Variables for User
names = []
hp = 0 # User Health Points
att = 0 # User Attack Value
xp = 0 # Use Experience Points
tries = 2 # User lives for Interrogation
gear = [] # User Gear
inventory = [] # User Inventory

# Variables for Assassin
ass_hp = 50 # Assassin Health Points 
ass_att = 7 # Assassin Attack Value

# Variables for Final Boss
b_hp = 300 # Final Boss Health Points
b_att = 31 # Final Boss Attack Value


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
    self.image_label.grid(row = 1)

    # Entry box
    self.entry_box = Entry(self.game_frame)
    self.entry_box.place(x = 160, y = 300)

    # Button
    self.continue_button = Button(self.game_frame, text = "Enter", bg = "grey70", font = ("Skia"), command = self.name_collection)
    self.continue_button.place(x = 370, y = 295)

    # Key Press
    def key_pressed(event):
      if event.keycode == 36:
        self.name_collection()

    self.entry_box.bind("<Key>",key_pressed)

    # Error Message (Boundary testing)
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 67, y = 350)

  # Name Collection
  def name_collection(self):
    name = self.entry_box.get()
    if len(name) <= 20 and len(name) >= 3:
      names.append(name)
      self.game_frame.destroy()
      Scenario1(root)
    else:
      # Error Message
      self.error_label.config(text = "Please enter a name which has a min of 3 letters and max of 20 letters.")


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
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 133)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 198)

    # Option 3
    self.rb3 = Radiobutton(self.game_frame, value = 3, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb3.place(x = 30, y = 264)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message (Boundary testing)
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

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
      # Error Message
      self.error_label.config(text = "Please select an option")


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
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)
  
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario10(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario10(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


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
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)
      
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario10(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario10(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


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
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)
      
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario10(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario10(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Second Dialogue (SD)
class Scenario10:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s10.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)
      
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario11(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario12(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# (SD) Response 1
class Scenario11:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s11.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)
      
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario5(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario5(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# (SD) Response 2
class Scenario12:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s12.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)
      
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario5(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario5(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Character Class Selection
class Scenario5:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s5.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 133)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 198)

    # Option 3
    self.rb3 = Radiobutton(self.game_frame, value = 3, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb3.place(x = 30, y = 264)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

  # Class Buffs
  def test_program(self):
    choice = self.var1.get()
    if choice == 1: # User chooses sword and shield
      global hp
      global att
      global gear
      hp = hp + 120
      att = att + 30
      gear.append("Short Sword and Metal Shield")
      self.game_frame.destroy()
      Scenario6(root)
    elif choice == 2: # User chooses black hood, leather armour and daggers
      hp = hp + 80
      att = att + 40
      gear.append("A black hood, leather armour and a few daggers")
      self.game_frame.destroy()
      Scenario6(root)
    elif choice == 3: # User chooses spells 
      hp = hp + 60
      att = att + 60
      gear.append("A book full of arcane spells and incantations")
      self.game_frame.destroy()
      Scenario6(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Inventory Selection
class Scenario6:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s6.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x=465, y=340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)
      
  # Potion Selection
  def test_program(self):
    choice = self.var1.get()
    if choice == 1: # User chooses Healing Potion
      global inventory
      inventory.append("Red Healing Potion")
      self.game_frame.destroy()
      Scenario7(root)
    elif choice == 2: # User chooses Power Potion
      inventory.append("Blue Power Potion")
      self.game_frame.destroy()
      Scenario7(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Third Dialogue
class Scenario7:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s7.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario8(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario8(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Entering the Town
class Scenario8:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s8.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      global xp
      xp = xp + 100
      self.game_frame.destroy()
      Scenario9(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario13(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Moving Closer
class Scenario9:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s9.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario14(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario16(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Asks Stranger
class Scenario13:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s13.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      global xp
      xp = xp + 100
      self.game_frame.destroy()
      Scenario14(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario16(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Listens to Speech (#1)
class Scenario14:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s14.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      global xp
      xp = xp + 999
      self.game_frame.destroy()
      Scenario15(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario16(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Listens to Speech (#2)
class Scenario15:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s15.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 335)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario16(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario16(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")

# Assasination
class Scenario16:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s16.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Combat1(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario18(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Attack hits and user wins
class AWin:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("a_win.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # You gained XP
    self.experience = Label(self.game_frame, text = "You Gained XP", font = ("Skia", "10"), bg = "#272727", fg = "pale green")
    self.experience.place(x = 255, y = 365)

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

  # Goes back to Combat1
  def test_program(self):
    self.game_frame.destroy()
    Scenario17(root)


# Attack hit but Enemy Still Alive
class AOn:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("a_on.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # You gained XP
    self.experience = Label(self.game_frame, text = "You Gained XP", font = ("Skia", "10"), bg = "#272727", fg = "pale green")
    self.experience.place(x = 255, y = 365)

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

  # Goes back to Combat1
  def test_program(self):
    self.game_frame.destroy()
    Combat1(root)


# Attack Miss
class ALoss:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("a_loss.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

  # Different Scenarios
  def test_program(self):
    if (hp <= 0):
      self.game_frame.destroy()
      Death(root)
    else:
      self.game_frame.destroy()
      Combat1(root)


# Defence Successful
class DOn:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("d_on.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # You gained XP
    self.experience = Label(self.game_frame, text = "You Gained XP", font = ("Skia", "10"), bg = "#272727", fg = "pale green")
    self.experience.place(x = 255, y = 365)

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

    # Goes back to Combat1
  def test_program(self):
      self.game_frame.destroy()
      Combat1(root)


# Defence Failure
class DLoss:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("d_loss.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

    # Different Scenarios
  def test_program(self):
    if (hp <= 0):
      self.game_frame.destroy()
      Death(root)
    else:
      self.game_frame.destroy()
      Combat1(root)


# Combat 1
class Combat1:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("combat1.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row=1)

    self.var1 = IntVar()

    # HP
    self.hp = Label(self.game_frame, text = hp, font = ("Skia", "12", "bold"), bg = "#666666", fg = "white")
    self.hp.place(x = 110, y = 123)

    # Attack
    self.attack = Label(self.game_frame, text = att, font = ("Skia", "12", "bold"), bg = "#666666", fg = "white")
    self.attack.place(x = 250, y = 123)

    # XP
    self.xp = Label(self.game_frame, text = xp, font = ("Skia", "12", "bold"), bg = "#666666", fg = "white")
    self.xp.place(x = 370, y = 123)

    # Enemy HP
    self.enemy_hp = Label(self.game_frame, text = ass_hp, font = ("Skia", "12", "bold"), bg = "#666666", fg = "red4")
    self.enemy_hp.place(x = 490, y = 136)

    # Gear
    self.gear = Label(self.game_frame, text = gear, font = ("Skia", "6", "bold"), bg = "#666666", fg = "white")
    self.gear.place(x = 298, y = 235)

    # Inventory
    self.inventory = Label(self.game_frame, text = inventory, font = ("Skia", "6", "bold"), bg = "#666666", fg = "white")
    self.inventory.place(x = 298, y = 220)

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 182)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 252)

    # Option 2
    self.rb3 = Radiobutton(self.game_frame, value = 3, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb3.place(x = 30, y = 322)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Potion Error Message
    self.error_potion = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_potion.place(x = 285, y = 345)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 285, y = 345)

  # Different Scenarios / Calculations
  def test_program(self):
    choice = self.var1.get()
    if choice == 1: # Attack the Enemy
      if random.randint(0,100) <= 80:
        global hp
        global xp
        global ass_hp
        global att
        ass_hp = ass_hp - att
        if (ass_hp <=0):
          xp = xp + 999
          self.game_frame.destroy()
          AWin(root) # Attack hits and kills Enemy
        elif (ass_hp >=1):
          xp = xp + 499
          self.game_frame.destroy()
          AOn(root) # Attack hits but the Enemy is still alive
      else:
        hp = hp - ass_att
        self.game_frame.destroy()
        ALoss(root) # Attack misses
    elif choice == 2: # Defend agaisnt the Enemy
      if random.randint(0,100) <= 66:
        xp = xp + 1999
        self.game_frame.destroy()
        DOn(root) # Successfully defends against the Enemy
      else:
        hp = hp - ass_att
        self.game_frame.destroy()
        DLoss(root) # Fails to defend against the Enemy
    elif choice == 3: # Use a potion
      global inventory
      if "Blue Power Potion" in inventory: # Increases Att
        att = att + 50
        inventory.remove("Blue Power Potion")
        self.game_frame.destroy()
        Combat1(root)
      elif "Red Healing Potion" in inventory: # Increases HP
        hp = hp + 100
        inventory.remove("Red Healing Potion")
        self.game_frame.destroy()
        Combat1(root)
      elif "Blue Power Potion" or "Red Healing Potion" not in inventory:
        self.error_potion.config(text = "You already used this")
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Talking to Guards after battle (TGB)
class Scenario17:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s17.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario19(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario25(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")


# Talking to Guards after fleeing (TGF)
class Scenario18:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s18.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario20(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario25(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# (TGF) Response 1
class Scenario19:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s19.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario20(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario25(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Interrogation
class Scenario20:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s20.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario21(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario21(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# First Question
class Scenario21:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s21.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 133)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 198)

    # Option 3
    self.rb3 = Radiobutton(self.game_frame, value = 3, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb3.place(x = 30, y = 264)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x = 220, y = 350)

  # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1: # User gets answer right
      self.game_frame.destroy()
      Scenario22(root)
    elif choice == 2: # User gets answer wrong
      global tries
      tries = tries - 1
      self.game_frame.destroy()
      Scenario22(root)
    elif choice == 3: # User gets answer wrong
      tries = tries - 1      
      self.game_frame.destroy()
      Scenario22(root)
    else:
      # Error Message
      self.error_label.config(text = "Please select an option")
  

# Second Question
class Scenario22:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s22.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 133)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x=30, y=198)

    # Option 3
    self.rb3 = Radiobutton(self.game_frame, value = 3, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb3.place(x = 30, y = 264)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message (Boundary testing)
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

  # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1: # User gets answers wrong
      global tries
      tries = tries - 1
      if (tries <= 0):
        self.game_frame.destroy()
        Death(root) 
      else:
        self.game_frame.destroy()
        Scenario23(root)
    elif choice == 2: # User gets answers wrong
      tries = tries - 1
      if (tries <= 0):
        self.game_frame.destroy()
        Death(root)
      else:
        self.game_frame.destroy()
        Scenario23(root)
    elif choice == 3: # User gets answers right
      self.game_frame.destroy()
      Scenario23(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Third Question
class Scenario23:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s23.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 133)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 198)

    # Option 3
    self.rb3 = Radiobutton(self.game_frame, value = 3, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb3.place(x = 30, y = 264)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

  # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1: # User gets answers wrong
      global tries
      tries = tries - 1
      if (tries <= 0):
        self.game_frame.destroy()
        Death(root)
      else:
        global xp
        xp = xp + 1999
        self.game_frame.destroy()
        Scenario24(root)
    elif choice == 2: # User gets answers right
      xp = xp + 1999
      self.game_frame.destroy()
      Scenario24(root)
    elif choice == 3: # User gets answers wrong
      tries = tries - 1
      if (tries <= 0):
        self.game_frame.destroy()
        Death(root)
      else:
        xp = xp + 1999
        self.game_frame.destroy()
        Scenario24(root)
    else:
      self.error_label.config(text = "Please select an option")

# Leaving Interrogation
class Scenario24:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s24.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 335)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario25(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario25(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Entering Final Boss Lair
class Scenario25:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s25.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario26(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario26(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Boss Dialogue (BD)
class Scenario26:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s26.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x=30, y=159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario27(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario28(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# (BD) Response 1
class Scenario27:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s27.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

  # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario29(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario29(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# (DB) Response 2
class Scenario28:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s28.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario29(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario29(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# I Am Your Father Line
class Scenario29:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s29.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      BadEnd1(root)
    elif choice == 2:
      self.game_frame.destroy()
      global xp
      xp = xp + 999
      Scenario30(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Final Boss Fight Begins
class Scenario30:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s30.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 335)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Combat2(root)
    elif choice == 2:
      self.game_frame.destroy()
      Combat2(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Attack Hits and Win
class AWin2:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("a_win.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # You gained XP
    self.experience = Label(self.game_frame, text = "You Gained XP", font = ("Skia", "10"), bg = "#272727", fg = "pale green")
    self.experience.place(x = 255, y = 365)

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

  # Return to Combat 2
  def test_program(self):
    self.game_frame.destroy()
    Combat2(root)


# Attack But Still Alive
class AOn2:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("a_on.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # You gained XP
    self.experience = Label(self.game_frame, text = "You Gained XP", font = ("Skia", "10"), bg = "#272727", fg = "pale green")
    self.experience.place(x = 255, y = 365)

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

  # Return to Combat 2
  def test_program(self):
    self.game_frame.destroy()
    Combat2(root)


# Attack Miss
class ALoss2:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("a_loss.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

  # Different Scenarios
  def test_program(self):
    if (hp <= 0):
      self.game_frame.destroy()
      Death(root)
    else:
      self.game_frame.destroy()
      Combat2(root)


# Defence Win
class DOn2:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("d_on.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # You gained XP
    self.experience = Label(self.game_frame, text = "You Gained XP", font = ("Skia", "10"), bg = "#272727", fg = "pale green")
    self.experience.place(x = 255, y = 365)

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

  # Different Scenarios
  def test_program(self):
    self.game_frame.destroy()
    Combat2(root)


# Defence Loss
class DLoss2:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("d_loss.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Continue Button
    self.game_instance = Button(self.game_frame, text = "Continue", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 250, y = 320)

  # Different Scenarios
  def test_program(self):
    if (hp <= 0):
      self.game_frame.destroy()
      Death(root)
    else:
      self.game_frame.destroy()
      Combat2(root)


# Final Boss Battle
class Combat2:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("combat1.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # HP
    self.hp = Label(self.game_frame, text = hp, font = ("Skia", "12", "bold"), bg = "#666666", fg = "white")
    self.hp.place(x = 110, y = 123)

    # Attack
    self.attack = Label(self.game_frame, text = att, font = ("Skia", "12", "bold"), bg = "#666666", fg = "white")
    self.attack.place(x = 250, y = 123)

    # XP
    self.xp = Label(self.game_frame, text = xp, font = ("Skia", "12", "bold"), bg = "#666666", fg = "white")
    self.xp.place(x = 370, y = 123)

    # Enemy HP
    self.enemy_hp = Label(self.game_frame, text = b_hp, font = ("Skia", "12", "bold"), bg = "#666666", fg = "red4")
    self.enemy_hp.place(x = 490, y = 136)

    # Gear
    self.gear = Label(self.game_frame, text = gear, font = ("Skia", "6", "bold"), bg = "#666666", fg = "white")
    self.gear.place(x = 298, y = 235)

    # Inventory
    self.inventory = Label(self.game_frame, text = inventory, font = ("Skia", "6", "bold"), bg = "#666666", fg = "white")
    self.inventory.place(x = 298, y = 220)

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 182)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 252)

    # Option 2
    self.rb3 = Radiobutton(self.game_frame, value = 3, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb3.place(x = 30, y = 322)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Potion Error Message
    self.error_potion = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_potion.place(x = 285, y = 345)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 285, y = 345)

    # Different Scenarios / Calculations
  def test_program(self):
    choice = self.var1.get()
    if choice == 1: # Attack Enemy
      if random.randint(0,100) <= 65:
        global hp
        global xp
        global att
        global b_hp
        global b_att
        b_hp = b_hp - att
        if (b_hp <= 0):
          xp = xp + 1999
          self.game_frame.destroy()
          AWin2(root) # Attack kills enemy
        elif (b_hp >= 1):
          xp = xp + 999
          self.game_frame.destroy()
          AOn2(root) # Attack successfully hits enemy 
      else:
        hp = hp - b_att
        self.game_frame.destroy()
        ALoss2(root) # Attack misses enemy
    elif choice == 2: # Defend against enemy
      if random.randint(0,100) <= 55:
        xp = xp + 2999
        self.game_frame.destroy()
        DOn2(root) # Successfully Defends against enemy
      else:
        hp = hp - b_att
        self.game_frame.destroy()
        DLoss2(root) # Fails to defend agaisnt enemy
    elif choice == 3: # Use Potions
      global inventory
      if "Blue Power Potion" in inventory: # Increase att
        att = att + 50
        inventory.remove("Blue Power Potion")
        self.game_frame.destroy()
        Combat2(root)
      elif "Red Healing Potion" in inventory: # Increase HP
        hp = hp + 100
        inventory.remove("Red Healing Potion")
        self.game_frame.destroy()
        Combat2(root)
      elif "Blue Power Potion" or "Red Healing Potion" not in inventory:
        self.error_potion.config(text = "You already used this")
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")

# Win against Final Boss
class Scenario31:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s31.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario32(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario33(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Final Dialogue from Boss
class Scenario32:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s32.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      GoodEnd(root)
    elif choice == 2:
      self.game_frame.destroy()
      GoodEnd(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Destroy or Keeping the Eye of Morgoth
class Scenario33:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("s33.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value = 1, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb1.place(x = 30, y = 159)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value = 2, padx = 14, pady = 18, bg = "grey50", variable = self.var1)
    self.rb2.place(x = 30, y = 251)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text = "Confirm", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 465, y = 340)

    # Error Message 
    self.error_label = Label(self.game_frame, font = ("Skia", "10"), bg = "#272727", fg = "red")
    self.error_label.place(x = 220, y = 350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      BadEnd2(root)
    elif choice == 2:
      self.game_frame.destroy()
      GoodEnd(root)
    # Error Message
    else:
      self.error_label.config(text = "Please select an option")


# Death and Player loses
class Death:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("death.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # XP Readings
    self.xp_readings = Label(self.game_frame, text = "Your final XP is", font = ("Skia", "20", "bold"), bg = "#666666", fg = "pale green", width = "13")
    self.xp_readings.place(x = 115, y = 250)

    # XP
    self.xp = Label(self.game_frame, text = xp, font = ("Skia", "20", "bold"), bg = "#666666", fg = "pale green", width = "8")
    self.xp.place(x = 395, y = 250)

    # Exit Button
    self.game_instance = Button(self.game_frame, text = "Exit", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 500, y = 340)

  # End Program
  def test_program(self):
    self.game_frame.destroy()
    root.destroy()


# Good Ending
class GoodEnd:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("good_end.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # XP Readings
    self.xp_readings = Label(self.game_frame, text = "Your final XP is", font = ("Skia", "20", "bold"), bg = "#666666", fg = "pale green", width = "13")
    self.xp_readings.place(x = 115, y = 250)

    # XP
    self.xp = Label(self.game_frame, text = xp, font = ("Skia", "20", "bold"), bg = "#666666", fg = "pale green", width = "8")
    self.xp.place(x = 395, y = 250)

    # Exit Button
    self.game_instance = Button(self.game_frame, text = "Exit", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 500, y = 340)

  # End Credits
  def test_program(self):
    self.game_frame.destroy()
    EndCredits(root)


# Bad Ending 1
class BadEnd1:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("bad_end1.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # XP Readings
    self.xp_readings = Label(self.game_frame, text = "Your final XP is", font = ("Skia", "20", "bold"), bg = "#666666", fg = "pale green", width = "13")
    self.xp_readings.place(x = 115, y = 250)

    # XP
    self.xp = Label(self.game_frame, text = xp, font = ("Skia", "20", "bold"), bg = "#666666", fg = "pale green", width = "8")
    self.xp.place(x = 395, y = 250)

    # Exit Button
    self.game_instance = Button(self.game_frame, text = "Exit", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 500, y = 340)

  # End Credits
  def test_program(self):
    self.game_frame.destroy()
    EndCredits(root)


# Bad Ending 2
class BadEnd2:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("bad_end2.jpg")
    self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # XP Readings
    self.xp_readings = Label(self.game_frame, text = "Your final XP is", font = ("Skia", "20", "bold"), bg = "#666666", fg = "pale green", width = "13")
    self.xp_readings.place(x = 115, y = 250)

    # XP
    self.xp = Label(self.game_frame, text = xp, font = ("Skia", "20", "bold"), bg = "#666666", fg = "pale green", width = "8")
    self.xp.place(x = 395, y = 250)

    # Exit Button
    self.game_instance = Button(self.game_frame, text = "Exit", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 500, y = 340)

  # End Credits
  def test_program(self):
    self.game_frame.destroy()
    EndCredits(root)


# End Credits
class EndCredits:
  def __init__(self, parent):

    # Image Background
    self.bg_image = Image.open("credits.jpg")
    self.bg_image = self.bg_image.resize((250, 320), Image.ANTIALIAS)
    self.bg_image = ImageTk.PhotoImage(self.bg_image)

    self.game_frame = Frame(parent)
    self.game_frame.grid()

    # Background Image Location
    self.image_label = Label(self.game_frame, image = self.bg_image)
    self.image_label.grid(row = 1)

    self.var1 = IntVar()

    # Exit Button
    self.game_instance = Button(self.game_frame, text = "Exit", font = ("Skia", "12", "bold"), bg = "grey70", fg = "white", command = self.test_program)
    self.game_instance.place(x = 100, y = 252)

  # End Program
  def test_program(self):
    self.game_frame.destroy()
    root.destroy()


# Start of program
if __name__ == "__main__":
  root = Tk() # Creating a window
  root.title("Ninkendo Games")
  game_instance = GameStarter(root) # Object calls the Class
  root.mainloop() # Keep looping so window stays on