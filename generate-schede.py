import base64

with open("static/cv/luca-martinelli/profile.jpeg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
