from Ticket.processData import GetPersonalData

#id을 받아서 dataframe 반환(사용자 정보)

processData = GetPersonalData('Ticket/visitorList.xlsx')
#파일 이름은 변경가능. 

class ApproachData():
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
        
        





    