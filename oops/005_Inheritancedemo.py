# class A:
#     def __init__(self):
#         print("a const calling")

#     def display(self):
#         print("a calling")

# class B:
#     def __init__(self):
#         print("b const calling")

#     def display(self):
#         print("b calling")

# class c:
#     def __init__(self):
#         print("c const calling")

#     def display(self):
#         print("c calling")

# class D:
#     def __init__(self):
#         print("D const calling")

#     def display(self):
#         print("d calling")

# c=A()
# c.display()


class A:
    def __init__(self):
        print("a const calling")

    def display(self):
        print("a calling")

class B:
    def __init__(self):
        print("b const calling")

    def display(self):
        print("b calling")

class c(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def display(self):
        print("c calling")
        B.display(self)
        A.display(self)

c=c()
c.display()
        



