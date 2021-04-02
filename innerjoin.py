import mysql.connector as mysql
#try:
mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
mycursor.execute('SELECT college.rollno, teacher.teachername, teacher.teachersubjects, college.name FROM college INNER JOIN teacher ON college.rollno=teacher.teacherid; ')
result=mycursor.fetchall()
print(result)

#notworking
#mydb.commit()