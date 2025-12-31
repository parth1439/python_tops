class Emp:
    def __init__(self,name,email,phone):
        self.name =name
        self._email =email
        self.phone =phone

e=Emp("parth","parth@gmail.com",7622893779)
print(dir(e))
print(e.phone)
print(e._email)
print(e._Emp__name)        


