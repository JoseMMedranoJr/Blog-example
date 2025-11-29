

class IceCream: 
    base_price = 1.50

    def __init__(self, flavor, scoops):
        self.flavor = flavor
        self.scoops = scoops  # maybe need to state somehow int
           
    def get_price(self):
        total_price = IceCream.base_price * self.scoops
        return total_price
      
    def __str__(self):
        return f"Your total is ${self.get_price()}."
    


class ConeIceCream(IceCream):

    def __init__(self, flavor, scoops, cone_type, cone_cost):
        super().__init__(flavor, scoops)
        self.cone_type = cone_type
        self.cone_cost = cone_cost
        
    def get_price(self):
        base_price = super().get_price() #??? do we recall, something is up here?
        return base_price + self.cone_cost
    
    def __str__(self):
        return f"Your new total is now ${self.get_price()}."


class CupIceCream(IceCream):
    

    def __init__(self, flavor, scoops, size, toppings=None):
        super().__init__(flavor, scoops)
        self.size = size

    def get_price(self):
        # total_price = IceCream.base_price * self.scoops
        # return total_price
        sizes = {small: 0, medium:1, large:2}
        if self.size = sizes[0]:  








IceCream1 = IceCream("Vanilla", 3)

IceCream2 = ConeIceCream("Chocolate", 2, "Waffle", 1)
# print(IceCream1)
print(IceCream2)


# print(IceCream.get_price(IceCream1))