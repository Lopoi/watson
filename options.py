import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Options:
    def __init__(self, root):
        self.root = root

        self.toggle_button = ttk.Button(self.root, text="Hide Options", command=self.toggle_options, bootstyle=DANGER)
        self.toggle_button.pack(pady=5)
        # Create a frame for the options
        self.showing = True
        self.options_frame = ttk.Frame(root)
        self.options_frame.pack(side="right", padx=10, pady=10, fill="y")
        
        # Create Title
        self.title = ttk.Label(self.options_frame, text="Options")
        self.title.pack(pady=5)

    def toggle_options(self):
        if self.showing:
            self.hide_options()
            self.toggle_button.config(text="Show Options")
            self.toggle_button.config(bootstyle=PRIMARY)
            self.showing = False
        else:
            self.show_options()
            self.toggle_button.config(text="Hide Options")
            self.toggle_button.config(bootstyle=DANGER)
            self.showing = True
    
    def hide_options(self):
        self.options_frame.pack_forget()

    def show_options(self):
        self.options_frame.pack(side="right", padx=10, pady=10, fill="y",after=self.toggle_button)

    # creates checkbox
    def create_option(self, flag, variable, text_variable=None):
        option = ttk.Checkbutton(self.options_frame, text=flag["description"], variable=variable, bootstyle="round-toggle")
        option.pack(pady=5,fill="x")
        if flag.get("text"):
            frame = ttk.Frame(self.options_frame)
            frame.pack(pady=5,fill="x")
            text = ttk.Label(frame, text=flag["text_label"])
            text.grid(row=0,column=0,padx=5)
            entry = ttk.Entry(frame, textvariable=text_variable)
            entry.grid(row=0,column=1,padx=5, columnspan=2)
        return option
    
    def add_helper(self, text):
        helper = ttk.Label(self.options_frame, text=text)
        helper.pack(pady=5,fill="x")