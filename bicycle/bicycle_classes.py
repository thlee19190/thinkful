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
    
    """Print inventory for the bikeship"""
    def print_inventory(self):
        print "Welcome! The current inventory at %s is... " % (self.name)
        for bike in self.inventory:
            print "The model name is {0} and the price is ${1}".format(bike.name, bike.price)
        print "-" * 20
     
    """Input bike inventory into the shop"""
    def get_bikes(self, bikes):
        for bike in bikes:
            self.inventory.append(bike)
            bike.price = bike.cost * (1 + self.margin)
    
    """Figure out which bikes each customer can purchase given their budget"""
    def sell_bikes(self, customer):
        for person in customer:
            self.personal_list = []
            for items in self.inventory:
                if items.price <= person.budget:
                    self.personal_list.append(items.name)
            print "Hi {0}! Here are the bikes that are available within your price range {1}".format(person.name, self.personal_list)
        print "-" * 20
        
        total_revenue = 0 
        
        """Ask which bike each customer wants to purchase then figure out the economics behind it"""
        for person in customer:
            bike_choice = str(raw_input("Let's start with {0}, which bike would you like to purchase? ".format(person.name)).capitalize())
            #print bike_choice
            #print self.inventory[0].name
            #print bike_choice == self.inventory[0].name
            for items in self.inventory:
                if items.name == bike_choice:
                    print "The %s is an excellent choice! " % (items.name)
                    print "The cost of the bike is %d " % (items.price)
                    person.budget -= items.price
                    total_revenue += items.price
                    print "The amount you have left over is {0}".format(person.budget)
                    print "-" * 20
                    self.inventory.remove(items)
        
        print "Eveyone has a bike! The total revenue for Jay's Cycles is %d" % (total_revenue)    
        total_profit = total_revenue - (total_revenue / 1.2)
        print "The total profit for Jay's Cycles is %d" % (total_profit)
        print "Here are the bikes are left over..."
        for items in self.inventory:
            print items.name
            
"""These are the bikes        
bike1 = Bike("Speed", 10, 100)
bike2 = Bike("Cruise", 12, 200)
bike3 = Bike("Devil", 14, 300)
bike4 = Bike("Mach", 16, 400)
bike5 = Bike("Racer", 18, 500)
bike6 = Bike("Ultimate", 20, 600)
bike_inventory = [bike1, bike2, bike3, bike4, bike5, bike6]

#These are the customers
customer1 = Customer("Gabe", 200)
customer2 = Customer("Justine", 1000)
customer3 = Customer("Thomas", 500)
customer_list = [customer1, customer2, customer3]

#This is the bike shop and we are putting the bikes into the bike shop's inventory
bikeshop = BikeShop("Jay's Cycles", 0.2)
bikeshop.get_bikes(bike_inventory)
bikeshop.print_inventory()

#Print the customer names and see which bikes they are able to afford
bikeshop.sell_bikes(customer_list)"""