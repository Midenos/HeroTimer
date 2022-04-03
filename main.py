import tkinter

from ui import GUI_Setup
import pandas as pd
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import pdf

# -----GLOBALS-----
FILEPATH = None
DATA = None
# CATEGORY = ["Umsetzung", "Büro", "Homeoffice", "Schlechtwetter", "Materialfahrt", "Aufgabe", "Fahrtzeit",
#              "Projektierung", "Vor-Ort-Termin", "Besprechung", "Pause", "Privat", "Keine"]
CATEGORY = ["Umsetzung", "Aufgabe", "Projektierung", "Vor-Ort-Termin", "Keine"]
STATUS = ["Eingereicht", "Bestätigt"]
PDF_DATA = None
TIME_STR = ""


# -----FUNCTIONS-----
def open_file_for_pd():
    global FILEPATH
    global DATA
    FILEPATH = filedialog.askopenfilename(initialdir="/", title="Wählen Sie die Excel Datei",
                                          filetypes=(("Excel files", "*.xls"), ("Excel files", "*.xlsx")))
    try:
        DATA = pd.read_excel(FILEPATH)
    except FileNotFoundError:
        FILEPATH = None
        gui.path_label.config(text="Keine Datei ausgewählt")
        gui.worktime_label.config(text="00:00:00")
    except TypeError:
        FILEPATH = None
        messagebox.showerror("Excel Error", "File Error, check excel data")
    else:
        calculate_worktime()


def category_change(cat_string):
    if cat_string in CATEGORY:
        CATEGORY.remove(cat_string)
    else:
        CATEGORY.append(cat_string)
    calculate_worktime()


def status_change(stat_string):
    if stat_string in STATUS:
        STATUS.remove(stat_string)
    else:
        STATUS.append(stat_string)
    calculate_worktime()


def filter_df_by_categories(df):
    df['Kategorie'] = df['Kategorie'].fillna("Keine")
    for index, row in df.iterrows():
        if row["Kategorie"] in CATEGORY:
            pass
        else:
            df = df.drop(index)
    return df


def filter_df_by_status(df):
    for index, row in df.iterrows():
        if row["Status"] in STATUS:
            pass
        else:
            df = df.drop(index)
    return df


def calculate_worktime():
    global DATA
    global PDF_DATA
    global TIME_STR
    df = DATA
    try:
        if FILEPATH is not None:
            df = filter_df_by_categories(df)
            df = filter_df_by_status(df)
        else:
            return
        hours = 0
        minutes = 0
        seconds = 0

        for time in df["Arbeitszeit"]:
            hours += int(time[0:2])
            minutes += int(time[3:5])
            seconds += int(time[6:8])

        minutes += int(seconds / 60)
        hours += int(minutes / 60)
        minutes = minutes % 60
        seconds = seconds % 60
    except KeyError:
        messagebox.showerror("Key Error", "Schlüssel nicht gefunden")
        gui.path_label.config(text=f"ERROR with: {FILEPATH}")
        gui.worktime_label.config(text="00:00:00")
    except TypeError:
        messagebox.showerror("Type Error", "Daten konnten nicht gelesen werden")
        gui.path_label.config(text=f"ERROR with: {FILEPATH}")
        gui.worktime_label.config(text="00:00:00")
    else:
        PDF_DATA = df
        TIME_STR = str(hours) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)
        gui.worktime_label.config(text=str(hours) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2))
        gui.path_label.config(text=f"In Bearbeitung: {FILEPATH}")


def create_pdf():
    if PDF_DATA is not None:
        pdf.create_pdf(PDF_DATA, TIME_STR, gui.inp_project_name.get())
        messagebox.showinfo("PDF erzeugt", "Die PDF Datei wurde erstellt")
    else:
        messagebox.showwarning("Keine Daten", "Bitte wählen Sie zu erst Ihre Daten korrekt aus")


# -----MAIN GUI-----
gui = GUI_Setup()

cb_bes_var = IntVar(value=1)
cb_pen_var = IntVar(value=1)
cb_vor_var = IntVar(value=0)
cb_gel_var = IntVar(value=0)

cat_ums_var = IntVar(value=1)
cat_pro_var = IntVar(value=1)
cat_auf_var = IntVar(value=1)
cat_vot_var = IntVar(value=1)
cat_hom_var = IntVar(value=0)
cat_bes_var = IntVar(value=0)
cat_bue_var = IntVar(value=0)
cat_fah_var = IntVar(value=0)
cat_mat_var = IntVar(value=0)
cat_pau_var = IntVar(value=0)
cat_pri_var = IntVar(value=0)
cat_swe_var = IntVar(value=0)
cat_nan_var = IntVar(value=1)

gui.open_file_btn.config(command=lambda: open_file_for_pd())
gui.create_pdf_btn.config(command=lambda: create_pdf())
gui.option_window_btn.config(command=lambda: gui.open_option_window())

gui.bes_cb.config(variable=cb_bes_var, command=lambda: status_change("Bestätigt"))
gui.pen_cb.config(variable=cb_pen_var, command=lambda: status_change("Eingereicht"))
gui.vor_cb.config(variable=cb_vor_var, command=lambda: status_change("Vorläufig"))
gui.gel_cb.config(variable=cb_gel_var, command=lambda: status_change("Gelöscht"))

gui.cat_cb_nan.config(variable=cat_nan_var, command=lambda: category_change("Keine"))
gui.cat_cb_ums.config(variable=cat_ums_var, command=lambda: category_change("Umsetzung"))
gui.cat_cb_pro.config(variable=cat_pro_var, command=lambda: category_change("Projektierung"))
gui.cat_cb_auf.config(variable=cat_auf_var, command=lambda: category_change("Aufgabe"))
gui.cat_cb_vot.config(variable=cat_vot_var, command=lambda: category_change("Vor-Ort-Termin"))
gui.cat_cb_hom.config(variable=cat_hom_var, command=lambda: category_change("Homeoffice"))
gui.cat_cb_bes.config(variable=cat_bes_var, command=lambda: category_change("Besprechung"))
gui.cat_cb_bue.config(variable=cat_bue_var, command=lambda: category_change("Büro"))
gui.cat_cb_fah.config(variable=cat_fah_var, command=lambda: category_change("Fahrtzeit"))
gui.cat_cb_mat.config(variable=cat_mat_var, command=lambda: category_change("Materialfahrt"))
gui.cat_cb_pau.config(variable=cat_pau_var, command=lambda: category_change("Pause"))
gui.cat_cb_pri.config(variable=cat_pri_var, command=lambda: category_change("Privat"))
gui.cat_cb_swe.config(variable=cat_swe_var, command=lambda: category_change("Schlechtwetter"))

gui.root.mainloop()
