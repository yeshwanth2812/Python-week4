import mysql.connector as mysql

mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)


mycursor.execute('CREATE TABLE college (rollno int(5), name varchar(255), Age int(25), Address varchar(255), PRIMARY KEY (rollno));')
result=mycursor.fetchall()
print(result)


mydb.commit()


