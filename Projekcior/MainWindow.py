import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Logistyka")
        self.minsize(700, 300) # randomowe wartości póki co
        self.maxsize(1920, 1080)
        self.geometry("1920x1080")
        self.configure(background="#141218")
        self.state("zoomed")

    def say_hello(self):
        print("sample_text")
