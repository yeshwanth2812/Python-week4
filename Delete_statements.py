import mysql.connector as mysql
#try:
mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
mycursor.execute('DELETE FROM college WHERE rollno="6";')
result=mycursor.fetchall()
print(result)

#mydb.commit()