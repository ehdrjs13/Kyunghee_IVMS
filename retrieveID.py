from processData import GetPersonalData

processData = GetPersonalData('visitorList.xlsx')
#파일 이름은 변경가능. 

class RetrieveByNum():
    def __init__(self) -> None:
        self.sheet = processData.GetCode()

        pass

    def searchID(self, pCode):
        idNum = pCode[1:5]

        try:
            return self.sheet[idNum]
        except:
            raise NotCorrectData
    
        
class NotCorrectData(Exception):
    def __init__(self) -> None:
        super().__init__('올바른 형태의 데이터가 아닙니다. ')





    