class Fighter:
    def __init__(self, name, height, weight, speed, origin, playerNum):
        #name, height, strength, weight, speed, origin, percentage, player number
        print("fighter class created!")
        self.name = name
        self.weight = weight
        self.height = height
        self.speed = speed
        self.origin = origin
        self.playerNum = playerNum
        self.percentage = 0

    def printStatus(self):
        print("---------------------------")
        print(f"Name: {self.name}")
        print(f"Damage: {self.percentage}%")
        print(f"Player number: {self.playerNum}")
        print("---------------------------")

    def attack(self,opponent):
        damage = 5
        print(f"{self.name} attacked {opponent.name} and dealt {damage}%!!!")
        opponent.percentage += damage

    def special(self,opponent):
        damage = 15
        print(f"{self.name} performed a special move on {opponent.name} and dealt {damage}%!!!")
        opponent.percentage += damage

class Samus(Fighter):
    def __init__(self,playerNum):
        print("samus class created")
        super().__init__("Samus",9,8,4,"Metroid",playerNum)
        self.isCharged = False
    
    def special(self, opponent):
        if(self.isCharged):
            damage = 35
            print(f"{self.name} fired her arm cannonat {opponent.name} and dealt {damage}%!!!")
            opponent.percentage += damage
            self.isCharged = False
        else:
            self.isCharged = True
            print(f"{self.name} is charging up her arm cannon!")

class Goku(Fighter):
    def __init__(self, playerNum):
        print("goku class created")
        super().__init__("Goku",8,7,1000000,"Dragon Ball",playerNum)
        self.power_level = 0

    def assess_power_level(self):
        if(self.percentage < 40):
            self.power_level = 5
        elif(self.percentage < 65):
            self.power_level = 100
        elif(self.percentage < 100):
            self.power_level = 1000
        elif(self.percentage < 150):
            self.power_level = 4000
        else:
            print("it's over 9000!!!!")
            self.power_level = 9001

    def attack(self,opponent):
        self.assess_power_level()
        damage = 5 + (self.power_level * .1)
        print(f"{self.name} attacked {opponent.name} and dealt {damage}%!!!")
        opponent.percentage += damage

    def special(self,opponent):
        self.assess_power_level()
        damage = 15 + (self.power_level * .1)
        print(f"{self.name} performed a kamehameha on {opponent.name} and dealt {damage}%!!!")
        opponent.percentage += damage


samus = Samus(1)
# samus.printStatus()


# steve = Fighter("Steve",6,5,3,"Minecraft",1)
# steve.printStatus()
# joker = Fighter("Joker",8,5,6,"Persona 5",2)
# joker.printStatus()
# steve.printStatus()
# joker.attack(steve)
# steve.printStatus()
# joker.printStatus()

# samus.special(steve)
# steve.printStatus()
# samus.attack(steve)
# steve.printStatus()
# samus.special(steve)
# steve.printStatus()


goku = Goku(2)
for i in range(0,20):
    samus.special(goku)
    samus.special(goku)
    goku.printStatus()

goku.special(samus)
samus.printStatus()