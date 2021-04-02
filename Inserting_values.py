import mysql.connector as mysql
#try:
mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
mycursor.execute('INSERT INTO college (rollno , name , Age , Address) VALUES ("6", "Vishndffdfdfu", "22", "HSR Layoyt Bangalore");')
result=mycursor.fetchall()
print(result)

mydb.commit()

