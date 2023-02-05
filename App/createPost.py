title_post = input("Entrer le titre de votre post : ")
date = input("Entrer la date : ")
img_post = input("Entrer une image pour votre post (sinon ecrire false) : ")
text_post = input("Entrer un texte pour votre post (<br> pour les sauts de ligne) : ")

title_code = f"<h2 id='title'>{title_post}</h2>"
if not img_post == "false" or not img_post == "False":
    img_code = f"<img id='image' src='{img_post}'>"
else:
    img_code = ""
date_code = f"<p id='date'></p>"
text_code = f"<p id='text'>{text_post}</p>"

code_html = f"<div class='post'>\n{title_code}\n{text_code}\n{img_code}\n</div>\n<br>"
print(f"Voici le code HTML à copier-coller :\n\n{code_html}")