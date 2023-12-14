import cv2
from pyzbar.pyzbar import decode
# from tkinter import messagebox
import winsound
import requests

print('Wait for a Second...\n\n')
print('\n\n[2023 Seoul High School KyungheeJe Visitor Check-In System]\n\n Scan QR to Check-IN..')




def scan_qr_code():

    cap = cv2.VideoCapture(0)

    while True:

        _, frame = cap.read()

        decoded_objects = decode(frame)

        for obj in decoded_objects:

           
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(points, clockwise=True)
                cv2.drawContours(frame, [hull], 0, (0, 255, 0), 2)
                
            
            qr_data = obj.data.decode("utf-8") #e.g.A0001SM

            response = requests.get(f'http://127.0.0.1:5000/mainEntrial/{qr_data}')

            #ip는 꼭 수정 하도록 합시다. 

            data = response.json()


            return data
            

            



            

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

def getDataFromQR():
    #수정필요X


    datas = scan_qr_code()['data']
    

    
    
    name = datas[1]
    school = datas[2]
    code = datas[4]

    check = datas[5]


    if check == 0:
        winsound.Beep(2000,100)
        winsound.Beep(1500,180)
        print(f'이름: {name}\n\n\n학교: {school}\n\n\nGate:  {code[0]}\n\n\n\n{code}\n\n\n\n환영합니다!\n')
    elif check == 1:
        winsound.Beep(2000,2000)
        print(("\033[91mERROR:이미 사용된 입장권입니다.\033[0m"))




# while True:
#     getDataFromQR()

while True:
    
    try:
        getDataFromQR()
    except:
        winsound.Beep(2000,2000)
        getDataFromQR()
        print("\033[91mERROR:올바른 형태의 데이터가 아닙니다.\033[0m")


