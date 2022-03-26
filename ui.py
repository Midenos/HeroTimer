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

        self.state_label = Label()
        self.state_label.config(text="Status Option", pady=5, bg=THEME_COLOR, font=("Arial", 10), fg="#ffdd00")
        self.state_label.grid(column=0, row=2, sticky="W")

        self.all_cb = Checkbutton()
        self.all_cb.config(text="Alle inkl. gelöscht & vorläufig", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.all_cb.grid(column=0, row=3, pady=5, sticky="W")

        self.bes_cb = Checkbutton()
        self.bes_cb.config(text="Bestätigt", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.bes_cb.grid(column=0, row=4, padx=00, sticky="W")

        self.pen_cb = Checkbutton()
        self.pen_cb.config(text="Eingereicht", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.pen_cb.grid(column=0, row=4, padx=95, sticky="W")

        self.worktime_info_label = Label()
        self.worktime_info_label.config(text="Arbeitszeit in Stunden:Minuten:Sekunden",
                                        pady=10, bg=THEME_COLOR, font=("Arial", 15), fg="#ffdd00")
        self.worktime_info_label.grid(column=0, row=5)

        self.worktime_label = Label()
        self.worktime_label.config(text="00:00:00", pady=5, bg=THEME_COLOR, font=("Arial", 15))
        self.worktime_label.grid(column=0, row=6)

        self.path_label = Label()
        self.path_label.config(text="", pady=5, bg=THEME_COLOR, font=("Arial", 10))
        self.path_label.grid(column=0, row=7)



