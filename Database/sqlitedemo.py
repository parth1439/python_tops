import sqlite3

con =sqlite3.connect("myddb.db")
# qury="create table student (id int primary key,name varchar(50),email varchar(50),phone varchar(50))"

# qury="insert into student values(1,'parth','parth@gmail.com','7622893779')"
qury="insert into student values(2,'hetvi','hetvi@gmail.com','8457675940','f')"
# qury="insert into student values(3,'abc','abc@gmail.com','8457640','male')"

# qury="delete from student where id=2"

#qury="alter table student add column gender varchar(5)"
con.execute(qury)
con.commit()

# qury="select * from student"
# data=con.execute(qury).fetchall()

# for i in data:
#     for j in i:
#         print(j,end=" ")
#     print()
