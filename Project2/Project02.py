import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import pickle
from PIL import ImageTk, Image
from os.path import exists

"""Drink class"""

class Drink:
    def __init__(self, name, recipe, time, server, image):
        self.name = name
        self.recipe = recipe
        self.time = time
        self.server = server
        self.image = ImageTk.PhotoImage(Image.open(image).resize((120, 246)))

    def setName(self, name):
        self.name = name

    def setRecipe(self, recipe):
        self.recipe = recipe

    def setTime(self, time):
        self.time = time

    def setServer(self, server):
        self.server = server

    def setImage(self, image):
        self.image = image

    def getName(self):
        return self.name

    def getRecipe(self):
        return self.recipe

    def getTime(self):
        return self.time

    def getRecipe(self):
        return self.server

    def getImage(self):
        return self.image


database = {}
file_exists = exists("database.pickle")
if file_exists:
    pickle_off = open("database.pickle","rb")
    database = pickle.load(pickle_off)

def addDrink():

    """ Creates an add drink button to implement the addDrinkAction function."""

    addForm = tk.Toplevel(root)
    addForm.title("Add Drink to the Menu")
    addForm.geometry('500x400')
    #addForm.configure(background = "grey");

    name = ttk.Label(addForm ,text = "Drink Name:").grid(row = 0,column = 0)
    recipe = ttk.Label(addForm ,text = "Ingredients:").grid(row = 1,column = 0)
    time = ttk.Label(addForm ,text = "Time:").grid(row = 2,column = 0)
    server = ttk.Label(addForm ,text = "Server:").grid(row = 3,column = 0)

    name_field = ttk.Entry(addForm)
    name_field.grid(row = 0,column = 1)
    #id_field.insert(tk.INSERT, "No special characters")
    recipe_field = ttk.Entry(addForm)
    recipe_field.grid(row = 1,column = 1)
    time_field = ttk.Entry(addForm)
    time_field.grid(row = 2,column = 1)
    server_field = ttk.Entry(addForm)
    server_field.grid(row = 3,column = 1)

    #Arguments get passed to back end functions here
    submit = ttk.Button(addForm, text="Submit", command=lambda:addDrinkAction(name_field.get(), recipe_field.get(), time_field.get(), server_field.get())).grid(row = 9, column = 0)

#Back end function
def addDrinkAction(name, recipe, time, server):

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

def delDrink():

    """ Creates a delete employee button."""

    delForm = tk.Toplevel(root)
    delForm.title("Remove Drink from the Menu")
    delForm.geometry('500x400')
    #delForm.configure(background = "grey");

    name = ttk.Label(delForm ,text = "Drink Name:").grid(row = 0,column = 0)

    name_field = ttk.Entry(delForm)
    name_field.grid(row = 0,column = 1)
    #Arguments get passed to back end functions here
    submit = ttk.Button(delForm, text="Submit", command=lambda:delDrinkAction(name_field.get())).grid(row = 1,column = 0)

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

def findDrink(drink):

    """ Creates a query button."""

    """findForm = tk.Toplevel(root)
    findForm.title("Order Drink from the Menu")
    findForm.geometry('500x400')
    #findForm.configure(background = "grey");

    name = ttk.Label(findForm ,text = "Drink Name:").grid(row = 0,column = 0)
    
    name_field = ttk.Entry(findForm)
    name_field.grid(row = 0,column = 1)

    #Arguments get passed to back end functions here
    submit = ttk.Button(findForm, text="Submit", command=lambda:findDrinkAction(name_field.get())).grid(row = 1,column = 0)"""

    findForm = tk.Toplevel(root)
    findForm.title("Order Drink from the Menu")
    findForm.geometry('500x400')
    
    findDrinkLabel = tk.Label(findForm, image=drink.getImage())
    findDrinkLabel.grid(row = 0,column = 0)

#Back end function
def findDrinkAction(id):

    """ Queries the directory for the employee matching the given id."""

    # If employee is found prints their data
    """if id in database:
        print("%s found!" % id)
        print(database[id])
        
        message = \
            "ID: " + id + "\n"\
            "First Name: " + database[id][0] + "\n"\
            "Last Name: " + database[id][1] + "\n"\
            "Position: " + database[id][2] + "\n"\
            "SSN: " + database[id][3] + "\n"\
            "Address: " + database[id][4] + "\n"\
            "Email Address: " + database[id][5] + "\n"\
            "Phone Number: " + database[id][6] + "\n"\
            "Skills: " + database[id][7] + "\n"\

        tkmb.showinfo(id, message)

        return True
    else:
        print("%s not found!" % id)
        return False"""

#test function
"""def testSpecial(subject):
    if "!" in subject:
        return True
    if "@" in subject:
        return True
    if "#" in subject:
        return True
    if "$" in subject:
        return True
    if "%" in subject:
        return True
    if "^" in subject:
        return True
    if "&" in subject:
        return True
    if "*" in subject:
        return True
    if "*" in subject:
        return True
    if "(" in subject:
        return True
    if ")" in subject:
        return True
    return False"""

