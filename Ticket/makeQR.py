from Ticket.processData import GetPersonalData

import qrcode

#makeTicket에 사용될 QR코드 생성.
class GetQR():
    def __init__(self) -> None:
        self.personalData = GetPersonalData('visitorList.xlsx')
        self.data = self.personalData.GetCode()
        
        return
    
    def makeQR(self, num):
        
        code = self.data[num][3]
        img = qrcode.make(code)
        img.save(f"Ticket/qrcodes/{num}.jpg")


