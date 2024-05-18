import tkinter as tk
from PIL import Image, ImageTk

frameHeight = 100
menuWidth = 135
logoWidth = 340
exitWidth = 300
#tabsWidth = 1920-menuWidth-logoWidth-exitWidth
buttonWidth = 326
tabsWidth = 3*buttonWidth
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
        toolbarMenu = tk.Frame(toolbar, bg=bgColour, width=menuWidth, height=frameHeight, highlightbackground=borderColour, highlightthickness=1)
        toolbarLogo = tk.Frame(toolbar, bg=bgColour, width=logoWidth, height=frameHeight, highlightbackground=borderColour, highlightthickness=1)
        toolbarTabs = tk.Frame(toolbar, bg=bgColour, width=tabsWidth, height=frameHeight, highlightbackground=borderColour, highlightthickness=1)
        toolbarExit = tk.Frame(toolbar, bg=bgColour, width=exitWidth, height=frameHeight, highlightbackground=borderColour, highlightthickness=1)

        toolbarMenu.pack(side="left")
        toolbarLogo.pack(side="left")
        toolbarTabs.pack(side="left")
        toolbarExit.pack(side="right")

        # Obrazki
        self.menu_image = tk.PhotoImage(file=r"img\burger.png")
        self.empty_state_image = tk.PhotoImage(file=r"img\empty-state-image.png")
        self.exit_button = tk.PhotoImage(file=r"img\exit_button.png")
        self.load_data = tk.PhotoImage(file=r"img\load_data.png")

        # Przyciski
        menu_button = tk.Button(toolbarMenu, image=self.menu_image, fg="#FFFFFF", bg=bgColour, height=10, width=18, borderwidth=0, highlightthickness=0)
        logo_button = tk.Button(toolbarLogo, height=5, text="Logo", fg="#FFFFFF", bg=bgColour, width=60, borderwidth=0, highlightthickness=0)
        analButton = tk.Button(toolbarTabs, height=5, text="Analiza", fg="#FFFFFF", bg=bgColour, width=43, borderwidth=0, highlightthickness=0)
        mapButton = tk.Button(toolbarTabs, height=5, text="Mapa", fg="#FFFFFF", bg=bgColour, width=43, borderwidth=0, highlightthickness=0)
        dataButton = tk.Button(toolbarTabs, height=5, text="Dane", fg="#FFFFFF", bg=bgColour, width=43, borderwidth=0, highlightthickness=0)
        exit_button = tk.Button(toolbarExit, image=self.exit_button, height=5, fg="#FFFFFF", bg=bgColour, width=25, borderwidth=0, highlightthickness=0)


        menu_button.pack(expand=True, fill="both")
        logo_button.pack(expand=True, fill="both")
        analButton.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        mapButton.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        dataButton.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        exit_button.pack(expand=True, fill=tk.BOTH)

        menu_button.config(width=41, height=82)
        exit_button.config(width=352, height=82)

        mainScreen = tk.Frame(self, bg=bgColour, height=frameHeight, highlightbackground=borderColour, highlightthickness=1)
        mainScreen.pack(expand=True, fill="both")
        empty_screen = tk.Canvas(mainScreen, bg=bgColour, width=660, height=432, highlightthickness=0)
        empty_screen.create_image(660, 432, image=self.empty_state_image, anchor="w")
        empty_screen.pack(expand=True, fill="both")
        load_data = tk.Button(mainScreen, image=self.load_data, bg=bgColour, highlightthickness=0, borderwidth=0)
        load_data.pack(side="top", fill='y')




    def say_hello(self):
        print("sample_text")
