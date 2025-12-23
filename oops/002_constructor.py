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


class product:

    def __init__(self,id,name,price):
        print("this is a product :")
        self.id=id
        self.name=name
        self.price=price

    def display(self):
        print(self.id,self.name,self.price)

p1=product(1,"mobile",40000)
p1.display()
