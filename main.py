#Import Tkinker
from tkinter import *
from PIL import ImageTk, Image

# Variables for User
hp = 0
att = 0
xp = 0
inventory = []

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

    # Error Message (Boundary testing)
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=65, y=350)

  # Name Collection
  def name_collection(self):
    name = self.entry_box.get()
    if len(name) <=20 and len(name) >=3:
      print(name)
      self.game_frame.destroy()
      Scenario1(root)
    else:
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

    # Error Message (Boundary testing)
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

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
    # Boundary testing
    else:
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

    # Error Message
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)
  
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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)
      
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

    # Error Message
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)
      
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

    # Error Message
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)
      
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
      self.error_label.config(text = "Please select an option")

# SD Response 1
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

    # Error Message
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)
      
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
      self.error_label.config(text = "Please select an option")

# SD Response 2
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

    # Error Message
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)
      
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

    # Error Message
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

  # Class Buffs
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      global hp
      global att
      global inventory
      hp = hp + 120
      att = att + 10
      inventory.append("Short Sword and Metal Shield")
      self.game_frame.destroy()
      Scenario6(root)
    elif choice == 2:
      hp = hp + 100
      att = att + 20
      inventory.append("A black hood, leather armour and a few daggers")
      self.game_frame.destroy()
      Scenario6(root)
    elif choice == 3:
      hp = hp + 80
      att = att + 50
      inventory.append("A book full of arcane spells and incantations")
      self.game_frame.destroy()
      Scenario6(root)
    else:
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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)
      
    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      global inventory
      inventory.append("""
      Blue Healing Potion""")
      self.game_frame.destroy()
      Scenario7(root)
    elif choice == 2:
      inventory.append("""
      Red Power Potion""")
      self.game_frame.destroy()
      Scenario7(root)
    else:
      self.error_label.config(text = "Please select an option")

# Second Dialogue
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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario9(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario13(root)
    else:
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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario15(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario16(root)
    else:
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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

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

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=220, y=350)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      combat1(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario1(root)
    else:
      self.error_label.config(text = "Please select an option")

# Combat 1
class combat1:
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
    self.hp = Label(self.game_frame, text = hp, font=("Skia", "12", "bold"), bg="#666666", fg="white")
    self.hp.place(x=122, y=123)

    # XP
    self.xp = Label(self.game_frame, text = xp, font=("Skia", "12", "bold"), bg="#666666", fg="white")
    self.xp.place(x=315, y=123)

    # Attack
    self.attack = Label(self.game_frame, text = att, font=("Skia", "12", "bold"), bg="#666666", fg="white")
    self.attack.place(x=500, y=123)

    # Inventory
    self.inventory = Label(self.game_frame, text = inventory, font=("Skia", "6", "bold"), bg="#666666", fg="white")
    self.inventory.place(x=298, y=220)

    # Option 1
    self.rb1 = Radiobutton(self.game_frame, value=1, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb1.place(x=30, y=182)

    # Option 2
    self.rb2 = Radiobutton(self.game_frame, value=2, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb2.place(x=30, y=252)

    # Option 2
    self.rb3 = Radiobutton(self.game_frame, value=3, padx=14, pady=18, bg="grey50", variable=self.var1)
    self.rb3.place(x=30, y=322)

    # Confirm Button
    self.game_instance = Button(self.game_frame, text="Confirm", font=("Skia", "12", "bold"), bg="grey70", fg="white", command=self.test_program)
    self.game_instance.place(x=465, y=340)

    # Error Message 
    self.error_label = Label(self.game_frame, font=("Skia", "10"), bg="#272727", fg="red")
    self.error_label.place(x=285, y=345)

    # Different Scenarios
  def test_program(self):
    choice = self.var1.get()
    if choice == 1:
      self.game_frame.destroy()
      Scenario1(root)
    elif choice == 2:
      self.game_frame.destroy()
      Scenario1(root)
    else:
      self.error_label.config(text = "Please select an option")

# Start of program
if __name__ == "__main__":
  root = Tk() # Creating a window
  root.title("Ninkendo Games")
  game_instance = GameStarter(root) # Object calls the Class
  root.mainloop() # Keep looping so window stays on