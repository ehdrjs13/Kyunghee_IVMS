from flask import Flask, request, jsonify, send_file
import pandas as pd 
import sqlite3
import logging
from datetime import datetime
from Datas.RealTimeMgmt import *
from Datas.Ticket.numberDoc import *

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

    return 'Done'

@app.route('/ticket/<id>', methods = ['GET'])
def ticket(id):
    #티켓 조회하기
    return send_file(f'Datas/Ticket/savedImg/{id}.png')
    

@app.route('/newusr', methods = ['GET'])
def newusr():
    name = request.args.get('name')  
    school = request.args.get('school')
    emailAddress = request.args.get('email')

    rtm = RealTimeMgmt()
    rtm.makeImage(name,school)
    rtm.addToSQL(name,school,emailAddress)

    
    return 'Success'

@app.route('/log', methods = ['GET'])
def log():
    return send_file('Server_Log/app.log', mimetype='text/plain')
    


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