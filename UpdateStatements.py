import mysql.connector as mysql
#try:
mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
mycursor.execute('UPDATE college SET name = "Yeshwanth S", age= "24" WHERE rollno = 1;')
result=mycursor.fetchall()
print(result)



#mydb.commit()