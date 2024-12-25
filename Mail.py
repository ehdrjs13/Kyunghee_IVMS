from MailTools.SendMail import *
from Datas.approachData import *

admin_address = input('발송자 Gmail 계정 주소를 입력하세요. ')
admin_pw = input('발송자 Gmail 계정 비밀번호 (App Password)를 입력하세요.')

a = ApproachData().sheet.transpose()

mail = SendMail()

for i in range(len(a['이메일 주소'])):
    try:
        num = str(a['개인번호'][i])
        mailaddress = a['이메일 주소'][i]
        name = a['이름'][i]
        school = a['학교'][i]
        print(name,school,num,mailaddress)
        mail.sendTicket(admin_address, admin_pw, mailaddress,num)
    except:
        pass



mail.quit()




