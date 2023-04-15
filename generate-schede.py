# sudo apt install inkscape

# %%
import os
import base64
import pandas as pd
import subprocess

candidati = pd.read_csv('candidati.csv', index_col=['id'])

for candidatoID, data in candidati.iterrows():
    print(f"[🤖 GENERANDO] {data['nome']} {data['cognome']}")

    template = open(f"schede-candidati/scheda-{data['lista']}.svg").read()

    imageLink = ""
    imagePath = f"static/cv/{candidatoID}/{candidatoID}.jpeg"
    if os.path.exists(imagePath):
        with open(imagePath, "rb") as fp:
            imageData = base64.b64encode(fp.read())
            imageLink = f"data:image/jpeg;base64,{imageData.decode()}"

    savePathSVG = f"schede-candidati/svg/{candidatoID}.svg"
    savePathPNG = f"schede-candidati/png/{candidatoID}.png"

    with open(savePathSVG, "w+") as fp:
        template = template.replace("[[NOME]]", data['nome'])
        template = template.replace("[[COGNOME]]", data['cognome'])
        template = template.replace("[[FOTO_PROFILO]]", imageLink)

        fp.write(template)

    subprocess.run(("inkscape", savePathSVG, "-o", savePathPNG))

# %%
