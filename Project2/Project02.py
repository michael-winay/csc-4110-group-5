import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import pickle
from os.path import exists

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

def findDrink():

    """ Creates a query button."""

    findForm = tk.Toplevel(root)
    findForm.title("Order Drink from the Menu")
    findForm.geometry('500x400')
    #findForm.configure(background = "grey");

    name = ttk.Label(findForm ,text = "Drink Name:").grid(row = 0,column = 0)
    
    name_field = ttk.Entry(findForm)
    name_field.grid(row = 0,column = 1)

    #Arguments get passed to back end functions here
    submit = ttk.Button(findForm, text="Submit", command=lambda:findDrinkAction(name_field.get())).grid(row = 1,column = 0)

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
    root.geometry('500x400')
    #root.configure(background = "grey");

    addButton = ttk.Button(root ,text="Add Drink", command = addDrink)
    addButton.pack()

    delButton = ttk.Button(root ,text="Remove Drink", command = delDrink)
    delButton.pack()

    findButton = ttk.Button(root ,text="Order Drink", command = findDrink)
    findButton.pack()

    quitButton = ttk.Button(root, text="Quit", command = quit)
    quitButton.pack()

    root.mainloop()
