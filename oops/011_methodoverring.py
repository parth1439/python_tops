class A:
    def __display(self):
        print("cass a display calling")

class B(A):
    pass
    def display(self):
        print("class b display calling")

b=B()
b.display()