from PIL import Image


def compos(path_back,path_fore_1, path_fore_2):
    back = Image.open(path_back)
    fore_1 = Image.open(path_fore_1)
    fore_2 = Image.open(path_fore_2)
    fore_1 = fore_1.resize((50,50))
    fore_1 = fore_1.resize((50,50))
    back.paste(fore_1, (50, 50))
    back.paste(fore_2, (500, 500))
    back.save('./image/compos.png')

compos(r"C:\Users\DELL\Pictures\picture\img01.jpg",
       r"C:\Users\DELL\Pictures\picture\35992522.jfif",
       r"C:\Users\DELL\Pictures\picture\35992522.jfif")

