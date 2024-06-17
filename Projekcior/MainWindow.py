import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import Prawdopodobienstwa

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
predictedDays = 20

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Logistyka")
        self.minsize(700, 300)  # randomowe wartości póki co
        self.maxsize(1920, 1080)
        self.geometry("1920x1080")
        self.configure(background=bgColour)
        self.state("zoomed")
        self.x_axis_titles_enabled = True
        self.y_axis_titles_enabled = True
        self.legend_enabled = True
        self.fig = None

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
        self.switch_on_img = tk.PhotoImage(file=r"img\Switch-on.png")
        self.switch_off_img = tk.PhotoImage(file=r"img\Switch-off.png")

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
                                      activebackground=activeButtonBgColour, cursor="hand2", borderwidth=0,
                                      font="Roboto 12", height=2, activeforeground="white", command=self.save_to_file)
        self.menu_button3 = tk.Button(self.menu_frame3, text="Wyjdź", bg=bgColour, fg="white",
                                      activebackground=activeButtonBgColour, cursor="hand2", borderwidth=0,
                                      font="Roboto 12", height=2, activeforeground="white", command=self.destroy)

        self.menu_button1.pack(fill="x")
        self.menu_button2.pack(fill="x")
        self.menu_button3.pack(fill="x")


        # Anal button - co ma sie pojawic po kliknieciu co to za skladnia ???; nie wiem?-adrian
        self.main_anal_frame = tk.Frame(self, bg="#141218")
        self.left_anal_frame = tk.Frame(self.main_anal_frame, width=400, height=400, bg="#1D1A20", pady=75)

        self.entry_frame = tk.Frame(self.left_anal_frame, bg="#36343B", pady=10, width=200, height=120)
        self.entry_frame.pack(side="top")
        self.entry_label = tk.Label(self.entry_frame, text="Liczba dni", bg="#36343B", fg="#E6E0E9")
        self.entry_label.pack(side="left", padx=(0, 5))
        self.entry = tk.Entry(self.entry_frame, bg="#36343B", fg="#E6E0E9", insertbackground="#36343B", relief="flat", textvariable=tk.StringVar())
        self.entry.pack(side="left")
        self.entry.insert(0,"20")

        self.entry_btn_frame = tk.Frame(self.left_anal_frame, width=10, height=10, bg="#1D1A20", pady=10)
        self.entry_button = tk.Button(self.entry_btn_frame, bg="#4A4458", fg="white", width=20, borderwidth=0,
                                        activebackground=activeButtonBgColour, cursor="hand2", text="aktualizuj wykres",
                                        height=2, activeforeground="white", command=self.update_plot)
        self.entry_btn_frame.pack(side="top", pady=5, padx=10)
        self.entry_button.pack(side="top", pady=10, padx=10)

        self.first_btn_frame = tk.Frame(self.left_anal_frame, width=200, height=100, bg="#1D1A20", pady=10)
        self.config_button1_label = tk.Label(self.first_btn_frame, text="Tytuł osi X", bg="#4A4458", fg="#E8DEF8")
        self.config_button1 = tk.Button(self.first_btn_frame, bg="#1D1A20", fg="white", width=60, borderwidth=0,
                                      activebackground=activeButtonBgColour, cursor="hand2", image=self.switch_on_img,
                                      height=30, activeforeground="white", command=self.disable_x_axis_titles)
        self.first_btn_frame.pack(side="top", fill="x", pady=5)
        self.config_button1.pack(side="right", pady=10, padx=10)
        self.config_button1_label.pack(side="left", pady=10, padx=10)

        self.second_btn_frame = tk.Frame(self.left_anal_frame, width=200, height=100, bg="#1D1A20", pady=10)
        self.config_button2_label = tk.Label(self.second_btn_frame, text="Tytuł osi Y", bg="#4A4458", fg="#E8DEF8")
        self.config_button2 = tk.Button(self.second_btn_frame, bg="#1D1A20", fg="white", width=60, borderwidth=0,
                                        activebackground=activeButtonBgColour, cursor="hand2", image=self.switch_on_img,
                                        height=30, activeforeground="white", command=self.disable_y_axis_titles)
        self.second_btn_frame.pack(side="top", fill="x", pady=5)
        self.config_button2.pack(side="right", pady=10, padx=10)
        self.config_button2_label.pack(side="left", pady=10, padx=10)

        self.third_btn_frame = tk.Frame(self.left_anal_frame, width=200, height=100, bg="#1D1A20", pady=10)
        self.config_button3_label = tk.Label(self.third_btn_frame, text="Legenda", bg="#4A4458", fg="#E8DEF8")
        self.config_button3 = tk.Button(self.third_btn_frame, bg="#1D1A20", fg="white", width=60, borderwidth=0,
                                        activebackground=activeButtonBgColour, cursor="hand2", image=self.switch_on_img,
                                        height=30, activeforeground="white", command=self.toggle_legend)
        self.third_btn_frame.pack(side="top", fill="x", pady=5)
        self.config_button3.pack(side="right", pady=10, padx=10)
        self.config_button3_label.pack(side="left", pady=10, padx=10)

        self.plot_anal_frame = tk.Frame(self.main_anal_frame, width=300, height=600, bg="#FFFFFF")
        # self.plot_anal_frame.pack(side="right", fill="both", expand=True)


        # Data button - co ma sie pojawic po kliknieciu
        self.image_label = tk.Label(self.main_frame, image=self.empty_state_image, bg=bgColour)
        # self.image_label.pack(pady=(100, 0))

        self.laduj_dane = tk.Button(self.main_frame, image=self.load_data, bg=bgColour, borderwidth=0,
                                    highlightthickness=0, activebackground=bgColour,
                                    command=self.load_data_action, cursor="hand2")
        # self.main_button.pack(pady=30)

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
        # ax.plot(df['date'], df['dav'], label='DAV')
        # ax.plot(df['date'], df['dane_dostaw'], label='Dane Dostaw')
        ax.plot(df['date'], df['ULG95'], label='ULG95')
        ax.plot(df['date'], df['DK'], label='DK')
        ax.plot(df['date'], df['ULTSU'], label='ULTSU')
        ax.plot(df['date'], df['ULTDK'], label='ULTDK')
        ax.grid(True, color="#332F3D")
        ax.set_facecolor(bgColour)

        ax.set_xlabel("Data", color=fontColour)
        ax.set_ylabel("Wartości", color=fontColour)
        ax.legend(loc="upper right")

        for widget in self.plot_anal_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_anal_frame)
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
        self.update_main_frame([self.main_anal_frame, None, True, "both", 0, 0],
                               [self.left_anal_frame, "left", True, None, 0, 0],
                               [self.plot_anal_frame, "right", True, "both", 0, 0])
        self.create_anal_content(predictedDays)

    def map_action(self):
        self.main_anal_frame.pack_forget()
        self.disable_button(self.map_button, self.data_button, self.anal_button)
        self.update_main_frame(
            [tk.Label(self.main_frame, text="Map content here", bg=bgColour, fg=fontColour), "left", False, None, 0, 0])

    def data_action(self):
        self.main_anal_frame.pack_forget()
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
        # df["Unnamed: 25"] = df["Unnamed: 25"].astype(float)
        df["Unnamed: 26"] = df["Unnamed: 26"].astype(float)
        df["Unnamed: 27"] = df["Unnamed: 27"].astype(float)
        df["Unnamed: 28"] = df["Unnamed: 28"].astype(float)
        df["Unnamed: 29"] = df["Unnamed: 29"].astype(float)
        df = df.iloc[2:]
        data = {
            "date": df["Unnamed: 0"],
            "dav": df["Unnamed: 2"],
            "time": df["Unnamed: 3"],
            # "dane_dostaw": df["Unnamed: 25"],
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

    def create_anal_content(self, days):
        data = Prawdopodobienstwa.TOTAL(days)
        print(days)

        categories = ['TOTAL', 'ULG95', 'DK', 'ULTSU', 'ULTDK']
        transformed_data = {category: [] for category in categories}

        for key in data:
            for entry in data[key]:
                for category in categories:
                    if category in entry:
                        transformed_data[category].append(entry[category])

        colors = ['blue', 'green', 'red', 'purple', 'orange']

        if self.fig is not None:
            plt.close(self.fig)  # Zamknięcie poprzedniego wykresu
            print("usuniety wykres")

        self.fig, axs = plt.subplots(len(categories), figsize=(10, 12))

        for idx, category in enumerate(categories):
            axs[idx].plot(range(1, days + 1), transformed_data[category], marker='o', label=category, color=colors[idx])
            axs[idx].set_xlim(1, days)
            axs[idx].set_xlabel('Dni dostaw')
            axs[idx].set_ylabel('Dane dostaw')
            axs[idx].legend()
            axs[idx].xaxis.set_major_locator(plt.MaxNLocator(integer=True))

        plt.tight_layout()

        # Usuń poprzednie płótno, jeśli istnieje
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
            print("usuniete plotno")

        # Osadzanie wykresu w Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_anal_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def create_date_picker(self, label_text):
        frame = tk.Frame(self.left_anal_frame, bg="#36343B", pady=10)

        label = tk.Label(frame, text=label_text, bg="#36343B", fg="#E6E0E9")
        label.pack(side="left", padx=(0, 5))

        self.entry = tk.Entry(frame, bg="#36343B", fg="#E6E0E9", insertbackground="#36343B", relief="flat")
        self.entry.pack(side="left", expand=True)

        return frame

    def disable_x_axis_titles(self):
        self.switch_on_img1 = tk.PhotoImage(file=r"img\Switch-on.png")
        self.switch_off_img1 = tk.PhotoImage(file=r"img\Switch-off.png")

        self.x_axis_titles_enabled = not self.x_axis_titles_enabled  # Przełącz stan

        if self.x_axis_titles_enabled:
            self.config_button1.config(image=self.switch_on_img1)
        else:
            self.config_button1.config(image=self.switch_off_img1)

        for ax in self.fig.axes:
            if self.x_axis_titles_enabled:
                ax.set_xlabel('Dni dostaw')
            else:
                ax.set_xlabel('')  # Ustaw pusty tytuł dla osi X

        self.fig.canvas.draw_idle()  # Odśwież wykres po zmianach

    def disable_y_axis_titles(self):
        self.switch_on_img2 = tk.PhotoImage(file=r"img\Switch-on.png")
        self.switch_off_img2 = tk.PhotoImage(file=r"img\Switch-off.png")

        self.y_axis_titles_enabled = not self.y_axis_titles_enabled  # Przełącz stan

        if self.y_axis_titles_enabled:
            self.config_button2.config(image=self.switch_on_img2)
        else:
            self.config_button2.config(image=self.switch_off_img2)

        for ax in self.fig.axes:
            if self.y_axis_titles_enabled:
                ax.set_ylabel('Dane dostaw')
            else:
                ax.set_ylabel('')  # Ustaw pusty tytuł dla osi Y

        self.fig.canvas.draw_idle()  # Odśwież wykres po zmianach

    def toggle_legend(self):
        self.switch_on_img3 = tk.PhotoImage(file=r"img\Switch-on.png")
        self.switch_off_img3 = tk.PhotoImage(file=r"img\Switch-off.png")

        self.legend_enabled = not self.legend_enabled  # Przełącz stan legendy

        if self.legend_enabled:
            self.config_button3.config(image=self.switch_on_img3)
        else:
            self.config_button3.config(image=self.switch_off_img3)

        for ax in self.fig.axes:
            if self.legend_enabled:
                ax.legend().set_visible(True)
            else:
                ax.legend().set_visible(False)

        self.fig.canvas.draw_idle()  # Odśwież wykres po zmianach

    def update_plot(self):
        try:
            days = int(self.entry.get())
            self.create_anal_content(days)
        except ValueError:
            print("Proszę wprowadzić prawidłową liczbę dni.")
