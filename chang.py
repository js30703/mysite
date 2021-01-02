import csv
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


f = open("verbs12.csv", "r", encoding = 'utf-8')
rdr = csv.reader(f)



i=0
for line in rdr:
    c.execute(f'UPDATE jamo_verbs SET id={i} WHERE id ={line[0]}')
    i+=1

conn.commit()
conn.close()
f.close()  


