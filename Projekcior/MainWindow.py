import tkinter as tk

frameHeight = 65
menuWidth = 80
logoWidth = 200
exitWidth = 160
tabsWidth = 1920-menuWidth-logoWidth-exitWidth
bgColour = "#141218"
borderColour = "#6750A4"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Logistyka")
        self.minsize(700, 300) # randomowe wartości póki co
        self.maxsize(1920, 1080)
        self.geometry("1920x1080")
        self.configure(background=bgColour)
        self.state("zoomed")

        toolbar = tk.Frame(self, bg=bgColour, height=frameHeight, highlightbackground=borderColour, highlightthickness=1)
        toolbar.pack(side="top", fill="x")
        toolbarMenu = tk.Frame(toolbar, bg=bgColour, height=frameHeight, width=menuWidth, highlightbackground=borderColour, highlightthickness=1)
        toolbarLogo = tk.Frame(toolbar, bg=bgColour, height=frameHeight, width=logoWidth, highlightbackground=borderColour, highlightthickness=1)
        toolbarTabs = tk.Frame(toolbar, bg=bgColour, height=frameHeight, width=tabsWidth, highlightbackground=borderColour, highlightthickness=1)
        toolbarExit = tk.Frame(toolbar, bg=bgColour, height=frameHeight, width=exitWidth, highlightbackground=borderColour, highlightthickness=1)
        toolbarMenu.pack(side="left")
        toolbarLogo.pack(side="left")
        toolbarExit.pack(side="right")
        toolbarTabs.pack(side="right", expand=True)

    def say_hello(self):
        print("sample_text")
