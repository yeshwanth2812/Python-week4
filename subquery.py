import mysql.connector as mysql
#try:
mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
result=mycursor.execute('SELECT Count(*) AS distinctage FROM (SELECT DISTINCT age FROM college);;')
print(result)

#mydb.commit()