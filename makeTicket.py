from processData import GetPersonalData
# from makeQR import GetQR
from PIL import Image, ImageDraw, ImageFont
import pandas

class makeTicket():
    def __init__(self) -> None:
        self.personalData = GetPersonalData('visitorList.xlsx')
        self.data = self.personalData.GetCode()
        return
    def makeImage(self, num):
        self.bg = Image.open('template.jpg')
        self.draw =  ImageDraw.Draw(self.bg)
        self.font = ImageFont.truetype('AppleSDGothicNeoEB.ttf', size = 35)

        self.NamePos = (540,315)
        self.SchoolPos = (540,445)
        self.NumPos = (540,580)
        self.GatePos = (540,210)

        name = self.data[num][0]
        school = self.data[num][1]
        code = self.data[num][3]

        self.draw.text(self.NamePos, name, fill = (0,0,0), font = self.font)
        self.draw.text(self.SchoolPos, school, fill = (0,0,0), font = self.font)
        self.draw.text(self.GatePos, code[0], fill = (0,0,0), font = self.font)
        self.draw.text(self.NumPos, code[1:5], fill = (0,0,0), font = self.font)

        self.bg.save(f'savedImg/{num}.png')

#fortest
a = makeTicket()

a.makeImage('0001')


