import cv2
from pyzbar.pyzbar import decode
from approachData import approachData
import pandas as pd
# from tkinter import messagebox
import winsound
import time

print('Wait for a Second...\n\n')

SearchData = approachData()

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
                
            
            qr_data = obj.data.decode("utf-8")
            
            datas = SearchData.searchID(qr_data)



            return [datas['이름'],datas['학교'],datas['개인코드']]

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

def getDataFromQR():



    datas = scan_qr_code()
    winsound.Beep(2000,100)
    winsound.Beep(1500,180)

    
    
    name = datas[0]
    school = datas[1]
    code = datas[2]



    print(f'이름: {name}\n\n\n학교: {school}\n\n\nGate:  {code[0]}\n\n\n\n{code}\n\n\n\n환영합니다!\n')



    

while True:
    
    try:
        getDataFromQR()
    except:
        winsound.Beep(2000,2000)
        print("\033[91mERROR:올바른 형태의 데이터가 아닙니다.\033[0m")


