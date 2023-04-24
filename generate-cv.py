# sudo apt install docxtpl docx2pdf

# %%
import pandas as pd
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
from datetime import datetime
import subprocess
import os

candidati = pd.read_csv('candidati.csv', index_col=['id'])

for candidatoID, data in candidati.iterrows():
    print(f"[🤖 GENERANDO] {data['nome']} {data['cognome']}")

    if pd.isna(data['professione']) or data['professione'] == '':
        continue

    if pd.notna(data['custom-cv']) and data['custom-cv'] == 'Sì':
        continue

    imagePath = f"static/cv/{candidatoID}/{candidatoID}.jpeg"

    if not os.path.exists(imagePath):
        continue

    genderSuffix = 'o' if data['sesso'] == 'M' else 'a'
    birthDate = datetime.strptime(data['data-nascita'], "%Y-%m-%d")

    candidatoDescription = f"Nat{genderSuffix} il {birthDate.strftime('%d/%m/%Y')} a {data['luogo-nascita']}. Residente a {data['residenza']}."

    doc = DocxTemplate("cvs/template.docx")

    templateData = {
        'name': f"{data['nome']} {data['cognome']}",
        'basic_info': candidatoDescription,
        'activity': data['professione'],
        'image': InlineImage(doc, image_descriptor=imagePath, width=Mm(35.5), height=Mm(53.2)) if os.path.exists(imagePath) else 'Nessuna foto profilo'
    }

    doc.render(templateData)

    doc.save(f"cvs/docx/{candidatoID}.docx")

    savePathPDF = f"static/cv/{candidatoID}/{candidatoID}.pdf"

    subprocess.run(("doc2pdf", "-o", savePathPDF, f"cvs/docx/{candidatoID}.docx"))

# %%
