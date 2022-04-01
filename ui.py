from tkinter import *

THEME_COLOR = "#156db5"


class GUI_Setup:

    def __init__(self):
        self.root = Tk()
        self.root.config(bg=THEME_COLOR, pady=20, padx=20)
        self.root.minsize(500, 510)
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

        self.create_pdf_btn = Button()
        self.create_pdf_btn.config(text="Erstelle PDF", width=30)
        self.create_pdf_btn.place(x=225, y=460, anchor=CENTER)



