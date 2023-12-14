from approachData import approachData
import sqlite3
import pandas as pd

a = approachData()

df = a.sheet

conn = sqlite3.connect('visitorlist.db')
df.to_sql('visitors', conn, index=False, if_exists='replace')

conn.close()

print('Done. ')