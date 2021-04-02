import mysql.connector as mysql
#try:
mydb = mysql.connect(user ="Yesh", password="Pass@123", host='127.0.0.1', database='college')
mycursor = mydb.cursor()
print(mycursor)
#mycursor.execute("Show tables;")
  
#myresult = mycursor.fetchall()
 
#for x in myresult:
#    print(x)

sql = "INSERT INTO CLASS1 (ROLLNO) VALUES ('2002')"
#val = ("2002")
result=mycursor.execute(sql)
print(result)
#for x in myresult:
#  print(x)
mydb.commit()

#except Exception as e:
    #print(e)