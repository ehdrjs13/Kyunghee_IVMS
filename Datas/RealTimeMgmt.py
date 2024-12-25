from Datas.Ticket.numberDoc import *
from Datas.Ticket.processData import *
from PIL import Image, ImageDraw, ImageFont
import sqlite3

class RealTimeMgmt:
    def __init__(self):
        pass
    
    def makeImage(self, name, school) -> None:
        self.bg = Image.open('Datas/Ticket/comps/template.jpg')
        self.draw =  ImageDraw.Draw(self.bg)
        self.font = ImageFont.truetype('Datas/Ticket/comps/AppleSDGothicNeoEB.ttf', size = 35)

        self.NamePos = (540,315)
        self.SchoolPos = (540,445)
        self.NumPos = (540,580)
        # self.GatePos = (540,210)
        self.CodePos = (570,680)

        
        self.num = load_number() + 1
        update_number(self.num)

        self.code = GetPersonalData.GetCode_identical(school,num)

        self.draw.text(self.NamePos, name, fill = (0,0,0), font = self.font)
        self.draw.text(self.SchoolPos, school, fill = (0,0,0), font = self.font)
        # self.draw.text(self.GatePos, code[0], fill = (0,0,0), font = self.font)
        self.draw.text(self.NumPos, self.code[1:5], fill = (0,0,0), font = self.font)
        
        self.qr = Image.open(f'Datas/Ticket/qrcodes/{self.code[1:5]}.jpg')
        self.qr = self.qr.resize((230, 230)) 
        
        self.bg.paste(self.qr, (450, 670), self.qr)

        self.draw.text(self.CodePos, self.code, fill = (0,0,0),font= ImageFont.truetype('Datas/Ticket/comps/AppleSDGothicNeoB.ttf', size = 15))
        
        self.bg.save(f'Datas/Ticket/savedImg/{self.num}.png')

        return
    
    def addToSQL(self,name,school,emailAddress):
        conn = sqlite3.connect('visitorlist.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO people (name, school, personal_number, personal_code, check_status, email)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, school, self.num, self.num, 0, emailAddress))
        conn.commit()
        conn.close()