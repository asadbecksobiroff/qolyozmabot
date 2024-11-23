# from .functions import Con
from PIL import Image, ImageDraw, ImageFont


class Main:

    def __init__(self, daftar):
        self.daftar = daftar

        if self.daftar == 'katak1':
            self.x = 5
            self.y = 8
            self.y_prob = 34

        elif self.daftar == 'katak2':
            self.x = 100
            self.y = 8
            self.y_prob = 34


        elif self.daftar == 'yol1':
            self.x = 5
            self.y = 53
            self.y_prob = 27

        elif self.daftar == 'yol2':
            self.x = 100
            self.y = 53
            self.y_prob = 27



    def write(self, Text):
        img = Image.open(f'data/images/{self.daftar}.jpg')
        font = ImageFont.truetype('data/images/inWritten.ttf', 35)
        d = ImageDraw.Draw(img)

        y = self.y
        event = 0
        for a in Text:
            for i in a:
                x = self.x
                # if event == 0:
                #     x = ((600 - (len(str(a))-4) * 20) / 2)


                d.text((x, y), i, font = font, fill = '#3f51b5') #3f51b5, #673ab7, #3d3e5f
                y += self.y_prob
                event += 1

        img.save('data/images/Konspekt.png')
