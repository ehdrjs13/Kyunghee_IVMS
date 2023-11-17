from processData import GetPersonalData

import qrcode

class GetQR():
    def __init__(self) -> None:
        self.personalData = GetPersonalData('visitorList.xlsx')
        self.data = self.personalData.GetCode()
        
        return
    
    def makeQR(self, num):
        
        code = self.data[num][3]
        img = qrcode.make(code)
        img.save(f"qrcodes/{num}.jpg")


