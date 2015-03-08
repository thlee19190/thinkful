from bicycle_classes import Customer, Bike, BikeShop 

        
"""These are the bikes"""           
bike1 = Bike("Speed", 10, 100)
bike2 = Bike("Cruise", 12, 200)
bike3 = Bike("Devil", 14, 300)
bike4 = Bike("Mach", 16, 400)
bike5 = Bike("Racer", 18, 500)
bike6 = Bike("Ultimate", 20, 600)
bike_inventory = [bike1, bike2, bike3, bike4, bike5, bike6]

"""These are the customers"""
customer1 = Customer("Gabe", 200)
customer2 = Customer("Justine", 1000)
customer3 = Customer("Thomas", 500)
customer_list = [customer1, customer2, customer3]

"""This is the bike shop and we are putting the bikes into the bike shop's inventory"""
bikeshop = BikeShop("Jay's Cycles", 0.2)
bikeshop.get_bikes(bike_inventory)
bikeshop.print_inventory()

"""Print the customer names and see which bikes they are able to afford"""
bikeshop.sell_bikes(customer_list)