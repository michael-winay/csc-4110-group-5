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

def addEmployee():

    """ Creates an add employee button to implement the addEmployeeAction function."""

    addForm = tk.Toplevel(root)
    addForm.title("Add Employee")
    addForm.geometry('500x400')
    #addForm.configure(background = "grey");

    id = ttk.Label(addForm ,text = "Employee ID:").grid(row = 0,column = 0)
    first = ttk.Label(addForm ,text = "First Name:").grid(row = 1,column = 0)
    last = ttk.Label(addForm ,text = "Last Name:").grid(row = 2,column = 0)
    position = ttk.Label(addForm ,text = "Position:").grid(row = 3,column = 0)
    ssn = ttk.Label(addForm ,text = "SSN:").grid(row = 4,column = 0)
    address = ttk.Label(addForm ,text = "Address:").grid(row = 5,column = 0)
    email = ttk.Label(addForm ,text = "Email address:").grid(row = 6,column = 0)
    phone = ttk.Label(addForm ,text = "Phone Number: ").grid(row = 7,column = 0)
    skills = ttk.Label(addForm ,text = "Skills: ").grid(row = 8,column = 0)

    id_field = ttk.Entry(addForm)
    id_field.grid(row = 0,column = 1)
    id_field.insert(tk.INSERT, "No special characters")
    first_field = ttk.Entry(addForm)
    first_field.grid(row = 1,column = 1)
    first_field.insert(tk.INSERT, "Alpha chars only")
    last_field = ttk.Entry(addForm)
    last_field.grid(row = 2,column = 1)
    last_field.insert(tk.INSERT, "Alpha chars only")
    position_field = ttk.Entry(addForm)
    position_field.grid(row = 3,column = 1)
    position_field.insert(tk.INSERT, "No special characters")
    ssn_field = ttk.Entry(addForm)
    ssn_field.grid(row = 4,column = 1)
    ssn_field.insert(tk.INSERT, "XXX-XX-XXXX format")
    address_field = ttk.Entry(addForm)
    address_field.grid(row = 5,column = 1)
    address_field.insert(tk.INSERT, "No special characters")
    email_field = ttk.Entry(addForm)
    email_field.grid(row = 6,column = 1)
    phone_field = ttk.Entry(addForm)
    phone_field.grid(row = 7,column = 1)
    phone_field.insert(tk.INSERT, "XXX-XXX-XXXX format")
    skills_field = ttk.Entry(addForm)
    skills_field.grid(row = 8,column = 1)
    skills_field.insert(tk.INSERT, "No special characters")

    #Arguments get passed to back end functions here
    submit = ttk.Button(addForm, text="Submit", command=lambda:addEmployeeAction(id_field.get(), first_field.get(), last_field.get(), position_field.get(), ssn_field.get(), address_field.get(), email_field.get(), phone_field.get(), skills_field.get())).grid(row = 9, column = 0)

#Back end function
def addEmployeeAction(id, first, last, position, ssn, address, email, phone, skills):

    """ Adds an employee to the directory using the user input."""

    # This filters the users' input for illegal format/characters
    if testSpecial(id):
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
        return 0

def delEmployee():

    """ Creates a delete employee button."""

    delForm = tk.Toplevel(root)
    delForm.title("Remove Employee")
    delForm.geometry('500x400')
    #delForm.configure(background = "grey");

    id = ttk.Label(delForm ,text = "Employee ID:").grid(row = 0,column = 0)

    id_field = ttk.Entry(delForm)
    id_field.grid(row = 0,column = 1)
    #Arguments get passed to back end functions here
    submit = ttk.Button(delForm, text="Submit", command=lambda:delEmployeeAction(id_field.get())).grid(row = 1,column = 0)

   #Back end function
def delEmployeeAction(id):

    """ Deletes an employee from the directory."""
    
    # Checks for the existense of employee and deletes them
    if id in database:
        del database[id]
        print("Employee deleted!")
    else:
        print("Employee ID does not exist.")
        return 0

def findEmployee():

    """ Creates a query button."""

    findForm = tk.Toplevel(root)
    findForm.title("Find Employee")
    findForm.geometry('500x400')
    #findForm.configure(background = "grey");

    id = ttk.Label(findForm ,text = "Employee ID:").grid(row = 0,column = 0)
    
    id_field = ttk.Entry(findForm)
    id_field.grid(row = 0,column = 1)

    #Arguments get passed to back end functions here
    submit = ttk.Button(findForm, text="Submit", command=lambda:findEmployeeAction(id_field.get())).grid(row = 1,column = 0)

#Back end function
def findEmployeeAction(id):

    """ Queries the directory for the employee matching the given id."""

    # If employee is found prints their data
    if id in database:
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
        return False

#test function
def testSpecial(subject):
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
    return False

#test function
def testSpecialAndNum(subject):
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
    return False

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

    addButton = ttk.Button(root ,text="Add Employee", command = addEmployee)
    addButton.pack()

    delButton = ttk.Button(root ,text="Remove Employee", command = delEmployee)
    delButton.pack()

    findButton = ttk.Button(root ,text="Find Employee", command = findEmployee)
    findButton.pack()

    quitButton = ttk.Button(root, text="Quit", command = quit)
    quitButton.pack()

    root.mainloop()