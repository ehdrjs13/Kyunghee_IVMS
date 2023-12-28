# from SendMail.SendMail import SendMail
# import pandas as pd
# from approachData import ApproachData

# admin_address = input('발송자 Gmail 계정 주소를 입력하세요. ')
# admin_pw = input('발송자 Gmail 계정 비밀번호 (App Password)를 입력하세요.')

# a = ApproachData().sheet.transpose()

# mail = SendMail()
# # df = a.sheet.transpose()

# for i in range(len(a['이메일 주소'])):
#     num ='{:04d}'.format(int(a['개인번호'][i]))
#     print(num)
#     if int(num) % 2 == 0:
#         mailaddress = 'tony070102@naver.com'
#     else:
#         mailaddress = 'ehdrjs13@kakao.com'
#     name = a['이름'][i]
#     school = a['학교'][i]
#     print(name,school,num,mailaddress)
#     mail.sendTicket(admin_address, admin_pw, mailaddress,num)

# mail.quit()

from SendMail.SendMail import SendMail
import pandas as pd
from approachData import ApproachData



a = ApproachData().sheet.transpose()




for i in range(len(a['이메일 주소'])):
    num = str(a['개인번호'][i+1])
    mailaddress = a['이메일 주소'][i+1]
    name = a['이름'][i+1]
    school = a['학교'][i+1]
    print(name,school,num,mailaddress)




