from tkinter import *
import pdf

# -----GLOBALS-----
THEME_COLOR = "#156db5"


class GUI_Setup:
    # -----Main Window Setup-----
    def __init__(self):
        # -----Option Window Init-----
        self.use_site_cb = None
        self.use_site_var = None
        self.use_sign_cb = None
        self.use_sign_var = None
        self.use_logo_var = None
        self.use_logo_cb = None
        self.logo_size_entry = None
        self.logo_y_entry = None
        self.logo_x_entry = None
        self.save_options_btn = None
        self.company_plz_entry = None
        self.company_name_entry = None
        self.company_street_entry = None

        # -----Main Window Init-----
        self.root = Tk()
        self.root.config(bg=THEME_COLOR, pady=20, padx=20)
        self.root.minsize(500, 590)
        self.root.iconbitmap("data/hero.ico")
        self.root.title("Hero Timer")

        self.header_label = Label()
        self.header_label.config(text="Hero Stundenzettel", bg=THEME_COLOR, font=("Arial", 18, "bold"), fg="#ffdd00")
        self.header_label.place(x=225, y=20, anchor=CENTER)

        self.open_file_btn = Button()
        self.open_file_btn.config(text="Datei öffnen", width=30)
        self.open_file_btn.place(x=225, y=70, anchor=CENTER)

        self.state_label = Label()
        self.state_label.config(text="Status Option", bg=THEME_COLOR, font=("Arial", 10), fg="#ffdd00")
        self.state_label.place(x=10, y=140, anchor="w")

        self.bes_cb = Checkbutton()
        self.bes_cb.config(text="Bestätigt", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.bes_cb.place(x=10, y=170, anchor="w")

        self.pen_cb = Checkbutton()
        self.pen_cb.config(text="Eingereicht", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.pen_cb.place(x=110, y=170, anchor="w")

        self.vor_cb = Checkbutton()
        self.vor_cb.config(text="Vorläufig", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.vor_cb.place(x=210, y=170, anchor="w")

        self.gel_cb = Checkbutton()
        self.gel_cb.config(text="Gelöscht", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.gel_cb.place(x=310, y=170, anchor="w")

        self.cat_label = Label()
        self.cat_label.config(text="Kategorie Option", bg=THEME_COLOR, font=("Arial", 10), fg="#ffdd00")
        self.cat_label.place(x=10, y=220, anchor="w")

        self.cat_cb_nan = Checkbutton()
        self.cat_cb_nan.config(text="Ohne Kategorie", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_nan.place(x=10, y=250, anchor="w")

        self.cat_cb_ums = Checkbutton()
        self.cat_cb_ums.config(text="Umsetzung", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_ums.place(x=10, y=280, anchor="w")

        self.cat_cb_pro = Checkbutton()
        self.cat_cb_pro.config(text="Projektierung", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_pro.place(x=110, y=280, anchor="w")

        self.cat_cb_auf = Checkbutton()
        self.cat_cb_auf.config(text="Aufgabe", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_auf.place(x=210, y=280, anchor="w")

        self.cat_cb_vot = Checkbutton()
        self.cat_cb_vot.config(text="Vor-Ort-Termin", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_vot.place(x=310, y=280, anchor="w")

        self.cat_cb_bue = Checkbutton()
        self.cat_cb_bue.config(text="Büro", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_bue.place(x=110, y=340, anchor="w")

        self.cat_cb_fah = Checkbutton()
        self.cat_cb_fah.config(text="Fahrzeit", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_fah.place(x=110, y=310, anchor="w")

        self.cat_cb_bes = Checkbutton()
        self.cat_cb_bes.config(text="Besprechung", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_bes.place(x=210, y=310, anchor="w")

        self.cat_cb_hom = Checkbutton()
        self.cat_cb_hom.config(text="Homeoffice", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_hom.place(x=310, y=310, anchor="w")

        self.cat_cb_pau = Checkbutton()
        self.cat_cb_pau.config(text="Pause", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_pau.place(x=10, y=340, anchor="w")

        self.cat_cb_mat = Checkbutton()
        self.cat_cb_mat.config(text="Materialfahrt", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_mat.place(x=10, y=310, anchor="w")

        self.cat_cb_pri = Checkbutton()
        self.cat_cb_pri.config(text="Privat", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_pri.place(x=210, y=340, anchor="w")

        self.cat_cb_swe = Checkbutton()
        self.cat_cb_swe.config(text="Schlechtwetter", bg=THEME_COLOR, highlightcolor=THEME_COLOR)
        self.cat_cb_swe.place(x=310, y=340, anchor="w")

        self.worktime_info_label = Label()
        self.worktime_info_label.config(text="Arbeitszeit in Stunden:Minuten:Sekunden",
                                        bg=THEME_COLOR, font=("Arial", 15), fg="#ffdd00")
        self.worktime_info_label.place(x=225, y=380, anchor=CENTER)

        self.worktime_label = Label()
        self.worktime_label.config(text="00:00:00", bg=THEME_COLOR, font=("Arial", 15))
        self.worktime_label.place(x=225, y=420, anchor=CENTER)

        self.path_label = Label()
        self.path_label.config(text="", bg=THEME_COLOR, font=("Arial", 10))
        self.path_label.place(x=225, y=100, anchor=CENTER)

        self.project_label = Label()
        self.project_label.config(text="Projekt und Dateiname:", bg=THEME_COLOR, font=("Arial", 10))
        self.project_label.place(x=225, y=490, anchor=CENTER)

        self.inp_project_name = Entry()
        self.inp_project_name.config(width=36)
        self.inp_project_name.place(x=225, y=510, anchor=CENTER)

        self.create_pdf_btn = Button()
        self.create_pdf_btn.config(text="Erstelle PDF", width=20)
        self.create_pdf_btn.place(x=300, y=540, anchor=CENTER)

        self.option_window_btn = Button()
        self.option_window_btn.config(text="Optionen", width=20)
        self.option_window_btn.place(x=150, y=540, anchor=CENTER)

    # -----Option Window Setup-----
    def open_option_window(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, Toplevel):
                return

        self.use_logo_var = IntVar()
        self.use_sign_var = IntVar()
        self.use_site_var = IntVar()

        options_window = Toplevel(self.root)
        options_window.config(bg=THEME_COLOR, pady=20, padx=20)
        options_window.geometry("400x400")
        options_window.iconbitmap("data/hero.ico")
        options_window.title("Optionen")

        options_company_label = Label(options_window)
        options_company_label.config(text="Firmendaten", bg=THEME_COLOR, font=("Arial", 12), fg="#ffdd00")
        options_company_label.place(x=190, y=10, anchor=CENTER)

        options_logo_label = Label(options_window)
        options_logo_label.config(text="Logo Einstellungen", bg=THEME_COLOR, font=("Arial", 12), fg="#ffdd00")
        options_logo_label.place(x=190, y=120, anchor=CENTER)

        options_other_label = Label(options_window)
        options_other_label.config(text="Andere Einstellungen", bg=THEME_COLOR, font=("Arial", 12), fg="#ffdd00")
        options_other_label.place(x=190, y=250, anchor=CENTER)

        self.company_name_entry = Entry(options_window)
        self.company_name_entry.insert(0, string=pdf.COMPANY_DATA[0])
        self.company_name_entry.config(width=40)
        self.company_name_entry.place(x=10, y=40, anchor="w")

        self.company_street_entry = Entry(options_window)
        self.company_street_entry.insert(0, string=pdf.COMPANY_DATA[1])
        self.company_street_entry.config(width=40)
        self.company_street_entry.place(x=10, y=60, anchor="w")

        self.company_plz_entry = Entry(options_window)
        self.company_plz_entry.insert(0, string=pdf.COMPANY_DATA[2])
        self.company_plz_entry.config(width=40)
        self.company_plz_entry.place(x=10, y=80, anchor="w")

        self.logo_x_entry = Entry(options_window)
        self.logo_x_entry.insert(0, string=pdf.COMPANY_DATA[4])
        self.logo_x_entry.config(width=5)
        self.logo_x_entry.place(x=10, y=150, anchor="w")

        logo_x_label = Label(options_window)
        logo_x_label.config(text="X - Position", bg=THEME_COLOR, font=("Arial", 10))
        logo_x_label.place(x=90, y=150, anchor=CENTER)

        self.logo_y_entry = Entry(options_window)
        self.logo_y_entry.insert(0, string=pdf.COMPANY_DATA[5])
        self.logo_y_entry.config(width=5)
        self.logo_y_entry.place(x=10, y=170, anchor="w")

        logo_y_label = Label(options_window)
        logo_y_label.config(text="Y - Position", bg=THEME_COLOR, font=("Arial", 10))
        logo_y_label.place(x=90, y=170, anchor=CENTER)

        self.logo_size_entry = Entry(options_window)
        self.logo_size_entry.insert(0, string=pdf.COMPANY_DATA[3])
        self.logo_size_entry.config(width=5)
        self.logo_size_entry.place(x=10, y=190, anchor="w")

        logo_size_label = Label(options_window)
        logo_size_label.config(text="Größe des Logos", bg=THEME_COLOR, font=("Arial", 10))
        logo_size_label.place(x=106, y=190, anchor=CENTER)

        self.use_logo_cb = Checkbutton(options_window)
        self.use_logo_cb.config(variable=self.use_logo_var, text="Verwende Logo", bg=THEME_COLOR,
                                highlightcolor=THEME_COLOR, command=self.use_logo)
        self.use_logo_cb.place(x=5, y=215, anchor="w")
        self.use_logo_var.set(int(pdf.COMPANY_DATA[6]))

        self.use_sign_cb = Checkbutton(options_window)
        self.use_sign_cb.config(variable=self.use_sign_var, text="Unterschriftsfeld", bg=THEME_COLOR,
                                highlightcolor=THEME_COLOR, command=self.use_sign)
        self.use_sign_cb.place(x=5, y=280, anchor="w")
        self.use_sign_var.set(int(pdf.COMPANY_DATA[7]))

        self.use_site_cb = Checkbutton(options_window)
        self.use_site_cb.config(variable=self.use_site_var, text="Seitenzähler", bg=THEME_COLOR,
                                highlightcolor=THEME_COLOR, command=self.use_site)
        self.use_site_cb.place(x=5, y=300, anchor="w")
        self.use_site_var.set(int(pdf.COMPANY_DATA[8]))

        self.save_options_btn = Button(options_window)
        self.save_options_btn.config(text="Speichern", width=20, command=self.save_options)
        self.save_options_btn.place(x=190, y=350, anchor=CENTER)

    # -----FUNCTIONS-----
    def use_logo(self):
        pdf.COMPANY_DATA[6] = str(self.use_logo_var.get())

    def use_sign(self):
        pdf.COMPANY_DATA[7] = str(self.use_sign_var.get())

    def use_site(self):
        pdf.COMPANY_DATA[8] = str(self.use_site_var.get())

    def save_options(self):
        pdf.COMPANY_DATA[0] = self.company_name_entry.get()
        pdf.COMPANY_DATA[1] = self.company_street_entry.get()
        pdf.COMPANY_DATA[2] = self.company_plz_entry.get()
        pdf.COMPANY_DATA[3] = self.logo_size_entry.get()
        pdf.COMPANY_DATA[4] = self.logo_x_entry.get()
        pdf.COMPANY_DATA[5] = self.logo_y_entry.get()
        pdf.save_pdf_data()
