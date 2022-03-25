from ui import GUI_Setup
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox

# -----GLOBALS-----
FILEPATH = None
DATA = None


# -----FUNCTIONS-----
def open_file_for_pd():
    global FILEPATH
    global DATA
    FILEPATH = filedialog.askopenfilename(initialdir="/", title="Wählen Sie die CSV",
                                          filetypes=(("Excel files", "*.xls"), ("Excel files", "*.xlsx")))
    try:
        DATA = pd.read_excel(FILEPATH)
    except:
        messagebox.showerror("Excel Error", "File Error, check excel data")
    else:
        calculate_worktime()


def calculate_worktime():
    hours = 0
    minutes = 0
    seconds = 0
    try:
        for time in DATA["Arbeitszeit"]:
            hours += int(time[0:2])
            minutes += int(time[3:5])
            seconds += int(time[6:8])
        minutes += int(seconds/60)
        hours += int(minutes/60)
        minutes = minutes % 60
        seconds = seconds % 60
    except:
        messagebox.showerror("Data Error", "Data error, check file")
        gui.path_label.config(text="ERROR with: " + FILEPATH)
    else:
        gui.worktime_label.config(text=str(hours) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
        gui.path_label.config(text=FILEPATH)


# -----MAIN-----
gui = GUI_Setup()
gui.open_file_btn.config(command=lambda: open_file_for_pd())
gui.root.mainloop()
