# pip install python-frontmatter
# %%
from io import BytesIO
import os
import frontmatter
import pandas as pd
from PIL import Image
from PIL.Image import Resampling

candidati = pd.read_csv('candidati.csv', index_col=['id'])

for candidatoID, data in candidati.iterrows():
    print(candidatoID)

    if data['lista'] == 'fi-lega':
        continue

    if pd.notna(data['custom-scheda']) and data['custom-scheda'] == 'Sì':
        continue

    if not os.path.exists(f"static/cv/{candidatoID}"):
        os.mkdir(f"static/cv/{candidatoID}")

    imageSrc = f"static/cv/{candidatoID}/{candidatoID}.jpeg"
    saveName = f"static/cv/{candidatoID}/{candidatoID}.webp"

    if os.path.exists(imageSrc):
        image = Image.open(imageSrc)
        image = image.resize([768, 1152], resample=Resampling.BICUBIC)
        image.save(saveName, format='webp', optimize=True, quality=80)

    post = frontmatter.Post(
        data['professione'] if pd.notna(data['professione']) else "")

    post.metadata = {
        "id": candidatoID,
        "order": data["order"],
        "name": data["nome"],
        "surname": data["cognome"],
        "gender": data["sesso"],
        "birthday": data["data-nascita"],
        "birthplace": data["luogo-nascita"],
        "location": data["residenza"],
        "type": "consigliere",
        "image": f"/cv/{candidatoID}/{candidatoID}.webp",
        "cv": f"/cv/{candidatoID}/{candidatoID}.pdf",
        "casellario": f"/cv/{candidatoID}/casellario-{candidatoID}.pdf",
        "centerImage": True if data["center-image"] == 'Sì' else False,
        "list": [data["lista"]]
    }

    f = BytesIO()
    frontmatter.dump(post, f, sort_keys=False)

    with open(f"./src/md/candidati/{candidatoID}.md", 'wb') as fp:
        fp.write(f.getbuffer())

# %%