#test function
"""def testSpecialAndNum(subject):
    if "!" in subject:
        return True
    if "@" in subject:
        return True
    if "#" in subject:
        return True
    if "$" in subject:
        return True
    if "%" in subject:
        return True
    if "^" in subject:
        return True
    if "&" in subject:
        return True
    if "*" in subject:
        return True
    if "*" in subject:
        return True
    if "(" in subject:
        return True
    if ")" in subject:
        return True
    if "0" in subject:
        return True
    if "1" in subject:
        return True
    if "2" in subject:
        return True
    if "3" in subject:
        return True
    if "4" in subject:
        return True
    if "5" in subject:
        return True
    if "6" in subject:
        return True
    if "7" in subject:
        return True
    if "8" in subject:
        return True
    if "9" in subject:
        return True
    return False"""

#quit button action
def quit():

    """ Quits the program."""

    pickling_on = open("database.pickle","wb")
    pickle.dump(database, pickling_on)
    pickling_on.close()
    root.destroy()

if __name__ == '__main__':

    root = tk.Tk()
    root.title("Main View")
    root.geometry('800x246')
    #root.configure(background = "grey");

    oldfashioned = Drink("old-fashioned",\
        ["- 2 oz bourbon or rye whiskey",\
        "- 2 dashes Angostura bitters",\
        "- 1 sugar cube or 1 tsp sugar"\
        "- Orange twist garnish"],\
        5, "Michael", 'images/old-fashioned.png')

    negroni = Drink("negroni",\
        ["- 1 oz gin",\
        "- 1 oz Campari",\
        "- 1 oz sweet vermouth"],\
        3, "Michael", 'images/negroni.png')

    moscowmule = Drink("moscow-mule",\
        ["- 2 oz vodka",\
        "- 4 to 6 oz ginger beer",\
        "- .5 oz lime juice"],\
        3, "Michael", 'images/moscow-mule.png')

    martini = Drink("martini",\
        ["- 3 oz gin or vodka",\
        "- .5 oz dry vermouth",\
        "- Lemon peel or olive"],\
        5, "Michael", 'images/old-fashioned.png')

    margarita = Drink("margarita",\
        ["- 2 oz silver tequila"
        "- 1 oz Cointreau",\
        "- 1 oz lime juice",\
        "- Salt for the rim"],\
        5, "Michael", 'images/margarita.png')

    cosmopolitan = Drink("cosmopolitan",\
        ["- 1.5 oz citrus vodka",\
        "- 1 oz Cointreau",\
        "- .5 oz lime juice",\
        "- .25 oz cranberry juice"],\
        5, "Michael", 'images/cosmopolitan.png')

    #menuImageOne = ImageTk.PhotoImage(Image.open('images/old-fashioned.png').resize((120, 246)))
    #menuImageTwo = ImageTk.PhotoImage(Image.open('images/negroni.png').resize((120, 246)))
    #menuImageThree = ImageTk.PhotoImage(Image.open('images/moscow-mule.png').resize((120, 246)))
    #menuImageFour = ImageTk.PhotoImage(Image.open('images/martini.png').resize((120, 246)))
    #menuImageFive = ImageTk.PhotoImage(Image.open('images/margarita.png').resize((120, 246)))
    #menuImageSix = ImageTk.PhotoImage(Image.open('images/cosmopolitan.png').resize((120, 246)))

    """menuLabelOne = tk.Label(image=menuImageOne)
    menuLabelTwo = tk.Label(image=menuImageTwo)
    menuLabelThree = tk.Label(image=menuImageThree)
    menuLabelFour = tk.Label(image=menuImageFour)
    menuLabelFive = tk.Label(image=menuImageFive)
    menuLabelSix = tk.Label(image=menuImageSix)"""
    
    menuButtonOne = ttk.Button(root, image=oldfashioned.getImage(), command = lambda:findDrink(oldfashioned))
    menuButtonOne.grid(row = 0,column = 0)

    menuButtonTwo = ttk.Button(root, image=negroni.getImage(), command = lambda:findDrink(negroni))
    menuButtonTwo.grid(row = 0,column = 1)

    menuButtonThree = ttk.Button(root, image=moscowmule.getImage(), command = lambda:findDrink(moscowmule))
    menuButtonThree.grid(row = 0,column = 2)

    menuButtonFour = ttk.Button(root, image=martini.getImage(), command = lambda:findDrink(martini))
    menuButtonFour.grid(row = 0,column = 3)

    menuButtonFive = ttk.Button(root, image=margarita.getImage(), command = lambda:findDrink(margarita))
    menuButtonFive.grid(row = 0,column = 4)

    menuButtonSix = ttk.Button(root, image=cosmopolitan.getImage(), command = lambda:findDrink(cosmopolitan))
    menuButtonSix.grid(row = 0,column = 5)

    menuButtonDelete = ttk.Button(root, text="Delete Drink")

    menuButtonQuit = ttk.Button(root, text="Quit", command = quit)
    menuButtonQuit.grid(row = 1, column = 0)

    root.mainloop()
