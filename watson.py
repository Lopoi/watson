import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sys
import os
from console import *
from options import *
import flags as flags

import sherlock
from result import QueryResult

class Watson:
    def __init__(self, window):
        self.window = window
        self.window.title("Watson")

        self.build_gui()

    def prepare_command(self):
        username = self.username.get()
        args = ["sherlock", username]
        for flag in flags.flags:
            if self.option_values[flag["name"]].get():
                args.append(flag["name"])
                if(flag.get("text")):
                    args.append(self.option_params[flag["name"]].get())
        sys.argv = args

    def print_command(self):
        self.prepare_command()
        print("Command: ")
        print(" ".join(sys.argv))
        #print("Why are you even here?")

    def search_user(self):
        print("Preparing to search username...")
        self.prepare_command()
        sherlock.main()

    def build_gui(self):
        self.title = ttk.Label(self.window, text="Username: ")
        self.title.pack(pady=5)

        self.username = ttk.Entry(self.window)
        self.username.pack(pady=10, padx=10, fill="x")

        self.button_frame = ttk.Frame(self.window)
        self.button_frame.pack(pady=5)

        self.search_button = ttk.Button(self.button_frame, text="Begin Search", bootstyle=SUCCESS, command=self.search_user)
        self.search_button.pack(padx=5, pady=10, side="left")

        self.print_button = ttk.Button(self.button_frame, text="Print Command", bootstyle=PRIMARY, command=self.print_command)
        self.print_button.pack(padx=5, pady=10, side="right")

        self.options = Options(self.window)
        self.option_values = {}
        self.option_params = {}
        for flag in flags.flags:
            self.option_values[flag["name"]] = tk.BooleanVar()
            self.option_params[flag["name"]] = None
            # If the flag has a text field, create a StringVar for it
            if(flag.get("text")):
                self.option_params[flag["name"]] = tk.StringVar()
            self.options.create_option(flag, self.option_values[flag["name"]], self.option_params[flag["name"]])
        self.options.add_helper("Note: Not all options are compatible with each other. Please use them at your own risk.")

        self.console = ConsoleApp(self.window)


root = tk.Tk()
root.title("Watson")

watson = Watson(root)

root.mainloop()