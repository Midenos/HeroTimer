from ui import GUI_Setup
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

# -----GLOBALS-----
FILEPATH = None
DATA = None
OPTION = 3


# -----FUNCTIONS-----
def open_file_for_pd():
    global FILEPATH
    global DATA
    FILEPATH = filedialog.askopenfilename(initialdir="/", title="Wählen Sie die CSV",
                                          filetypes=(("Excel files", "*.xls"), ("Excel files", "*.xlsx")))
    try:
        DATA = pd.read_excel(FILEPATH)
    except:
        FILEPATH = None
        messagebox.showerror("Excel Error", "File Error, check excel data")
    else:
        calculate_worktime()


def set_options():
    global OPTION
    if cb_all_var.get() == 1:
        OPTION = 0
        cb_bes_var.set(1)
        cb_pen_var.set(1)
    elif cb_pen_var.get() == 1 and cb_bes_var.get() == 1:
        OPTION = 3
        cb_all_var.set(0)
    elif cb_bes_var.get() == 1:
        OPTION = 1
        cb_all_var.set(0)
    elif cb_pen_var.get() == 1:
        OPTION = 2
        cb_all_var.set(0)
    else:
        OPTION = -1
    if FILEPATH is not None:
        calculate_worktime()


def calculate_worktime():
    hours = 0
    minutes = 0
    seconds = 0
    try:
        if OPTION == -1:
            gui.worktime_label.config(text="00:00:00")
            gui.path_label.config(text="In Bearbeitung: " + FILEPATH)
            return
        if OPTION == 0:
            for time in DATA["Arbeitszeit"]:
                hours += int(time[0:2])
                minutes += int(time[3:5])
                seconds += int(time[6:8])
        elif OPTION == 1:
            for index, row in DATA.iterrows():
                if row["Status"] == "Bestätigt":
                    hours += int(row["Arbeitszeit"][0:2])
                    minutes += int(row["Arbeitszeit"][3:5])
                    seconds += int(row["Arbeitszeit"][6:8])
        elif OPTION == 2:
            for index, row in DATA.iterrows():
                if row["Status"] == "Eingereicht":
                    hours += int(row["Arbeitszeit"][0:2])
                    minutes += int(row["Arbeitszeit"][3:5])
                    seconds += int(row["Arbeitszeit"][6:8])
        elif OPTION == 3:
            for index, row in DATA.iterrows():
                if row["Status"] == "Bestätigt" or row["Status"] == "Eingereicht":
                    hours += int(row["Arbeitszeit"][0:2])
                    minutes += int(row["Arbeitszeit"][3:5])
                    seconds += int(row["Arbeitszeit"][6:8])
        minutes += int(seconds / 60)
        hours += int(minutes / 60)
        minutes = minutes % 60
        seconds = seconds % 60
    except:
        messagebox.showerror("Data Error", "Data error, check file")
        gui.path_label.config(text="ERROR with: " + FILEPATH)
    else:
        gui.worktime_label.config(text=str(hours) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
        gui.path_label.config(text="In Bearbeitung: " + FILEPATH)


# -----MAIN-----
gui = GUI_Setup()
cb_all_var = IntVar()
cb_bes_var = IntVar()
cb_pen_var = IntVar()
gui.open_file_btn.config(command=lambda: open_file_for_pd())
gui.all_cb.config(variable=cb_all_var, command=lambda: set_options())
gui.bes_cb.config(variable=cb_bes_var, command=lambda: set_options())
gui.pen_cb.config(variable=cb_pen_var, command=lambda: set_options())
cb_all_var.set(0)
cb_pen_var.set(1)
cb_bes_var.set(1)
gui.root.mainloop()
