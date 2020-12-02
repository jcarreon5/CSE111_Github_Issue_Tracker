import tkinter as tk

from Database import *

root = tk.Tk()
loginWindow = tk.Frame(root)
projectsWindow = tk.Frame(root)

def startUI():
    loginWindow.pack()
    
    username = tk.StringVar()
    password = tk.StringVar()
    
    tk.Label(loginWindow, text = "Please log in...", width = 25, height = 5).pack()
    
    tk.Label(loginWindow, text = "Are you a developer or customer?").pack()
    
    table = tk.StringVar(None, "None")
    developer = tk.Radiobutton(loginWindow, text = "Developer", variable = table, value = "Developer")
    developer.pack()
    customer = tk.Radiobutton(loginWindow, text = "Customer", variable = table, value = "Customer")
    customer.pack()
    
    tk.Label(loginWindow, text = "Enter username:").pack()
    
    tk.Entry(loginWindow, textvariable = username).pack()
    
    tk.Label(loginWindow, text = "Enter password:").pack()
    
    passwordEntry = tk.Entry(loginWindow, textvariable = password)
    passwordEntry.pack()
    
    login = tk.Button(loginWindow, text = "Log-in", width = 10, height = 1, command = lambda: logIn(username, password, table))
    login.pack()
    
    root.mainloop()

def callprojectsWindow(projects):
    loginWindow.pack_forget()
    projectsWindow.pack()
    
    tk.Label(projectsWindow, text = "Projects").pack()
    
    scrollbar = tk.Scrollbar(projectsWindow)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    
    projectDisplay = tk.Listbox(projectsWindow, yscrollcommand = scrollbar.set)
    
    
    projectsWindow.tkraise()

def logIn(username, password, table):
    #print("user:", username.get(), "pass:", password.get(), "table:", table.get())
    id = loginDatabase(username, password, table)
    projects = getProjectInfoByID(id, table)
    callprojectsWindow(projects)
    

def main():
    startUI()
    print("==========")
    

if __name__ == '__main__':
    main()
