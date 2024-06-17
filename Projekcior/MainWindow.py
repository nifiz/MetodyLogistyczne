import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

frameHeight = 100
menuWidth = 135
logoWidth = 340
exitWidth = 220
buttonWidth = 326
tabsWidth = 3 * buttonWidth
bgColour = "#141218"
borderColour = "#6750A4"
fontColour = "#CAC4D0"
disabledfontColour = "#E6E0E9"
activeButtonBgColour = "#72668A"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Logistyka")
        self.minsize(700, 300)  # randomowe wartości póki co
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

        toolbar = tk.Frame(self, bg=bgColour, height=frameHeight, highlightbackground=borderColour,
                           highlightthickness=1)
        toolbar.pack(side="top", fill="x")
        toolbarMenu = tk.Frame(toolbar, bg=bgColour, width=menuWidth, height=frameHeight,
                               highlightbackground=borderColour)
        toolbarLogo = tk.Frame(toolbar, bg=bgColour, width=logoWidth, height=frameHeight,
                               highlightbackground=borderColour)
        toolbarTabs = tk.Frame(toolbar, bg=bgColour, width=tabsWidth, height=frameHeight,
                               highlightbackground=borderColour, highlightthickness=0)
        toolbarExit = tk.Frame(toolbar, bg=bgColour, width=exitWidth, height=frameHeight,
                               highlightbackground=borderColour, highlightthickness=0)

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
        self.map_button = tk.Button(toolbarTabs, height=5, text="Mapa", fg=fontColour, bg=bgColour, width=33,
                                    borderwidth=0,
                                    highlightthickness=0, font="Roboto", activebackground=bgColour,
                                    activeforeground=fontColour, disabledforeground=disabledfontColour,
                                    command=self.map_action, cursor="hand2")
        self.data_button = tk.Button(toolbarTabs, height=5, text="Dane", fg=fontColour, bg=bgColour, width=33,
                                     borderwidth=0,
                                     highlightthickness=0, font="Roboto", disabledforeground=disabledfontColour,
                                     activebackground=bgColour, activeforeground=fontColour, command=self.data_action,
                                     cursor="hand2")
        self.exit_button = tk.Button(toolbarExit, image=self.exit_button_img, height=5, bg=bgColour, width=15,
                                     borderwidth=0, highlightthickness=0, padx=0, pady=0, activebackground=bgColour,
                                     cursor="hand2", command=self.destroy)

        self.menu_button.pack(expand=True, fill="both", padx=15)
        self.logo_button.pack(expand=True, fill="both")
        self.anal_button.pack(side=tk.LEFT, expand=True, fill="both")
        self.map_button.pack(side=tk.LEFT, expand=True, fill="both")
        self.data_button.pack(side=tk.LEFT, expand=True, fill="both")
        self.exit_button.pack(side=tk.RIGHT, expand=True, fill="both")

        self.menu_button.config(width=41, height=82)
        self.exit_button.config(width=352, height=82)

        # Separatory czyli te kreski przy kliknieciu
        self.anal_separator = ttk.Separator(orient="horizontal")
        self.anal_separator.place(in_=self.anal_button, x=0, y=-1000, rely=1.0, height=2, relwidth=1.0)
        self.map_separator = ttk.Separator(orient="horizontal")
        self.map_separator.place(in_=self.map_button, x=0, y=-1000, rely=1.0, height=2, relwidth=1.0)
        self.data_separator = ttk.Separator(orient="horizontal")
        self.data_separator.place(in_=self.data_button, x=0, y=-1000, rely=1.0, height=2, relwidth=1.0)

        # Main frame
        self.main_frame = tk.Frame(self, bg=bgColour)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Klikniecie w burgera
        self.menu_frame = tk.Frame(self.main_frame, bg=bgColour, highlightbackground=borderColour, highlightthickness=1)

        # Przyciski po kliknieciu w burgera
        self.menu_frame1 = tk.Frame(self.menu_frame, highlightthickness=1, highlightbackground=borderColour)
        self.menu_frame2 = tk.Frame(self.menu_frame, highlightthickness=1, highlightbackground=borderColour)
        self.menu_frame3 = tk.Frame(self.menu_frame, highlightthickness=1, highlightbackground=borderColour)

        self.menu_frame1.pack(fill="x")
        self.menu_frame2.pack(fill="x")
        self.menu_frame3.pack(fill="x")

        self.menu_button1 = tk.Button(self.menu_frame1, text="Wczytaj dane", bg=bgColour, fg="white",
                                      activebackground=activeButtonBgColour, cursor="hand2", borderwidth=0,
                                      font="Roboto 12", height=2, activeforeground="white",
                                      command=self.load_data_action)
        self.menu_button2 = tk.Button(self.menu_frame2, text="Zapisz", bg=bgColour, fg="white",
                                      activebackground=activeButtonBgColour, cursor="hand2",borderwidth=0,
                                      font="Roboto 12", height=2, activeforeground="white", command=self.save_to_file)
        self.menu_button3 = tk.Button(self.menu_frame3, text="Wyjdź", bg=bgColour, fg="white",
                                      activebackground=activeButtonBgColour, cursor="hand2",borderwidth=0,
                                      font="Roboto 12", height=2, activeforeground="white", command=self.destroy)

        self.menu_button1.pack(fill="x")
        self.menu_button2.pack(fill="x")
        self.menu_button3.pack(fill="x")

        # Anal button co ma sie pojawic po kliknieciu co to za skladnia ???
        self.left_frame = tk.Frame(self.main_frame, width=300, height=600, bg="#1E1B22")
        self.plot_frame = tk.Frame(self.main_frame, bg=bgColour)

        # Data button co ma sie pojawic po kliknieciu
        self.image_label = tk.Label(self.main_frame, image=self.empty_state_image, bg=bgColour)
        #self.image_label.pack(pady=(100, 0))

        self.laduj_dane = tk.Button(self.main_frame, image=self.load_data, bg=bgColour, borderwidth=0,
                                     highlightthickness=0, activebackground=bgColour,
                                     command=self.load_data_action, cursor="hand2")
        #self.main_button.pack(pady=30)

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

    def update_main_frame(self, *new_content):
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()
        for i in new_content:
            i[0].pack(side=i[1], expand=i[2], fill=i[3], padx=i[4], pady=i[5])

    def plot_data(self, file_path):
        df = self.parser(data_file)

        fig, ax = plt.subplots(figsize=(12, 7))
        fig.patch.set_facecolor(bgColour)
        fig.patch.set_edgecolor('red')
        ax.tick_params(axis='x', colors=fontColour)
        ax.tick_params(axis='y', colors=fontColour)
        plt.xticks(np.arange(0, 460, 50))
        #ax.plot(df['date'], df['dav'], label='DAV')
        #ax.plot(df['date'], df['dane_dostaw'], label='Dane Dostaw')
        ax.plot(df['date'], df['ULG95'], label='ULG95')
        ax.plot(df['date'], df['DK'], label='DK')
        ax.plot(df['date'], df['ULTSU'], label='ULTSU')
        ax.plot(df['date'], df['ULTDK'], label='ULTDK')
        ax.grid(True, color="#332F3D")
        ax.set_facecolor(bgColour)

        ax.set_xlabel("Data", color=fontColour)
        ax.set_ylabel("Wartości", color=fontColour)
        ax.legend(loc="upper right")

        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)

    def menu_action(self):
        if self.menu_frame.winfo_ismapped():
            self.menu_frame.place_forget()
        else:
            self.menu_frame.place(x=0, y=0, relwidth=0.2)

    def save_to_file(self):
        print("save_to_file")

    def logo_action(self):
        print("logo")

    def anal_action(self):
        self.disable_button(self.anal_button, self.data_button, self.map_button)
        self.update_main_frame([self.left_frame, "left", True, None, 0, 0],
                               [self.plot_frame, "right", True, None, 0, 0])
        self.plot_data(data_file)


    def map_action(self):
        self.disable_button(self.map_button, self.data_button, self.anal_button)
        self.update_main_frame([tk.Label(self.main_frame, text="Map content here", bg=bgColour, fg=fontColour), "left", False, None, 0, 0])

    def data_action(self):
        self.disable_button(self.data_button, self.anal_button, self.map_button)
        self.update_main_frame([self.image_label, None, False, None, 0, (100, 0)],
                               [self.laduj_dane, None, False, None, 0, 30])

    @classmethod
    def parser(cls, file_path):
        df = pd.read_excel(file_path, sheet_name='Deliveries per Customer (detail', skiprows=9)

        df = df.iloc[2:460]

        # Przekształcenie kolumn na odpowiednie typy
        df["Unnamed: 0"] = df["Unnamed: 0"].astype(str)
        df["Unnamed: 2"] = df["Unnamed: 2"].astype(str)
        df["Unnamed: 3"] = df["Unnamed: 3"].astype(str)
        #df["Unnamed: 25"] = df["Unnamed: 25"].astype(float)
        df["Unnamed: 26"] = df["Unnamed: 26"].astype(float)
        df["Unnamed: 27"] = df["Unnamed: 27"].astype(float)
        df["Unnamed: 28"] = df["Unnamed: 28"].astype(float)
        df["Unnamed: 29"] = df["Unnamed: 29"].astype(float)
        df = df.iloc[2:]
        data = {
            "date": df["Unnamed: 0"],
            "dav": df["Unnamed: 2"],
            "time": df["Unnamed: 3"],
            #"dane_dostaw": df["Unnamed: 25"],
            "ULG95": df["Unnamed: 27"],
            "DK": df["Unnamed: 28"],
            "ULTSU": df["Unnamed: 29"],
            "ULTDK": df["Unnamed: 30"]
        }

        return pd.DataFrame(data)

    def load_data_action(self):
        global data_file
        data_file = filedialog.askopenfilename(title="Wybierz plik z danymi",
                                               filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])





    def say_hello(self):
        print("sample_text")
