import mysql.connector as mysql

mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
mycursor.execute('CREATE INDEX colleind ON college (rollno, name, Address);')
result=mycursor.fetchall()
print(result)


mydb.commit()