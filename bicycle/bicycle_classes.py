class Customer(object):
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

class Bike(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class BikeShop(object):

    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.inventory = []
    
    def print_inventory(self):
        print "The current inventory at %s is... " % (self.name)
        for bike in self.inventory:
            print "The model name is {0} and the price is ${1}".format(bike.name, bike.price)
     
    def get_bikes(self, bikes):
        for bike in bikes:
            self.inventory.append(bike)
            bike.price = bike.cost * (1 + self.margin)
    
    def sell_bikes(self, customer):
        for person in customer:
            self.personal_list = []
            for items in self.inventory:
                if items.price <= person.budget:
                    self.personal_list.append(items.name)
            print "Hi {0}! Here are the bikes that are availble within your price range {1}".format(person.name, self.personal_list)
        
        for person in customer:
            bike_choice = raw_input("Let's start with {0}, which bike would you like to purchase? ".format(person.name)).capitalize()
            for items in self.inventory:
                if items == bike_choice:
                    print "The %s is an excellent choice! " % (items)
                    print "The cost of the bike is %d " % (items.price)
                    leftover_money = str(customer.budget - items.price)
                    print "The amount you have left over is {0}".format(leftover_money)
                    self.inventory.remove(items)
                    print self.inventory
                else:
                    break
            
"""These are the bikes"""           
bike1 = Bike("Speed", 10, 100)
bike2 = Bike("Criuse", 12, 200)
bike3 = Bike("Devil", 14, 300)
bike4 = Bike("Mach", 16, 400)
bike5 = Bike("Racer", 18, 500)
bike6 = Bike("Ultimate", 20, 600)
bike_inventory = [bike1, bike2, bike3, bike4, bike5, bike6]

"""These are the customers"""
customer1 = Customer("Gabe", 200)
customer2 = Customer("Yohei", 500)
customer3 = Customer("Thomas", 1000)
customer_list = [customer1, customer2, customer3]

"""This is the bike shop and we are putting the bikes into the bike shop's inventory"""
bikeshop = BikeShop("Jay's Cycles", 0.2)
bikeshop.get_bikes(bike_inventory)

"""Print the customer names and see which bikes they are able to afford"""
bikeshop.sell_bikes(customer_list)