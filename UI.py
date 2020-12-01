import tkinter as tk


def startUI():
    window = tk.Tk()
    
    username = ""
    password = ""
    
    label = tk.Label(text = "Please log in...", width = 20, height = 40)
    label.pack()
    
    usernameLabel = tk.Label(text = "Enter username:")
    usernameLabel.pack()
    
    usernameEntry = tk.Entry(textvariable = username)
    usernameEntry.select_clear()
    usernameEntry.pack()
    
    passwordLabel = tk.Label(text = "Enter password:")
    passwordLabel.pack()
    
    passwordEntry = tk.Entry(textvariable = password)
    passwordEntry.pack()
    
    login = tk.Button(text = "Log-in", width = 64, height = 32)
    login.pack()
    
    window.mainloop()

def main():
    startUI()
    print("==========")
    

if __name__ == '__main__':
    main()
