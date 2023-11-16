from processData import GetPersonalData
# from makeQR import GetQR
import qrcode

class GetQR():
    def __init__(self) -> None:
        self.personalData = GetPersonalData('visitorList.xlsx')
        self.data = self.personalData.GetCode()
        for i in range(self.data.shape[1]):
            num_four = str(i+1).zfill(4)
            self.makeQR(num_four)
        return
    
    def makeQR(self, num):
        
        code = self.data[num][3]
        img = qrcode.make(code)
        img.save(f"qrcodes/{num}.jpg")


a = GetQR()

