from flask import Flask, render_template
import csv
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="Das@369", database="myDB")
    print('database connected')

except:
    print("I am unable to connect to the database")

cursor = mydb.cursor()
csv_data = csv.reader(open('battles.csv'))
for row in csv_data:
    cursor.execute('INSERT  INTO battle (name,year,battle_number,attacker_king,defender_king,attacker_1,attacker_2,attacker_3,attacker_4,defender_1,defender_2,defender_3,defender_4,attacker_outcome,battle_type,major_death,major_capture,attacker_size,defender_size,attacker_commander,defender_commander,summer,location,region) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)

print(row)

mydb.commit()
cursor.close()
print("Done")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showdata')
def showdata():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM battle")
    data = cursor.fetchall()
    return render_template('showdata.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
