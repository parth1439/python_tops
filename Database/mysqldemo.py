# import pymysql

# con = pymysql.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="parth19052005",
#     database="tops"
# )

# # print("connected")
# cursor = con.cursor()

# cursor.execute("create database tops")
# qury="create table student (id int primary key, name varchar(50),email varchar(50))"
# cursor.execute(qury)


# qury="insert into student values(%s,%s,%s)"
# val=(1,'parth','parth@gmail.com')
# cursor.execute(qury,val)
# con.commit()

# qury="insert into student values(%s,%s,%s)"
# val=(2,'dev','dev@gmail.com')
# cursor.execute(qury,val)
# con.commit()

# qury="insert into student values(0,'nimit','nimit@gmail.com')"
# cursor.execute(qury)
# # con.commit()

# qury="insert into student values(%s,%s,%s)"
# val=(3,'nimit','nimit@gmail.com')
# cursor.execute(qury,val)
# con.commit()

# qury="insert into student values(%s,%s,%s)"
# val=(4,'hetvi','hetvi@gmail.com')
# cursor.execute(qury,val)
# con.commit()

# qry="update student set email=%s where id=%s"
# val=("abc@gmail.com",3)
# cursor.execute(qry,val)
# con.commit()


import pymysql

con = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="parth19052005",
    # database="school"
    
)
print("conected")
cursor=con.cursor

cursor.execute("create database tops")
# qury="create table student (id int primary key, name varchar(50),email varchar(50))"
# cursor.execute(qury)
# con.commit()

