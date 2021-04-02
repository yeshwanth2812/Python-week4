import mysql.connector as mysql
#try:
mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
mycursor.execute('SELECT name FROM college WHERE age BETWEEN 21 AND 23 ;')
result=mycursor.fetchall()
print(result)


#mydb.commit()