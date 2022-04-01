import pandas as pd
from fpdf import FPDF

DATA = None
TIME = ""
COUNT = 0
PDF_DATA = ""
COMPANY_DATA = []

with open("config.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()
    for l in lines:
        COMPANY_DATA.append(l)

class PDF(FPDF):
    def header(self):
        self.image('logo.png', 180, 12, 25)
        self.set_font('helvetica', 'B', 12)
        self.cell(60, 6, f'{COMPANY_DATA[0]}', border=0, align='L', ln=1)
        self.cell(60, 6, f'{COMPANY_DATA[1]}', border=0, align='L', ln=1)
        self.cell(60, 6, f'{COMPANY_DATA[2]}', border=0, align='L', ln=1)
        self.ln(20)


def initiate_pdf_data():
    global PDF_DATA
    PDF_DATA = PDF('P', 'mm', "Letter")
    PDF_DATA.add_page()
    PDF_DATA.set_font('helvetica', '', 16)
    PDF_DATA.set_auto_page_break(auto=True, margin=10)


def create_pdf_data(df):
    PDF_DATA.set_font('helvetica', 'B', 16)
    PDF_DATA.cell(0, 10, 'Stundenabrechnung', border=1, align='C', ln=1)
    PDF_DATA.set_font('helvetica', '', 16)
    PDF_DATA.ln()
    PDF_DATA.cell(70, 0, f'Mitarbeiter', 0, 0, 'L')
    PDF_DATA.cell(70, 0, f'Kategorie', 0, 0, 'L')
    PDF_DATA.cell(70, 0, f'Dauer', 0, 1, 'L')
    PDF_DATA.cell(0, 0, f'______________________________________________________________', 0, 1, 'L')
    PDF_DATA.ln(5)
    for index, row in df.iterrows():
        PDF_DATA.cell(70, 10, f'{row["Mitarbeiter"]}', 0, 0, 'L')
        PDF_DATA.cell(70, 10, f'{row["Kategorie"]}', 0, 0, 'L')
        PDF_DATA.cell(70, 10, f'{row["Arbeitszeit"]}', 0, 1, 'L')
    PDF_DATA.cell(0, 0, f'______________________________________________________________', 0, 1, 'L')
    PDF_DATA.set_font('helvetica', 'B', 16)
    PDF_DATA.cell(70)
    PDF_DATA.cell(70, 15, f'Gesamte Arbeitszeit: ', 0, 0, 'L')
    PDF_DATA.cell(0, 15, f'{TIME}', 0, 1, 'L')


def create_pdf(df, time_str):
    global DATA
    global TIME
    global COUNT
    DATA = df
    TIME = time_str
    initiate_pdf_data()
    create_pdf_data(DATA)
    PDF_DATA.output(f'pdf_{COUNT}.pdf')
    COUNT += 1


