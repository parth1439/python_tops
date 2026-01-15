# import pymysql 
# con=pymysql.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="parth19052005",
#     database="tops"
  
# )

# print("connected")
# cursor=con.cursor()
# # cursor.execute("create database tops")

# qur="create table student(id int primary key,name var)"
# cursor.execute(qur)
# con.commit()

# print("contected")
# cursor=con.cursor()

# cursor.execute("create database tops")

# qry=("create table student(id int primary key auto_increment,name varchar(50),email varchar(50))")
# cursor.execute(qry)
# con.commit()


# qry="insert into student values(%s,%s,%s)"
# # val=(1,"parth","parth@gmail.com")
# val=(2,"gopal","gopal@gmail.com")

# # qry="delete from student where id=%s"
# # val=(2,)
# cursor.execute(qry,val)
# con.commit()

# cursor.execute("select * from student")
# data=cursor.fetchall(1)






