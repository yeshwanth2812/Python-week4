import mysql.connector as mysql

mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
result=mycursor.execute('DROP INDEX college.collegeind;')
print(result)

mydb.commit()