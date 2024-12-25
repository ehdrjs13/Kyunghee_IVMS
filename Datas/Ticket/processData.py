import pandas as pd

# xlsx파일 내의 데이터들을 정리하여 self.df에 dataframe의 형태로 저장. 

class GetPersonalData():
    def __init__(self, filename) -> None :
        self.df = pd.read_excel(filename).dropna()
        self.name = self.df['이름']
        self.school = self.df['학교']
        self.email = self.df['이메일 주소']


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
        elif schname == '현대고':
            return 'HD'

#update: 12-26
        elif schname == '경문고':
            return 'KM'
        elif schname == '언남고':
            return 'UN'
        elif schname == '중대부고':
            return 'JD'
        elif schname == '은광여고':
            return 'EK'
        elif schname == '한림예고':
            return 'HL'
        elif schname == '경기여고':
            return 'KG'
        elif schname == '진선여고':
            return 'JS'
        elif schname == '숙명여고':
            return 'MG'
        elif schname == '청담고':
            return 'CD'
        elif schname == '계원예고':
            return 'GW'
        elif schname == '보성여고':
            return 'BS'
        else:
            return 'ot'
        #elif schname == '학교이름':
        #   return '학교코드'
        
    def GetNum(self,num) -> str :
            if num <= 130:
                return 'A'
            elif num > 130 and num <= 260:
                return 'B'
            elif num > 260 and num <= 390:
                return 'C'
            elif num > 390 and num <= 500:
                return 'D'
            else:
                return 'N'

    
    def GetCode(self):
        for i in range(len(self.df)):
            
            num = i + 1
            num_four = str(num).zfill(4)

            sccode = self.GetSchoolCode(self.school[i])

            print('Processing..: ', num_four)
            
            
            self.gate = self.GetNum(num)

            self.personalData[num_four] = {'이름' : self.name[i],'학교' : self.school[i], '개인번호': num_four, '개인코드' : self.gate+num_four+sccode, 'Check' : 0,'이메일 주소' : self.email[i] }
            
        return pd.DataFrame(self.personalData)
    
    @staticmethod
    def GetCode_identical(self, schoolName, num):
        num_four = str(num).zfill(4)

        sccode = self.GetSchoolCode(schoolName)

        print('Processing..: ', num_four)
        
        
        gate = self.GetNum(num)

        return gate+num_four+sccode

        

        



