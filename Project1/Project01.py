import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk

def addEmployee():
    addForm = tk.Toplevel(root)
    addForm.title("Add Employee")
    addForm.geometry('500x400')
    addForm.configure(background = "grey");

    id = ttk.Label(addForm ,text = "Employee ID:").grid(row = 0,column = 0)
    first = ttk.Label(addForm ,text = "First Name:").grid(row = 1,column = 0)
    last = ttk.Label(addForm ,text = "Last Name:").grid(row = 2,column = 0)
    position = ttk.Label(addForm ,text = "Position:").grid(row = 3,column = 0)
    ssn = ttk.Label(addForm ,text = "SSN:").grid(row = 4,column = 0)
    address = ttk.Label(addForm ,text = "Address:").grid(row = 5,column = 0)
    email = ttk.Label(addForm ,text = "Email address:").grid(row = 6,column = 0)
    phone = ttk.Label(addForm ,text = "Phone Number: ").grid(row = 7,column = 0)
    skills = ttk.Label(addForm ,text = "Skills: ").grid(row = 8,column = 0)

    id_field = ttk.Entry(addForm).grid(row = 0,column = 1)
    first_field = ttk.Entry(addForm).grid(row = 1,column = 1)
    last_field = ttk.Entry(addForm).grid(row = 2,column = 1)
    position_field = ttk.Entry(addForm).grid(row = 3,column = 1)
    ssn_field = ttk.Entry(addForm).grid(row = 4,column = 1)
    address_field = ttk.Entry(addForm).grid(row = 5,column = 1)
    email_field = ttk.Entry(addForm).grid(row = 6,column = 1)
    phone_field = ttk.Entry(addForm).grid(row = 7,column = 1)
    skills_field = ttk.Entry(addForm).grid(row = 8,column = 1)

def delEmployee():
    delForm = tk.Toplevel(root)
    delForm.title("Remove Employee")
    delForm.geometry('500x400')
    delForm.configure(background = "grey");

    id = ttk.Label(delForm ,text = "Employee ID:").grid(row = 0,column = 0)

    id_field = ttk.Entry(delForm).grid(row = 0,column = 1)

def findEmployee():
    findForm = tk.Toplevel(root)
    findForm.title("Find Employee")
    findForm.geometry('500x400')
    findForm.configure(background = "grey");

    id = ttk.Label(findForm ,text = "Employee ID:").grid(row = 0,column = 0)

    id_field = ttk.Entry(findForm).grid(row = 0,column = 1)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Main View")
    root.geometry('500x400')
    root.configure(background = "grey");

    addButton = ttk.Button(root ,text="Add Employee", command = addEmployee)
    addButton.pack()

    delButton = ttk.Button(root ,text="Remove Employee", command = delEmployee)
    delButton.pack()

    findButton = ttk.Button(root ,text="Find Employee", command = findEmployee)
    findButton.pack()

    root.mainloop()