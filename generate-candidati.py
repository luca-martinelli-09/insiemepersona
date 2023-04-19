# pip install python-frontmatter
# %%
from io import BytesIO
import os
import frontmatter
import pandas as pd

candidati = pd.read_csv('candidati.csv', index_col=['id'])

for candidatoID, data in candidati.iterrows():
    print(candidatoID)

    if data['lista'] == 'fi-lega':
        continue

    if not os.path.exists(f"static/cv/{candidatoID}"):
        os.mkdir(f"static/cv/{candidatoID}")

    post = frontmatter.Post(data['professione'] if pd.notna(data['professione']) else "")
    post.metadata = {
        "id": candidatoID,
        "name": data["nome"],
        "surname": data["cognome"],
        "gender": data["sesso"],
        "birthday": data["data-nascita"],
        "birthplace": data["luogo-nascita"],
        "location": data["residenza"],
        "type": "consigliere",
        "image": f"/cv/{candidatoID}/{candidatoID}.jpeg",
        "cv": f"/cv/{candidatoID}/{candidatoID}.pdf",
        "casellario": f"/cv/{candidatoID}/casellario-{candidatoID}.pdf",
        "list": [data["lista"]]
    }

    f = BytesIO()
    frontmatter.dump(post, f, sort_keys=False)

    with open(f"./src/md/candidati/{candidatoID}.md", 'wb') as fp:
        fp.write(f.getbuffer())
# %%
