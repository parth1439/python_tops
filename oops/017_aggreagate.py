class salary:
    def __init__(self,pay):
        self.pay=pay

    def total_pay(self):
        return self.pay*12
    
class emp:
    def __init__(self,sal_obj,bonus):
        self.sal_obj = sal_obj
        self.bonus=bonus

    def get_pay(self):
        print(f"total {self.sal_obj.total_pay()+self.bonus}")

s=salary(5000)
print(s.total_pay())

e=emp(s,10000)
e.get_pay()

e1=emp(s,12000)
e1.get_pay()
    

