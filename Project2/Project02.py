import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import jsonpickle
import pickle
from PIL import ImageTk, Image
from tkinter import filedialog
from os.path import exists

"""Drink class"""

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

    def getRecipe(self):
        return self.server

    def getImagePath(self):
        return self.image_path

database = []
file_exists = exists("database.pickle")
if file_exists:
    pickle_off = open("database.pickle","rb")
    database = jsonpickle.decode(pickle.load(pickle_off))
else:
    pickling_on = open("database.pickle","wb")
    
    oldfashioned = Drink("old-fashioned",\
        ["2 oz bourbon or rye whiskey",\
        "2 dashes Angostura bitters",\
        "1 sugar cube or 1 tsp sugar"\
        "Orange twist garnish"],\
        5, "Michael", 'images/old-fashioned.png')

    negroni = Drink("negroni",\
        ["1 oz gin",\
        "1 oz Campari",\
        "1 oz sweet vermouth"],\
        3, "Michael", 'images/negroni.png')

    moscowmule = Drink("moscow-mule",\
        ["2 oz vodka",\
        "4 to 6 oz ginger beer",\
        ".5 oz lime juice"],\
        3, "Michael", 'images/moscow-mule.png')

    martini = Drink("martini",\
        ["3 oz gin or vodka",\
        ".5 oz dry vermouth",\
        "Lemon peel or olive"],\
        5, "Michael", 'images/old-fashioned.png')

    margarita = Drink("margarita",\
        ["2 oz silver tequila"
        "1 oz Cointreau",\
        "1 oz lime juice",\
        "Salt for the rim"],\
        5, "Michael", 'images/margarita.png')

    cosmopolitan = Drink("cosmopolitan",\
        ["1.5 oz citrus vodka",\
        "1 oz Cointreau",\
        ".5 oz lime juice",\
        ".25 oz cranberry juice"],\
        5, "Michael", 'images/cosmopolitan.png')

    database.append(oldfashioned)
    database.append(negroni)
    database.append(moscowmule)
    database.append(martini)
    database.append(margarita)
    database.append(cosmopolitan) 

    pickle.dump(jsonpickle.encode(database), pickling_on)
    pickling_on.close()

def imageFileExplorer(path_label):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("PNG files","*.png*"), ("all files", "*.*")))
    global file_path
    file_path = filename
    path_label.config(text = file_path)

def addDrink():

    """ Creates an add drink button to implement the addDrinkAction function."""


    addForm = tk.Toplevel(root)
    addForm.title("Add Drink to the Menu")
    addForm.geometry('500x400')
    #addForm.configure(background = "grey");

    name = ttk.Label(addForm ,text = "Drink Name:")
    name.grid(row = 0,column = 0)
    recipe = ttk.Label(addForm ,text = "Ingredients:")
    recipe.grid(row = 1,column = 0)
    time = ttk.Label(addForm ,text = "Time:")
    time.grid(row = 2,column = 0)
    server = ttk.Label(addForm ,text = "Server:")
    server.grid(row = 3,column = 0)
    image = ttk.Label(addForm, text = "Image:")
    image.grid(row = 4, column = 0)

    name_field = ttk.Entry(addForm)
    name_field.grid(row = 0,column = 1)
    recipe_field = ttk.Entry(addForm)
    recipe_field.grid(row = 1,column = 1)
    recipe_field.insert(tk.INSERT, "comma seperated")
    time_field = ttk.Entry(addForm)
    time_field.grid(row = 2,column = 1)
    server_field = ttk.Entry(addForm)
    server_field.grid(row = 3,column = 1)
    image_path = ttk.Label(addForm, text = "")
    image_path.grid(row = 4, column = 2)
    image_button = tk.Button(addForm, text = "Browse...", command = lambda:imageFileExplorer(image_path))
    image_button.grid(row = 4, column = 1)
    """try:
        file_path
    except:
        image_path = ttk.Label(addForm, text = "")
        image_path.grid(row = 4, column = 2)
    else:
        image_path = ttk.Label(addForm, text = file_path)
        image_path.grid(row = 4, column = 2)"""

    submit = ttk.Button(addForm, text="Submit", command=lambda:addDrinkAction(name_field.get(), recipe_field.get(), time_field.get(), server_field.get(), file_path)).grid(row = 9, column = 0)

