import sys
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext

class TextRedirector:
    def __init__(self, text_widget, tag):
        self.text_widget = text_widget
        self.tag = tag

    def write(self, s):
        self.text_widget.insert(tk.END, s, (self.tag,))
        self.text_widget.see(tk.END)  # Auto-scroll to the bottom
        self.text_widget.update_idletasks()  # Update the Tkinter window
    
    def flush(self):
        pass
    def clear_console(self):
        self.text_widget.delete("1.0", tk.END)  # Clear the content of the Text widget


class ConsoleApp:
    def __init__(self, window):
        self.window = window
        
        self.title = ttk.Label(self.window, text="Results: ")
        self.title.pack(pady=5)

        # Create a Text widget for console output
        self.console_output = scrolledtext.ScrolledText(self.window, wrap=tk.WORD)
        self.console_output.pack(padx=10, pady=10, fill="both")

        # Redirect stdout to the Text widget
        self.text_redirector = TextRedirector(self.console_output, "stdout")
        sys.stdout = self.text_redirector

        # Print some sample output
        print("Type a username and press search!")
        print("The screen may freeze during the search. (its a feature)")
        
        clear_button = ttk.Button(self.window, text="Clear Results", command=self.text_redirector.clear_console, bootstyle=DANGER)
        clear_button.pack(pady=5)