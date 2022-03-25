from tkinter import *

THEME_COLOR = "#156db5"


class GUI_Setup:

    def __init__(self):
        self.root = Tk()
        self.root.config(width=500, height=800, bg=THEME_COLOR, pady=20, padx=20)
        self.root.iconbitmap("data/hero.ico")
        self.root.title("Hero Timer")

        self.header_label = Label()
        self.header_label.config(text="Hero Stundenzettel", pady=35, bg=THEME_COLOR,
                                 font=("Arial", 18, "bold"), fg="#ffdd00")
        self.header_label.grid(column=0, row=0)

        self.open_file_btn = Button()
        self.open_file_btn.config(text="Open File", width=30)
        self.open_file_btn.grid(column=0, row=1, pady=20)

        self.worktime_info_label = Label()
        self.worktime_info_label.config(text="Arbeitszeit in Stunden:Minuten:Sekunden",
                                        pady=10, bg=THEME_COLOR, font=("Arial", 15), fg="#ffdd00")
        self.worktime_info_label.grid(column=0, row=2)

        self.worktime_label = Label()
        self.worktime_label.config(text="00:00:00", pady=5, bg=THEME_COLOR, font=("Arial", 15))
        self.worktime_label.grid(column=0, row=3)

        self.path_label = Label()
        self.path_label.config(text="", pady=5, bg=THEME_COLOR, font=("Arial", 10))
        self.path_label.grid(column=0, row=4)


