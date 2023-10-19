class Car():
    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price

    def price_inc(self):
        self.price= int(self.price*1.15)
#Inheritance in Python
class SuperCar(Car):
    def __init__(self, model, year, price, cc):
        super().__init__(model, year, price)
        self.cc = cc

honda=SuperCar('city',2010,20000,1500)
tata=Car('suv',2023,800000)
honda.cc=1500
print(honda.year)
#print(honda.price)
#honda.price_inc()
#print(honda.price)


