class Calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,obj):
        return self.a+obj.a,self.b+obj.b

    # def __mul__(self,obj):
    #     return self.a*obj.a,self.b*obj.b
    
    def display(self):
        print(self.a,self.b)



c1 = Calc(10,20)
c2 = Calc(30,40)
print("addiction")
c3=c1+c2
c3.display()

# class Calc:

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, obj):
#         return Calc(self.a + obj.a, self.b + obj.b)

#     def __mul__(self, obj):
#         return Calc(self.a * obj.a, self.b * obj.b)

#     def display(self):
#         print(self.a, self.b)


# c1 = Calc(10, 20)
# c2 = Calc(30, 40)

# # Addition
# c3 = c1 + c2
# print("Addition Result:")
# c3.display()

# # Multiplication
# c4 = c1 * c2
# print("Multiplication Result:")
# c4.display()

