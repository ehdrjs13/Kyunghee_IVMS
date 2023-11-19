import cv2
from pyzbar.pyzbar import decode
from retrieveID import RetrieveByNum
import pandas as pd

SearchData = RetrieveByNum()

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

    name = datas[0]
    school = datas[1]
    code = datas[2]

    print('이름: ',name,'\n\n\n학교: ',school,'\n\n\nGate: ', code[0],'\n\n\n\n',code,'\n\n\n\n')


while True:
    
    getDataFromQR()

