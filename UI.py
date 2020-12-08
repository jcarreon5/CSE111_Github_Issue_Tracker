from os import error
import Tkinter as tk
from Database import *

root = tk.Tk()
loginWindow = tk.Frame(root)
projectsWindow = tk.Frame(root)
projectInfoWindow = tk.Frame(root)
branchInfoWindow = tk.Frame(root)
issueInfoWindow = tk.Frame(root)
releaseInfoWindow = tk.Frame(root)
mergeInfoWindow = tk.Frame(root)
errorPopup = tk.Frame(root)
windows = [loginWindow, projectsWindow, projectInfoWindow, errorPopup, branchInfoWindow, issueInfoWindow, releaseInfoWindow,mergeInfoWindow]

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
    
    tk.Entry(loginWindow, textvariable = password)
    
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
    
    tk.Button(projectsWindow, text = "Open Project", width = 10, height = 1, command = lambda: callShowProjectData(projects, projIDs[projectDisplay.curselection()[0]] - 1)).pack()

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
        
    
def callShowProjectData(projects, ID = 1):
    for w in windows:
        w.pack_forget()
    projectInfoWindow.pack()
    
    
    tk.Label(text = "Project name: ").pack()
    tk.Label(text = projects[ID][1]).pack()
    tk.Label(text = "Project description: ").pack()
    tk.Label(text = projects[ID][2]).pack()
    tk.Label(text = "Issues:").pack()
    
    
    
    issues = getAllIssuesForProject(projects[ID][0])
    issueIDs = []
    if(issues):
        scrollbar = tk.Scrollbar(projectInfoWindow)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        
        issueDisplay = tk.Listbox(projectInfoWindow, yscrollcommand = scrollbar.set)
        for i in issues:
            t = getIssueDetails(i)
            issueDisplay.insert(tk.END, t[2])
            issueIDs.append(t[0])
            
        issueDisplay.pack(side = tk.LEFT, fill = tk.BOTH)
        scrollbar.config(command = issueDisplay.yview)
    

    else:
        e = tk.Label(errorPopup, text = "Invalid login/password combination!")
        e.pack()
        root.after(1000, tk.Label.pack_forget, e)
        root.after(1000, tk.Label.pack_forget, errorPopup)
        errorPopup.tkraise(loginWindow)
        return
    
    tk.Button(projectInfoWindow, text = "Open Issue", width = 10, height = 1, command = lambda: callShowProjectData(projects, issueIDs[issueDisplay.curselection()[0]] - 1)).pack()

    projectInfoWindow.tkraise()

    tk.Label(text = "Project created date: ").pack()
    tk.Label(text = projects[ID][3]).pack()
    tk.Label(text = "Project last update: ").pack()
    tk.Label(text = projects[ID][4]).pack()

def callShowBranchData(branch, ID = 1):
    for w in windows:
        w.pack_forget()
    branchInfoWindow.pack()
    
    
    tk.Label(text = " Issue ID: ").pack()
    tk.Label(text = branch[ID][1]).pack()
    tk.Label(text = "Branch Description: ").pack()
    tk.Label(text = branch[ID][2]).pack()


def callShowIssueData(issues, ID = 1):
    for w in windows:
        w.pack_forget()
    releaseInfoWindow.pack()
    
    
    tk.Label(text = "Project ID: ").pack()
    tk.Label(text = issues[ID][1]).pack()
    tk.Label(text = "Issue Description: ").pack()
    tk.Label(text = issues[ID][2]).pack()
    tk.Label(text = "Branches:").pack()
    
    
    branches = getAllBranchesFromIssue(issues[ID][0])
    branchIDs = []
    if(branches):
        scrollbar = tk.Scrollbar(issueInfoWindow)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        
        branchDisplay = tk.Listbox(issueInfoWindow, yscrollcommand = scrollbar.set)
        for i in branches:
            t = getBranchesDetails(i)
            branchDisplay.insert(tk.END, t[2])
            branchIDs.append(t[0])
            
        branchDisplay.pack(side = tk.LEFT, fill = tk.BOTH)
        scrollbar.config(command = branchDisplay.yview)
    

    else:
        e = tk.Label(errorPopup, text = "Invalid login/password combination!")
        e.pack()
        root.after(1000, tk.Label.pack_forget, e)
        root.after(1000, tk.Label.pack_forget, errorPopup)
        errorPopup.tkraise(loginWindow)
        return
    
    tk.Button(issueInfoWindow, text = "Open Issue", width = 10, height = 1, command = lambda: callShowIssueData(issues, branchIDs[branchDisplay.curselection()[0]] - 1)).pack()

    issueInfoWindow.tkraise()

def callShowReleaseData(releases, ID = 1):
    for w in windows:
        w.pack_forget()
    releaseInfoWindow.pack()
    
    
    tk.Label(text = "Project ID: ").pack()
    tk.Label(text = releases[ID][1]).pack()
    tk.Label(text = "Release description: ").pack()
    tk.Label(text = releases[ID][2]).pack()


def callShowMergeRequestData(merge, ID = 1):
    for w in windows:
        w.pack_forget()
    mergeInfoWindow.pack()
    
    tk.Label(text = "Merge description: ").pack()
    tk.Label(text = merge[ID][2]).pack()

    branches = getAllBranchesFromMerge(merge[ID][0])
    branchIDs = []
    if(branches):
        scrollbar = tk.Scrollbar(mergeInfoWindow)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        
        branchDisplay = tk.Listbox(mergeInfoWindow, yscrollcommand = scrollbar.set)
        for i in branches:
            t = getBranchesDetails(i)
            branchDisplay.insert(tk.END, t[2])
            branchIDs.append(t[0])
            
        branchDisplay.pack(side = tk.LEFT, fill = tk.BOTH)
        scrollbar.config(command = branchDisplay.yview)
    

    else:
        e = tk.Label(errorPopup, text = "Invalid login/password combination!")
        e.pack()
        root.after(1000, tk.Label.pack_forget, e)
        root.after(1000, tk.Label.pack_forget, errorPopup)
        errorPopup.tkraise(loginWindow)
        return
    
    tk.Button(mergeInfoWindow, text = "Open Issue", width = 10, height = 1, command = lambda: callShowMergeRequestData(merge, branchIDs[branchDisplay.curselection()[0]] - 1)).pack()

    mergeInfoWindow.tkraise()


def main():
    #startUI()
    databaseSetup()
    callProjectsWindow(getProjectInfoByID(11, "Developer"))
    root.mainloop()
    print("==========")
    

if __name__ == '__main__':
    main()
