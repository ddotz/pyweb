
from PIL import Image


def compos(path_back,path_fore_1, path_fore_2):
    back = Image.open(path_back)
    fore_1 = Image.open(path_fore_1)
    fore_2 = Image.open(path_fore_2)
    # fore_1 = fore_1.resize((50,50))
    # fore_2 = fore_2.resize((50,50))
    back.paste(fore_1, (92, 1770))
    back.paste(fore_2, (88,2180))
    back.save('./static/compos.png')


