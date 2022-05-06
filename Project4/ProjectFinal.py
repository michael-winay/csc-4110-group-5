import pydoc
from sqlite3 import connect
import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import jsonpickle
import pickle
from PIL import ImageTk, Image
from tkinter import Frame, filedialog
from os.path import exists
import os
import re
from pygame import Cursor
import pyodbc

"""Drink class"""

#improvements:
#added cloud functionality
#fixed major bug in drink selection

#automatic page closure
#dynamic main view
#streamlined input filtering using regex
#ability to edit entries, excluding images

root = tk.Tk()

class Drink:
    def __init__(self, name, recipe, time, server, image_path):
        self.name = name
        self.recipe = recipe
        self.time = time
        self.server = server
        self.image_path = image_path

    def setName(self, name):
        self.name = name

    def setRecipe(self, recipe):
        self.recipe = recipe

    def setTime(self, time):
        self.time = time

    def setServer(self, server):
        self.server = server

    def setImagePath(self, image_path):
        self.image_path = image_path

    def getName(self):
        return self.name

    def getRecipe(self):
        return self.recipe

    def getTime(self):
        return self.time

    def getServer(self):
        return self.server

    def getImagePath(self):
        return self.image_path

def connectDB():
    query='Select * from orders'
    conn = pyodbc.connect(
    'Driver={SQL Server}; Server=( localhost:3306); Database=id18892795_barmaster;Trusted_Connection=yes;'
    )
    cursor = conn.cursor()
    cursor.execute(query)
    for i in cursor:
        print(i)

database = []
logEntries = []

file_exists = exists("database.pickle")
if file_exists:
    pickle_off = open("database.pickle","rb")
    database = jsonpickle.decode(pickle.load(pickle_off))
else:
    pickling_on = open("database.pickle","wb")

    oldfashioned = Drink("old_fashioned",\
        {"whiskey": 2,
        "Angostura bitters": 2,
        "sugar cube": 1,
        "orange twist": 1},\
        5, "Michael", './images/old-fashioned.png')

    negroni = Drink("negroni",\
        {"gin": 1,
        "campari": 1,
        "vermouth": 1},\
        3, "Michael", './images/negroni.png')

    moscowmule = Drink("moscow_mule",\
        {"vodka": 2,
        "ginger beer": 3,
        "lime juice": 0.5},\
        3, "Michael", './images/moscow-mule.png')

    martini = Drink("martini",\
        {"vodka": 3,
        "vermouth": 0.5,
        "olive": 1},\
        5, "Michael", './images/martini.png')

    margarita = Drink("margarita",\
        {"silver tequila": 2,
        "cointreau": 1,
        "lime juice": 1,
        "salt": 1},\
        5, "Michael", './images/margarita.png')

    cosmopolitan = Drink("cosmopolitan",\
        {"vodka": 1.5,
        "cointreau": 1,
        "lime juice": 0.5,
        "cranberry juice": 0.25},\
        5, "Michael", './images/cosmopolitan.png')

    database.append(oldfashioned)
    database.append(negroni)
    database.append(moscowmule)
    database.append(martini)
    database.append(margarita)
    database.append(cosmopolitan) 

    pickle.dump(jsonpickle.encode(database), pickling_on)
    pickling_on.close()

def createFrame(root):
    frame = tk.Frame(root)
    
    menuImageArray = []
    for i in range(0, len(database)):
        menuImageArray.append(ImageTk.PhotoImage(Image.open(database[i].getImagePath()).resize((120, 246))))

    for i in range(0, len(database)):
        menuButton = ttk.Button(root, command = lambda i=i: findDrink(database[i], i))
        menuButton.image = menuImageArray[i]
        menuButton['image'] = menuButton.image
        menuButton.grid(row = 0, column = i)

        findDrinkLabel = tk.Label(root, text=database[i].getName())
        findDrinkLabel.grid(row = 1,column = i)

    menuButtonAdd= ttk.Button(root, text="Add", command = addDrink)
    menuButtonAdd.grid(row = 2, column = 0)

    menuButtonQuit = ttk.Button(root, text="Save & Quit", command = quit)
    menuButtonQuit.grid(row = 2, column = 1)

    return frame

def resetFrame():
    global frame 

    frame.destroy()
    frame = createFrame(root)
    frame.grid(row = 0, column = 0)

def imageFileExplorer(path_label):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("PNG files","*.png*"), ("all files", "*.*")))
    global file_path
    file_path = filename
    path_label.config(text = file_path)

