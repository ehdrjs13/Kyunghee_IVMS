import pandas as pd

# xlsx파일 내의 데이터들을 정리하여 self.df에 dataframe의 형태로 저장. 

class GetPersonalData():
    def __init__(self, filename) -> None :
        self.df = pd.read_excel(filename).dropna()
        self.name = self.df['이름']
        self.school = self.df['학교']

        self.personalData = dict()

        return
    
    def GetSchoolCode(self, schname) -> str :
        #이외 학교 추가바람. 
        if schname == '상문고':
            return 'SM'
        elif schname == '동덕여고':
            return 'DD'
        elif schname == '세화고':
            return 'SW'
        elif schname == '반포고':
            return 'BP'
        elif schname == '중동고':
            return 'JD'
        elif schname == '세화여고':
            return 'SG'
        elif schname == '휘문고':
            return 'HM'
        elif schname == '서초고':
            return 'SC'
        elif schname == '양재고':
            return 'YJ'
        else:
            return 'ot'
        #elif schname == '학교이름':
        #   return '학교코드'
        
    def GetNum(self,num) -> str :
            if num <= 200:
                return 'A'
            elif num > 200 and num <= 400:
                return 'B'
            elif num > 400 and num <= 600:
                return 'C'
            elif num > 600 and num <= 800:
                return 'D'
            elif num > 800 and num <= 1000:
                return 'E'
            else:
                return 'N'

    
    def GetCode(self):
        for i in range(len(self.df)):
            
            num = i + 1
            num_four = str(num).zfill(4)

            sccode = self.GetSchoolCode(self.school[i])

            print('Processing..: ', num_four)
            
            
            self.gate = self.GetNum(num)

            self.personalData[num_four] = {'이름' : self.name[i],'학교' : self.school[i], '개인번호': num_four, '개인코드' : self.gate+num_four+sccode}
            
        return pd.DataFrame(self.personalData)

        



