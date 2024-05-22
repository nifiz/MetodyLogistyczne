import tkinter as tk
from tkinter import ttk

frameHeight = 100
menuWidth = 135
logoWidth = 340
exitWidth = 220
buttonWidth = 326
tabsWidth = 3*buttonWidth
bgColour = "#141218"
borderColour = "#6750A4"
fontColour = "#CAC4D0"
disabledfontColour ="#E6E0E9"

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
        self.exit_button_img = tk.PhotoImage(file=r"img\exit_button.png")
        self.load_data = tk.PhotoImage(file=r"img\load_data.png")

        # Przyciski
        self.menu_button = tk.Button(toolbarMenu, image=self.menu_image, bg=bgColour, height=15, width=18,
                                highlightthickness=0, borderwidth=0, activebackground=bgColour,
                                command=self.menu_action, cursor="hand2")
        self.logo_button = tk.Button(toolbarLogo, height=5, text="Paliwska", fg="white", bg=bgColour,
                                width=40, borderwidth=0, highlightthickness=0, font="Roboto 12 bold",
                                activebackground=bgColour, activeforeground="white",
                                command=self.logo_action, cursor="hand2")
        self.anal_button = tk.Button(toolbarTabs, height=5, text="Analiza", fg=fontColour, bg=bgColour, width=33,
                                borderwidth=0, highlightthickness=0, font="Roboto", activebackground=bgColour,
                                activeforeground=fontColour, disabledforeground=disabledfontColour,
                                command=self.anal_action, cursor="hand2")
        self.map_button = tk.Button(toolbarTabs, height=5, text="Mapa", fg=fontColour, bg=bgColour, width=33, borderwidth=0,
                               highlightthickness=0, font="Roboto", activebackground=bgColour,
                               activeforeground=fontColour,  disabledforeground=disabledfontColour,
                               command=self.map_action, cursor="hand2")
        self.data_button = tk.Button(toolbarTabs, height=5, text="Dane", fg=fontColour, bg=bgColour, width=33, borderwidth=0,
                               highlightthickness=0, font="Roboto",  disabledforeground=disabledfontColour, activebackground=bgColour,
                               activeforeground=fontColour, command=self.data_action, cursor="hand2")
        self.exit_button = tk.Button(toolbarExit, image=self.exit_button_img, height=5, bg=bgColour, width=15,
                                borderwidth=0, highlightthickness=0, padx=0, pady=0, activebackground=bgColour,
                                cursor="hand2")

        self.menu_button.pack(expand=True, fill="both", padx=15)
        self.logo_button.pack(expand=True, fill="both")
        self.anal_button.pack(side=tk.LEFT, expand=True, fill="both")
        self.map_button.pack(side=tk.LEFT, expand=True, fill="both")
        self.data_button.pack(side=tk.LEFT, expand=True, fill="both")
        self.exit_button.pack(side=tk.RIGHT, expand=True, fill="both")

        self.menu_button.config(width=41, height=82)
        self.exit_button.config(width=352, height=82)

        #Separatory czyli te kreski przy kliknieciu
        self.anal_separator = ttk.Separator(orient="horizontal")
        self.anal_separator.place(in_=self.anal_button, x=0, y=-1000, rely=1.0, height=2, relwidth=1.0)
        self.map_separator = ttk.Separator(orient="horizontal")
        self.map_separator.place(in_=self.map_button, x=0, y=-1000, rely=1.0, height=2, relwidth=1.0)
        self.data_separator = ttk.Separator(orient="horizontal")
        self.data_separator.place(in_=self.data_button, x=0, y=-1000, rely=1.0, height=2, relwidth=1.0)

        # Main frame
        self.main_frame = tk.Frame(self, bg=bgColour)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        self.image_label = tk.Label(self.main_frame, image=self.empty_state_image, bg=bgColour)
        self.image_label.pack(pady=(100, 0))

        self.main_button = tk.Button(self.main_frame, image=self.load_data, bg=bgColour, borderwidth=0,
                                     highlightthickness=0, activebackground=bgColour,
                                     command=self.load_data_action, cursor="hand2")
        self.main_button.pack(pady=30)

    # Funkcje
    def get_separator(self, button):
        if button == self.anal_button:
            return self.anal_separator
        elif button == self.map_button:
            return self.map_separator
        elif button == self.data_button:
            return self.data_separator

    def disable_button(self, button, *buttons):
        button.config(state=tk.DISABLED, cursor="")
        self.enable_buttons(*buttons)
        separator = self.get_separator(button)
        separator.place_configure(rely=1.0, y=1)

    def enable_buttons(self, *buttons):
        for button in buttons:
            button.config(state=tk.NORMAL, cursor="hand2")
            separator = self.get_separator(button)
            separator.place_configure(rely=1.0, y=-1000)

    def menu_action(self):
        print("Menu")

    def logo_action(self):
        print("logo")

    def anal_action(self):
        self.disable_button(self.anal_button, self.data_button, self.map_button)

    def map_action(self):
        self.disable_button(self.map_button, self.data_button, self.anal_button)


    def data_action(self):
        self.disable_button(self.data_button, self.anal_button, self.map_button)

    def load_data_action(self):
        print("load_data")

    def say_hello(self):
        print("sample_text")
