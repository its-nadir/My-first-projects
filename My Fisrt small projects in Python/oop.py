class Cheese:
    def __init__(self, name, milkType, country, cheeseType, age, quantity, pricePerKg):
        self.name = name

        self.milkType = milkType
        self.country = country
        self.cheeseType = cheeseType
        self.age = age
        self.quantity = quantity
        self.pricePerKg = pricePerKg

    def describe(self):
        print(f"{self.name} is a {self.cheeseType} cheese from {self.country}. "
              f"It's made from {self.milkType} milk, aged {self.age} months, "
              f"costs {self.pricePerKg:.2f} PLN per kg, and we have {self.quantity} kg available.")

class CheeseShop:
    def __init__(self, shopName):
        self.shopName = shopName
        self.inventory = []

    def addCheese(self, cheese):
        self.inventory.append(cheese)
        print(f"We have added {cheese.name} to our selection!")

    def listCheeses(self):
        if not self.inventory:
            print("Sorry, we're out of that cheese right now.")
        else:
            for cheese in self.inventory:
                cheese.describe()

    def findCheese(self, cheeseName):
        for cheese in self.inventory:
            if cheese.name.lower() == cheeseName.lower():
                return cheese
        print(f"Apologies, we're currently out of {cheeseName} cheese.")

    def buyCheese(self, cheeseName, weightInKg):
        cheese = self.findCheese(cheeseName)
        if cheese:
            if weightInKg <= cheese.quantity:
                cheese.quantity -= weightInKg
                totalCost = weightInKg * cheese.pricePerKg
                print(f"You've bought {weightInKg} kg of {cheeseName} for {totalCost:.2f} PLN.")
            else:
                print(f"We have only {cheese.quantity} kg remaining of {cheeseName}.")

def main():
    shop = CheeseShop("Mario Cheese Shop")

    while True:
        print("\nWelcome to Mario Cheese Shop!")
        print("1. Add a new cheese")
        print("2. Show me all the cheeses")
        print("3. I want to buy some cheese")
        print("4. I'm done, thanks!")

        choice = input("What would you like to do? ")

        if choice == '1':
            name = input("Enter the cheese name (e.g: Cheddar, Gouda, Mozzarella....): ").capitalize()
            milkType = input("What type of milk is it made from (e.g: cow, goat, mixed ....)? ")
            country = input("Where is it from? ")
            cheeseType = input("What type of cheese is it (e.g: soft, hard, creamy...)? ")
            age = int(input("How old is the cheese (in months)? "))
            quantity = float(input("How much do we have (in kg)? "))
            pricePerKg = float(input("What's the price per kg (in PLN)? "))
            
            newCheese = Cheese(name, milkType, country, cheeseType, age, quantity, pricePerKg)
            shop.addCheese(newCheese)

        elif choice == '2':
            shop.listCheeses()

        elif choice == '3':
            if not shop.inventory:
                print("Sorry, we don't have any cheese available at the moment.")
            else:
                print("Available cheeses:")
                for cheese in shop.inventory:
                    print(f"{cheese.name} - Price per kg: {cheese.pricePerKg:.2f} PLN")
                
                cheeseName = input("Which cheese would you like to purchase? ")
                selectedCheese = shop.findCheese(cheeseName)
                
                if selectedCheese:
                    weightInKg = float(input(f"How much {selectedCheese.name} would you like to buy (in kg)? "))
                    shop.buyCheese(selectedCheese.name, weightInKg)

        elif choice == '4':
            print("Thank you for visiting Mario Cheese Shop. Have a wonderful day!")
            break

        else:
            print("I'm not sure what that means. Could you try again?")

main()