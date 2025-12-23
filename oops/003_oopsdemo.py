class student:

    clg="abcd"
    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email

    def display(self):
        print(self.id,self.name,self.email)

    @classmethod
    def show(cls):
        print(cls.clg)






