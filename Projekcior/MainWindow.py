import tkinter as tk

frameHeight = 100
menuWidth = 135
logoWidth = 340
exitWidth = 220
buttonWidth = 326
tabsWidth = 3*buttonWidth
bgColour = "#141218"
borderColour = "#6750A4"
fontColour = "#CAC4D0"

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Logistyka")
        self.minsize(700, 300) # randomowe wartości póki co
        self.maxsize(1920, 1080)
        self.geometry("1920x1080")
        self.configure(background=bgColour)
        self.state("zoomed")

        # Zeby sie nie psulo przy zumie
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except Exception as e:
            print(e)

        toolbar = tk.Frame(self, bg=bgColour, height=frameHeight, highlightbackground=borderColour, highlightthickness=1)
        toolbar.pack(side="top", fill="x")
        toolbarMenu = tk.Frame(toolbar, bg=bgColour, width=menuWidth, height=frameHeight, highlightbackground=borderColour)
        toolbarLogo = tk.Frame(toolbar, bg=bgColour, width=logoWidth, height=frameHeight, highlightbackground=borderColour)
        toolbarTabs = tk.Frame(toolbar, bg=bgColour, width=tabsWidth, height=frameHeight, highlightbackground=borderColour, highlightthickness=0)
        toolbarExit = tk.Frame(toolbar, bg=bgColour, width=exitWidth, height=frameHeight, highlightbackground=borderColour, highlightthickness=0)

        toolbarMenu.pack(side="left")
        toolbarLogo.pack(side="left")
        toolbarTabs.pack(side="left")
        toolbarExit.pack(side="right")
        toolbarExit.propagate(False)

        # Obrazki
        self.menu_image = tk.PhotoImage(file=r"img\burger.png")
        self.empty_state_image = tk.PhotoImage(file=r"img\empty-state-image.png")
        self.exit_button = tk.PhotoImage(file=r"img\exit_button.png")
        self.load_data = tk.PhotoImage(file=r"img\load_data.png")

        # Przyciski
        menu_button = tk.Button(toolbarMenu, image=self.menu_image, bg=bgColour, height=15, width=18,
                                highlightthickness=0, borderwidth=0)
        logo_button = tk.Button(toolbarLogo, height=5, text="Paliwska", fg="white", bg=bgColour,
                                width=40, borderwidth=0, highlightthickness=0, font="Roboto 12 bold")
        analButton = tk.Button(toolbarTabs, height=5, text="Analiza", fg=fontColour, bg=bgColour, width=33,
                               borderwidth=0, highlightthickness=0, font="Roboto")
        mapButton = tk.Button(toolbarTabs, height=5, text="Mapa", fg=fontColour, bg=bgColour, width=33, borderwidth=0,
                              highlightthickness=0, font="Roboto")
        dataButton = tk.Button(toolbarTabs, height=5, text="Dane", fg=fontColour, bg=bgColour, width=33, borderwidth=0,
                               highlightthickness=0, font="Roboto")
        exit_button = tk.Button(toolbarExit, image=self.exit_button, height=5, bg=bgColour, width=15,
                                borderwidth=0, highlightthickness=0, padx=0, pady=0)


        menu_button.pack(expand=True, fill="both", padx=15)
        logo_button.pack(expand=True, fill="both")
        analButton.pack(side=tk.LEFT, expand=True, fill="both")
        mapButton.pack(side=tk.LEFT, expand=True, fill="both")
        dataButton.pack(side=tk.LEFT, expand=True, fill="both")
        exit_button.pack(side=tk.RIGHT, expand=True, fill="both")

        menu_button.config(width=41, height=82)
        exit_button.config(width=352, height=82)


        self.main_frame = tk.Frame(self, bg=bgColour)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.image_label = tk.Label(self.main_frame, image=self.empty_state_image, bg=bgColour)
        self.image_label.pack(pady=(100, 0))

        self.main_button = tk.Button(self.main_frame, image=self.load_data, bg=bgColour, borderwidth=0, highlightthickness=0)
        self.main_button.pack(pady=30)


    def say_hello(self):
        print("sample_text")