#Back end function
def addDrinkAction(name, recipe, time, server, image_path):
    #This should move the image at image_path to the local images directory
    #also add the input as an object of the drink class

    """ Adds an employee to the directory using the user input."""

    # This filters the users' input for illegal format/characters
    """if testSpecial(id):
        print("ID contains illegal character! Resubmit request.")
        return 0
    if testSpecialAndNum(first):
        print("First contains illegal character! Resubmit request.")
        return 0
    if testSpecialAndNum(last):
        print("Last contains illegal character! Resubmit request.")
        return 0
    if testSpecial(position):
        print("ID contains illegal character! Resubmit request.")
        return 0
    if "-" not in ssn:
        print("SSN not in correct format. Resubmit request.")
    if testSpecial(address):
        print("Address contains illegal character! Resubmit request.")
        return 0
    if "-" not in phone:
        print("Phone number is not in the correct format. Resubmit request.")
    if testSpecial(skills):
        print("Skills contain illegal character! Resubmit request.")
        return 0

    # Checks if id is already in the database to eliminate duplicates
    if id in database:
        print("Employee ID already exists. Please enter a different ID.")
        return 0
    else:
        database[id] = [first, last, position, ssn, address, email, phone, skills]
        print("Database updated!")
        return 0"""

def findDrink(drink, index):

    findForm = tk.Toplevel(root)
    findForm.title("Order Drink from the Menu")
    findForm.geometry('500x400')
    
    findDrinkLabel = tk.Label(findForm)
    findDrinkLabel.grid(row = 0,column = 0)

    #should display the info about the selected drink here:


    delDrinkButton = ttk.Button(findForm, text="Delete drink", command = delDrinkAction)
    delDrinkButton.grid(row = 1, column = 0)

#probably not needed anymore
"""def delDrink():

    delForm = tk.Toplevel(root)
    delForm.title("Remove Drink from the Menu")
    delForm.geometry('500x400')
    #delForm.configure(background = "grey");

    name = ttk.Label(delForm ,text = "Drink Name:").grid(row = 0,column = 0)

    name_field = ttk.Entry(delForm)
    name_field.grid(row = 0,column = 1)
    #Arguments get passed to back end functions here
    submit = ttk.Button(delForm, text="Submit", command=lambda:delDrinkAction(name_field.get())).grid(row = 1,column = 0)"""

   #Back end function

def delDrinkAction(id):

    """ Deletes an employee from the directory."""
    
    # Checks for the existense of employee and deletes them
    """if id in database:
        del database[id]
        print("Employee deleted!")
    else:
        print("Employee ID does not exist.")
        return 0"""

def quit():

    """ Quits the program."""

    pickling_on = open("database.pickle","wb")
    pickle.dump(jsonpickle.encode(database), pickling_on)
    pickling_on.close()
    root.destroy()

if __name__ == '__main__':
    
    root.title("Main View")
    root.geometry('800x300')
    #root.configure(background = "grey");

    menuImageArray = []
    for i in range(0, len(database)):
        menuImageArray.append(ImageTk.PhotoImage(Image.open(database[i].getImagePath()).resize((120, 246))))

    for i in range(0, len(database)):
        menuButton = ttk.Button(root, image = menuImageArray[i], command = lambda:findDrink(database[i], i))
        menuButton.grid(row = 0, column = i)
        findDrinkLabel = tk.Label(root, text=database[i].getName())
        findDrinkLabel.grid(row = 1,column = i)

    menuButtonAdd= ttk.Button(root, text="Add", command = addDrink)
    menuButtonAdd.grid(row = 2, column = 0)

    menuButtonQuit = ttk.Button(root, text="Save & Quit", command = quit)
    menuButtonQuit.grid(row = 2, column = 1)

    root.mainloop()
