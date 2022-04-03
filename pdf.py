import pandas as pd
from fpdf import FPDF

# -----GLOBALS-----
DATA = None
TIME = ""
PDF_DATA = ""
COMPANY_DATA = []
HEAD_LABEL = ""

# -----Load Data from Config.txt-----
with open("config.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()
    for line in lines:
        COMPANY_DATA.append(line.strip())


# -----Header Inheritance-----
class PDF(FPDF):
    def header(self):
        if COMPANY_DATA[6] == "1":
            self.image('logo.png', int(COMPANY_DATA[4]), int(COMPANY_DATA[5]), int(COMPANY_DATA[3]))
        self.set_font('helvetica', 'B', 12)
        self.cell(60, 6, f'{COMPANY_DATA[0]}', border=0, align='L', ln=1)
        self.cell(60, 6, f'{COMPANY_DATA[1]}', border=0, align='L', ln=1)
        self.cell(60, 6, f'{COMPANY_DATA[2]}', border=0, align='L', ln=1)
        self.ln(20)

    def footer(self):
        if COMPANY_DATA[8] == "1":
            self.set_font('helvetica', 'B', 12)
            self.set_y(-15)
            self.cell(0, 10, f'Seite {self.page_no()}/{{nb}}', align='C')


# -----FUNCTIONS-----
def initiate_pdf_data():
    global PDF_DATA
    PDF_DATA = PDF('P', 'mm', "Letter")
    PDF_DATA.add_page()
    PDF_DATA.set_font('helvetica', '', 16)
    PDF_DATA.set_auto_page_break(auto=True, margin=10)


def create_pdf_data(df):
    PDF_DATA.set_font('helvetica', 'B', 16)
    PDF_DATA.cell(0, 10, f'{HEAD_LABEL}', border=1, align='C', ln=1)
    PDF_DATA.set_font('helvetica', '', 16)
    PDF_DATA.ln()
    PDF_DATA.cell(30, 0, 'Datum', 0, 0, 'L')
    PDF_DATA.cell(65, 0, 'Mitarbeiter', 0, 0, 'L')
    PDF_DATA.cell(60, 0, 'Kategorie', 0, 0, 'L')
    PDF_DATA.cell(50, 0, 'Dauer', 0, 1, 'L')
    PDF_DATA.cell(0, 0, f'______________________________________________________________', 0, 1, 'L')
    PDF_DATA.ln(5)
    for index, row in df.iterrows():
        PDF_DATA.cell(30, 10, f'{str(row["Start"]).split(",")[0]}', 0, 0, 'L')
        PDF_DATA.cell(65, 10, f'{row["Mitarbeiter"]}', 0, 0, 'L')
        PDF_DATA.cell(60, 10, f'{row["Kategorie"]}', 0, 0, 'L')
        PDF_DATA.cell(50, 10, f'{row["Arbeitszeit"]}', 0, 1, 'L')
    PDF_DATA.cell(0, 0, f'______________________________________________________________', 0, 1, 'L')
    PDF_DATA.set_font('helvetica', 'B', 16)
    PDF_DATA.cell(85)
    PDF_DATA.cell(70, 15, f'Gesamte Arbeitszeit: ', 0, 0, 'L')
    PDF_DATA.cell(0, 15, f'{TIME}', 0, 1, 'L')
    if COMPANY_DATA[7] == "1":
        PDF_DATA.ln(20)
        PDF_DATA.cell(122, 11, f'_______________________', 0, 0, 'L')
        PDF_DATA.cell(0, 11, f'_______________________', 0, 1, 'L')
        PDF_DATA.set_font('helvetica', '', 11)
        PDF_DATA.cell(122, 0, f'Ort, Datum', 0, 0, 'L')
        PDF_DATA.cell(0, 0, f'Unterschrift', 0, 1, 'L')


def create_pdf(df, time_str, header_label):
    global DATA
    global TIME
    global HEAD_LABEL
    HEAD_LABEL = header_label
    DATA = df
    TIME = time_str
    initiate_pdf_data()
    create_pdf_data(DATA)
    PDF_DATA.output(f'pdf_{HEAD_LABEL}.pdf')


# -----Save Data from Config.txt-----
def save_pdf_data():
    with open("config.txt", "w", encoding="UTF-8") as f:
        for item in COMPANY_DATA:
            f.write(f"{item}\n")
