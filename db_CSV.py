import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Das@369", database="myDB")
print('database connected')

cursor = mydb.cursor()
csv_data = csv.reader(open('battles.csv'))
for row in csv_data:
    cursor.execute('INSERT  INTO battle (name,year,battle_number,attacker_king,defender_king,attacker_1,attacker_2,attacker_3,attacker_4,defender_1,defender_2,defender_3,defender_4,attacker_outcome,battle_type,major_death,major_capture,attacker_size,defender_size,attacker_commander,defender_commander,summer,location,region,note) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
    print(row)

mydb.commit()
cursor.close()
print("Done")
