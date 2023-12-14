from approachData import approachData
import sqlite3
import pandas as pd


a = approachData()

df = a.sheet.transpose()
df = df.reset_index(drop=True)
df.index.name = 'indexing'

print(df)

conn = sqlite3.connect('visitorlist.db')
df.to_sql('visitors', conn, index=True, if_exists='replace')

conn.close()

print('Done. ')