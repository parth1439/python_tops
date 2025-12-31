# class student:

#     clg="abcd"
#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
#         self.email=email

#     def display(self):
#         print(self.id,self.name,self.email)

#     @classmethod
#     def show(cls):
#         print(cls.clg)


#class attribute

class student:

    collage_name="abc collage"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("addition new student in database")

s1=student("parth",50)
print(s1.name,s1.marks)

s2=student("gopal",90)
print(s2.name,s2.marks)
print(s2.collage_name)








