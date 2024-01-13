import sqlite3
import json
import pprint
import person
import scraper

print(sqlite3.sqlite_version)

conn = sqlite3.connect("UCSalaries.db")
cur = conn.cursor()
cur.executescript('drop table if exists salaries;')
cur.execute("""CREATE TABLE salaries(ID, Name, Job_Title, Regular_Pay, Overtime_Pay, Other_Pay, Total_Pay, Benefits, Total_Pay_And_Benefits)""")

for i in range(1, 51):
    scraper.readPage(i)
    d = open('dataset', 'r')
    dictionary = json.load(d)
    d.close()

    #pprint.pprint(dictionary[0])

    for val in dictionary:
        data = person.Person(val)
        cur.execute("INSERT INTO salaries VALUES " + str(data))
    conn.commit()
    
    
conn.close()