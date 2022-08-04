class Sundae:
    def __init__(self, flavor, numScoops, container):
        print("running init for sundae")
        self.flavor = flavor
        self.numScoops = numScoops
        self.container = container
        self.toppings = []

cleveland_brownie = Sundae("vanilla",3,"waffle cone")
double_chocolate = Sundae("double chocolate chunk", 2, "bowl")
print(cleveland_brownie.flavor)
print(double_chocolate.flavor)