def addDrink():

    """ Creates an add Drink button to implement the addDrinkAction function."""

    global addForm
    addForm = tk.Toplevel(root)
    addForm.title("Add Drink to the Database")
    addForm.geometry('500x400')

    name = ttk.Label(addForm, text= "Drink Name:")
    name.grid(row = 0, column = 0)
    recipe = ttk.Label(addForm, text = "Recipe:")
    recipe.grid(row = 1,column = 0)
    time = ttk.Label(addForm, text = "Time:")
    time.grid(row = 2,column = 0)
    server = ttk.Label(addForm, text = "Server:")
    server.grid(row = 3,column = 0)
    image_path = ttk.Label(addForm, text = "Drink Image:")
    image_path.grid(row = 6, column = 0)

    name_field = ttk.Entry(addForm)
    name_field.grid(row = 0,column = 1)
    recipe_field = ttk.Entry(addForm)
    recipe_field.grid(row = 1,column = 1)
    time_field = ttk.Entry(addForm)
    time_field.grid(row = 2,column = 1)
    server_field = ttk.Entry(addForm)
    server_field.grid(row = 3,column = 1)
    
    image_button = tk.Button(addForm, text = "Browse...", command = lambda:imageFileExplorer(image_path))
    image_button.grid(row = 6, column = 1)

    image_path = ttk.Label(addForm, text = "")
    image_path.grid(row = 6, column = 2)

    submit = ttk.Button(addForm, text="Submit", command=lambda:addDrinkAction(name_field.get(), recipe_field.get(), time_field.get(), server_field.get(), connectDB))
    submit.grid(row = 9, column = 0)

#Back end function
def addDrinkAction(name, recipe, time, server, image_path):

    """ Adds a Drink to the menu using the user input."""

    # This filters the users' input for illegal input
    nameCheck = re.findall("[^a-zA-Z\s:]", name)
    serverCheck = re.findall("[^a-zA-Z\s:]", server)
    timeCheck = re.findall("\D+", time)

    if(nameCheck):
        tkmb.showinfo("ERROR", "ERROR: Drink name must only contain alphabetical characters")
        return 0;

    elif(serverCheck):
        tkmb.showinfo("ERROR", "ERROR: Server name must only contain alphabetical characters")
        return 0;

    elif(timeCheck):
        tkmb.showinfo("ERROR", "ERROR: Time must only contain numbers")
        return 0;
  
    if name in database:
        print("Drink already exists. Please enter a different name.")
        return 0

    else:
        locals()[name] = Drink(name, recipe, time, server, image_path)
        database.append(locals()[name])
        print("Database updated!")
        addForm.destroy()
        resetFrame()
        return 0

def findDrink(Drink, index):

    global findForm
    findForm = tk.Toplevel(root)
    findForm.title("Drink Information")
    findForm.geometry('500x400')
    
    findDrinkLabel = tk.Label(findForm)
    findDrinkLabel.grid(row = 0,column = 0)
    
    name = ttk.Label(findForm, text= "Name:")
    name.grid(row = 0, column = 0)
    name = ttk.Entry(findForm)
    name.insert(tk.INSERT, Drink.getName())
    name.grid(row = 0, column = 1)

    recipe = ttk.Label(findForm, text = "Recipe:")
    recipe.grid(row = 1,column = 0)
    recipe = ttk.Entry(findForm)
    recipe.insert(tk.INSERT, Drink.getRecipe())
    recipe.grid(row = 1,column = 1)

    time = ttk.Label(findForm, text = "Time:")
    time.grid(row = 2,column = 0)
    time = ttk.Entry(findForm)
    time.insert(tk.INSERT, Drink.getTime())
    time.grid(row = 2,column = 1)

    server = ttk.Label(findForm, text = "Server:")
    server.grid(row = 3,column = 0)
    server = ttk.Entry(findForm)
    server.insert(tk.INSERT, Drink.getServer())
    server.grid(row = 3,column = 1)

    updateDrinkButton = ttk.Button(findForm, text="Update Drink", command = lambda:updateDrinkAction(Drink, name.get(), recipe.get(), time.get(), server.get()))
    updateDrinkButton.grid(row = 4, column = 0)

    delDrinkButton = ttk.Button(findForm, text="Delete Drink", command = lambda:delDrinkAction(index))
    delDrinkButton.grid(row = 4, column = 1)

def updateDrinkAction(Drink, name, recipe, time, server):
    Drink.setName(name)
    Drink.setRecipe(recipe)
    Drink.setTime(time)
    Drink.setServer(server)

    findForm.destroy()

def delDrinkAction(index):

    """ Deletes a Drink from the menu."""
    os.remove(database[index].getImagePath())

    del database[index]
    findForm.destroy()

    resetFrame()

    deletedPhoto = root.grid_slaves(row = 0, column = len(database))
    deletedPhoto[0].destroy()

    deletedLabel = root.grid_slaves(row = 1, column = len(database))
    deletedLabel[0].destroy()

    return 0

def quit():

    """ Quits the program."""

    pickling_on = open("database.pickle","wb")
    pickle.dump(jsonpickle.encode(database), pickling_on)
    pickling_on.close()
    root.destroy()

if __name__ == '__main__':
    
    root.title("Main View")
    root.geometry('800x300')

    frame = createFrame(root)
    frame.grid(row = 0, column = 0)

    root.mainloop()

