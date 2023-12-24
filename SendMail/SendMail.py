
class SendMail():
  def __init__(self) -> None:

    import smtplib



    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465
    self.smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

    pass
  
  def sendTicket(self, admin_address, admin_pw, address, num):
     print(f'processing : {num}')
     from email.mime.multipart import MIMEMultipart
     from email.mime.text import MIMEText
     
     EMAIL_ADDR = admin_address
     EMAIL_PASSWORD = admin_pw
     self.smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
     EMAIL_ADDR = admin_address
     EMAIL_PASSWORD = admin_pw
     self.smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)

     message = MIMEMultipart()
     message['From'] = '서울고등학교 학생회'
     message['To'] = address
     subject = "제 77회 서울고등학교 경희제 입장 티켓 배부"
     message['Subject'] = subject

     # 이메일 본문 추가
     body = MIMEText('안녕하십니까? 서울고등학교 학생회입니다.\n귀하를 77년의 역사를 지닌 서울고등학교의 축제, 경희제에 초대합니다! \n\n서울고등학교는 제 77회 경희제에서 안전사고 방지와 입장객 수요 관리를 위해 입장 사전 예약제를 도입하였습니다. \n\n이 메일을 받은 외부인께서는 첨부된 티켓 이미지를 사용하여 경희제에 입장하실 수 있습니다.\n입장 방법과 관련해서는 첨부된 입장 매뉴얼을 참고해주시기 바랍니다. \n\n*본 티켓은 입장 신청 설문을 작성하고 학생증을 제출한 학생 본인만 사용 가능합니다. \n*입장 관련 문의 사항은 서울고등학교 학예부장(전화번호)나 서울고등학교 학생회 인스타그램을 통하여 문의 주시기 바랍니다.  ', 'plain', 'utf-8')
     message.attach(body)



     #사진 첨부
     with open(f'Ticket/savedImg/{num}.png', 'rb') as image:
         image_file = image.read()  # 이미지 파일 읽어오기

     image_type = 'png' 
     image_attachment = MIMEText(image_file, 'base64', 'utf-8')
     image_attachment.add_header('Content-Disposition', 'attachment', filename=f'{num}.png')
     message.attach(image_attachment)
     self.smtp.sendmail(EMAIL_ADDR, address, message.as_string())

     print(f'done : {num}')

  def quit(self):
     self.smtp.quit()
     print('Process Done.')







