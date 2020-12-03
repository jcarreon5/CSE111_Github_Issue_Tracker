from os import error
import tkinter as tk
from Database import *

root = tk.Tk()
loginWindow = tk.Frame(root)
projectsWindow = tk.Frame(root)
projectInfoWindow = tk.Frame(root)
errorPopup = tk.Frame(root)
windows = [loginWindow, projectsWindow, projectInfoWindow, errorPopup]

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
    
    tk.Button(loginWindow, text = "Log-in", width = 10, height = 1, command = lambda: logIn(username, password, table)).pack()
    
    root.mainloop()

def callProjectsWindow(projects):
    for w in windows:
        w.pack_forget()
    projectsWindow.pack()
    
    tk.Label(projectsWindow, text = "Projects").pack()
    
    scrollbar = tk.Scrollbar(projectsWindow)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    
    projectDisplay = tk.Listbox(projectsWindow, yscrollcommand = scrollbar.set)
    projIDs = []
    for p in projects:
        projectDisplay.insert(tk.END, p[1])
        projIDs.append(p[0])
    
    projectDisplay.pack(side = tk.LEFT, fill = tk.BOTH)
    scrollbar.config(command = projectDisplay.yview)
    
    tk.Button(projectsWindow, text = "Open Project", width = 10, height = 1, command = lambda: callShowProjectData(projects, projIDs[projectDisplay.curselection()[0]])).pack()

    projectsWindow.tkraise()

def logIn(username, password, table):
    #print("user:", username.get(), "pass:", password.get(), "table:", table.get())
    id = loginDatabase(username.get(), password.get(), table.get())
    projects = getProjectInfoByID(id, table.get())
    if(projects):
        callProjectsWindow(projects)
    else:
        e = tk.Label(errorPopup, text = "Invalid login/password combination!")
        e.pack()
        root.after(1000, tk.Label.pack_forget, e)
        root.after(1000, tk.Label.pack_forget, errorPopup)
        errorPopup.tkraise(loginWindow)
        
    
def callShowProjectData(projects, ID = 0):
    for w in windows:
        w.pack_forget()
    projectInfoWindow.pack()
    
    tk.Button(projectsWindow, text = "Open Project", width = 10, height = 1, command = lambda: callProjectsWindow(projects)).pack()
    
    tk.Label(text = "Project name: ").pack()
    tk.Label(text = projects[ID][1]).pack()
    tk.Label(text = "Project description: ").pack()
    tk.Label(text = projects[ID][2]).pack()
    tk.Label(text = "Project created date: ").pack()
    tk.Label(text = projects[ID][3]).pack()
    tk.Label(text = "Project last update: ").pack()
    tk.Label(text = projects[ID][4]).pack()


def main():
    #startUI()
    databaseSetup()
    callProjectsWindow(getProjectInfoByID(0, "Developer"))
    root.mainloop()
    print("==========")
    

if __name__ == '__main__':
    main()
