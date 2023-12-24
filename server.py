from flask import Flask, request, jsonify
import requests
import pandas as pd 
import sqlite3
import logging
from datetime import datetime

now = datetime.now()



app = Flask(__name__)


logging.basicConfig(filename='Server_Log/app.log', level=logging.DEBUG)

logging.getLogger('werkzeug').setLevel(logging.ERROR)


@app.route('/mainEntrial/<id>', methods = ['GET'])
def search(id):
    con = sqlite3.connect('visitorlist.db')
    cursor = con.cursor()
    
    index = int(id[1:5]) - 1
    cursor.execute(f"SELECT * FROM visitors WHERE indexing = {index}")
    data = cursor.fetchone() #tuple

    #체크값 1로 바꾸기
    cursor.execute(f"UPDATE visitors SET 'Check' = 1 WHERE indexing = {index}")

    con.commit()

    con.close()

    app.logger.info(f'\n{now.time()}  |  Entrial : {data[4]} ----------')





    return jsonify(data=data)

@app.route('/recovery/<id>', methods = ['GET'])
def recovery(id):
    con = sqlite3.connect('visitorlist.db')
    cursor = con.cursor()
    
    index = int(id[1:5]) - 1

    #체크값 1로 바꾸기
    cursor.execute(f"UPDATE visitors SET 'Check' = 0 WHERE indexing = {index}")

    con.commit()

    con.close()

    app.logger.info(f'\n{now.time()}  |  Recover : {index+1} ----------')

    return 'Done!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)


#<json 전송 형식>
#     {
#     "data": [
#         0,
#         "홍길동",
#         "상문고",
#         "0001",
#         "A0001SM",
#         0
#     ]
# }