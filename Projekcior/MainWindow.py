import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text="Click me!", command=self.say_hello)
        self.btn.pack(padx=120, pady=30)

    def say_hello(self):
        print("Hello, Tkinter!")


