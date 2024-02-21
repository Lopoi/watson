import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sys
import os
from console import *

#folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sherlock/sherlock'))
folder_path = os.path.join(sys._MEIPASS, 'sherlock/sherlock') if hasattr(sys, '_MEIPASS') else 'sherlock/sherlock'
sys.path.append(folder_path)
import sherlock
from result import QueryResult
sys.path.remove(folder_path)
#print(dir(sherlock))  # Print the attributes of the module

root = tk.Tk()

root.title("Watson")

label = ttk.Label(root, text="Username: ")
label.pack(pady=5)

entry = ttk.Entry(root)
entry.pack(pady=10, padx=10, fill="x")

def search_user():
    username = entry.get()
    print("Searching for user: " + username)
    sys.argv = ['sherlock', username]
    sherlock.main()

button = ttk.Button(root, text="Begin Search", bootstyle=SUCCESS, command=search_user)
button.pack(padx=5, pady=10)

output = ttk.Label(root, text="Results: ")
output.pack(pady=5)

app = ConsoleApp(root)

root.mainloop()