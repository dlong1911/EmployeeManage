


class car():

    def __init__(self,model,price) -> None:
        self.brand = 'None'
        self.model = model
        self.price = int(price)
    
    def show_info(self):
        print(f"Thuong hieu: {self.brand}")
        print(f"Mau xe: {self.model}")
        print("Gia ban le: {:,} VND".format(self.price))

    def get_brand(self):
        return self.brand
    def get_model(self):
        return self.model
    def get_price(self):
        return self.price
    
    def set_brand(self,brand):
        self.brand = brand
    def set_model(self,model):
        self.model = model
    def set_price(self,price):
        self.price = price

class Mercedes(car):
    def __init__(self, model, price) -> None:
        super().__init__( model, price)
        self.brand = "Mercedes"
class Audi(car):
    def __init__(self, model, price) -> None:
        super().__init__( self,model, price)
        self.brand = "Audi"
class Vinfast(car):
    def __init__(self, model, price) -> None:
        super().__init__( model, price)
        self.brand = "Vinfast"

amg=Mercedes("AMG GT-R",100000000)
amg.set_model("G63 AMG")
amg.show_info()