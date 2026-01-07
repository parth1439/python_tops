#construor automatically call 


# class test:
                 
#     def __init__(self,id,name,cousre):
#         print("hello")
#         self.id=id
#         self.name=name
#         self.cousre=cousre

#     def display(self):
#         print("Display calling")
#         print(self.id,self.name,self.cousre)

# t=test(10,"parth","python")
# t.display()

# t1=test(20,"xyz","java")
# t1.display()


# class student:

#     def __init__(self,id,name,email):
#         self.id=id
#         self.name=name
#         self.email=email

#     def display(self):
#         print(self.id,self.name,self.email)

# st=student(10,"parth","parth@gmail.com")
# st.display()


class person:
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("parth","HR")
a.info()   
