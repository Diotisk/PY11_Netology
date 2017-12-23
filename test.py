class Animal:
    weight = 0
    age = 0

    def __init__(self, weight, age):
        self.weight = weight
        self.age = age

    def feed(self):
        feed_amount = float(input("Enter amount of feed in kg"))
        print("The animal is fed with", feed_amount, "kg")
        return feed_amount

    def graze(self):
        graze_durance = float(input("Enter amount of graze hours"))
        print("The animal has been grazed for", graze_durance, "hours")
        return graze_durance

class Livestock(Animal):

    def __init__(self, weight, age, colour):
        self.colour = colour
        super().__init__(weight, age)

class Cow(Livestock):
    colour = None

    def cow_milk(self):
        cow_milk_amount = float(input("Enter amount of milk in litres"))
        print("Got", cow_milk_amount, "litres of cow milk")
        return cow_milk_amount

class Goat(Livestock):
    colour = None

    def goat_milk(self):
        goat_milk_amount = float(input("Enter amount of milk in litres"))
        print("Got", goat_milk_amount, "litres of goat milk")
        return goat_milk_amount

class Sheep(Livestock):
    colour = None

    def sheep_milk(self):
        sheep_milk_amount = float(input("Enter amount of milk in litres"))
        print("Got", sheep_milk_amount, "litres of sheep milk")
        return sheep_milk_amount

    def shear(self):
        wool_amount = float(input("Enter amount of wool in kg"))
        print("Got", wool_amount, "kg of wool")
        return wool_amount

class Pig(Livestock):
    colour = None

class Poultry(Animal):

    def __init__(self, weight, age, colour):
        self.colour = colour
        super().__init__(weight, age)

class Duck(Poultry):
    colour = None

    def lay_eggs_duck(self):
        duck_egg_amount = int(input("Enter the amount of eggs"))
        print(duck_egg_amount, "of eggs were laid.")
        return duck_egg_amount

class Chicken(Poultry):
    colour = None

    def lay_eggs_chicken(self):
        chicken_egg_amount = int(input("Enter the amount of eggs"))
        print(chicken_egg_amount, "of eggs were laid.")
        return chicken_egg_amount

class Goose(Poultry):
    colour = None

    def pluck(self):
        feather_amount = float(input("Enter amount of feather in kg"))
        print("Got {} kg of goose feather".format(feather_amount))
        return feather_amount

#Test
Goose_0 = Goose(9, 2, "grey")
Goose_1 = Goose(7.5, 3, "white")
Goose_2 = Goose(4.4, 3.6, "rose")

Geese = [Goose_0, Goose_1, Goose_2]
sum_feather = []

for i in Geese:
    print(i.__dict__)
    sum_feather.append(i.pluck())

print("You got {} goose feather.".format(sum(sum_feather)))