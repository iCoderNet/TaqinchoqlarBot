# import libraries
from PIL import Image, ImageOps
from PIL import ImageDraw
from PIL import ImageFont
from itsdangerous import json
from regex import A


def juftlik3(id, tx1, tx2):
    # open image
    img = Image.open('images/j3.jpg')

    # draw image object
    I1 = ImageDraw.Draw(img)

    #Font
    myFont = ImageFont.truetype('fonts/Sweety Camellia Monogram.ttf', 65)

    # add text to image
    I1.text((70, 315), tx1, font=myFont, fill =(255, 0, 0))
    I1.text((250, 315), tx2, font=myFont, fill =(255, 0, 0))

    # save image
    img.save(f"photos/{id}.jpg")
    return f"photos/{id}.jpg"


def juftlik2(id, tx1, tx2):

    im=Image.open("images/j2.jpg")
    f = ImageFont.truetype('fonts/ReactiveAnchor-L3L0n.ttf', 100)

    txt=Image.new('L', (500,500))
    d = ImageDraw.Draw(txt)
    d.text( (0, 0), tx1,  font=f, fill=250)
    w=txt.rotate(40,  expand=1)
    im.paste( ImageOps.colorize(w, (0,0,0), (255,255,255)), (333,330),  w)

    txt1=Image.new('L', (500,500))
    d1 = ImageDraw.Draw(txt1)
    d1.text( (0, 0), tx2,  font=f, fill=250)
    w1=txt1.rotate(38,  expand=1)
    im.paste( ImageOps.colorize(w1, (0,0,0), (0,0,0)), (583, 200),  w1)

    im.save(f"photos/{id}.jpg")
    return f"photos/{id}.jpg"


def juftlik1(id, tx1, tx2):

    im=Image.open("images/j1.jpg")
    f = ImageFont.truetype('fonts/LucySaidOkPersonalUseItalic-OV9ee.ttf', 180)

    txt=Image.new('L', (500,500))
    d = ImageDraw.Draw(txt)
    d.text( (0, 0), tx1,  font=f, fill=250)
    w=txt.rotate(60,  expand=1)
    im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (450,350),  w)

    txt1=Image.new('L', (500,500))
    d1 = ImageDraw.Draw(txt1)
    d1.text( (0, 0), tx2,  font=f, fill=250)
    w1=txt1.rotate(60,  expand=1)
    im.paste( ImageOps.colorize(w1, (0,0,0), (0,0,0)), (700, 240),  w1)

    im.save(f"photos/{id}.jpg")
    return f"photos/{id}.jpg"


def birlik1(id, tx1):
    # open image
    img = Image.open('images/b1.jpg')

    # draw image object
    I1 = ImageDraw.Draw(img)

    #Font
    myFont = ImageFont.truetype('fonts/Delia Monogram.ttf', 200)

    # add text to image
    I1.text((400, 600), tx1, font=myFont, fill =(255, 255, 255))

    # save image
    img.save(f"photos/{id}.jpg")
    return f"photos/{id}.jpg"

def birlik2(id, tx1):
    # open image
    img = Image.open('images/b2.jpg')

    #Font
    myFont = ImageFont.truetype('fonts/Delia Monogram.ttf', 250)
    txt=Image.new('L', (500,500))
    d = ImageDraw.Draw(txt)
    d.text( (0, 0), tx1,  font=myFont, fill=250)
    w=txt.rotate(-35,  expand=1)
    img.paste( ImageOps.colorize(w, (0,0,0), (255, 255, 255)), (230,750),  w)

    # save image
    img.save(f"photos/{id}.jpg")
    return f"photos/{id}.jpg"

def birlik3(id, tx1):
    # open image
    img = Image.open('images/b3.jpg')

    #Font
    myFont = ImageFont.truetype('fonts/Delia Monogram.ttf', 200)
    txt=Image.new('L', (500,500))
    d = ImageDraw.Draw(txt)
    d.text( (0, 0), tx1,  font=myFont, fill=250)
    w=txt.rotate(-35,  expand=1)
    img.paste( ImageOps.colorize(w, (0,0,0), (255, 255, 255)), (160,570),  w)

    # save image
    img.save(f"photos/{id}.jpg")
    return f"photos/{id}.jpg"


photos = {
    "birlik": {
        "1": "https://i.imgur.com/YCYZq8k.jpg",
        "2": "https://i.imgur.com/J57bItL.jpg",
        "3": "https://i.imgur.com/N07XM2X.jpg",
    },
    "juftlik": {
        "1": "https://i.imgur.com/UVEhLbS.jpg",
        "2": "https://i.imgur.com/dMehCRK.jpg",
        "3": "https://i.imgur.com/s6tpjFW.jpg",
    }
}

def make_photo(cat, s, id, text):
    if cat == 'birlik':
        if s == '1':
            return birlik1(id, text)
        elif s == '2':
            return birlik2(id, text)
        elif s == '3':
            return birlik3(id, text)
    elif cat == 'juftlik':
        tx1, tx2 = text.split('+')
        if s == '1':
            return juftlik1(id, tx1, tx2)
        elif s == '2':
            return juftlik2(id, tx1, tx2)
        elif s == '3':
            return juftlik3(id, tx1, tx2)
    else:
        return None


class Step:
    all =  {}

    def write(self, id, tx=None):
        self.all[id] =  tx
        return True

    def read(self, id):
        return self.all[id].split('|')

stp = Step()
