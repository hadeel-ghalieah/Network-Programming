
class JuiceBeauty:
    # parameterized constructor
    def __init__(self, product='', production_date=2015, expiry_date=2020, price=0):
        self.product = product 
        self.production_date = production_date
        self.expiry_date = expiry_date
        self.price = price

    # Class Method
    @classmethod
    def Selling_Shop(cls, product, shop):
        return cls(product, "Al-Zeraha")

    def setProduct(self, product):
        self.product = product

    def setProductionDate(self, production_date):
        self.production_date = production_date

    def setExpiryDate (self, expiry_date):
        self.expiry_date = expiry_date

    def setPrice(self, price):
        self.price = price


    def getProduct(self):
        return self.product 

    def getProductionDate(self):
        return self.production_date

    def getExpiryDate(self):
        return self.expiry_date
        
    def getPrice(self):
        return self.Price

    def __str__(self):
        return "MyProduct is: " + self.product + "|| The Production Date is: " +  str(self.production_date) + "|| The Expiry Date is: "  +  str(self.expiry_date) + "|| The Price is: " + str(self.price)


class Lipstick(JuiceBeauty):
    def __init__(self, product = '', production_date=2020, expiry_date=2025, price=500, color='', number=''):
        super().__init__(product, production_date, expiry_date, price)
        self.color = color
        self.number = number

    # Method Overriding.
    def getProduct(self):
        print(" This is a Lipstick from JuiceBeauty Baby ^_^ ")


class EyeLiner(JuiceBeauty):
    def __init__(self, product = '', production_date=2020, expiry_date=2025, price=500, color='', number=''):
        super().__init__(product, production_date, expiry_date, price)
        self.color = color
        self.number = number

    # Instance Method
    def charmers(self):
        print(" This is the best eyeliner you could ever have dear ")
        

### ======================================================== ###
      
        


