class Menu:
    def __init__(self, menu_name):
        self.menu_dict = {}
        self.menu_name = menu_name

    def view_menu(self):
        print(self.menu_name)
        for item in self.menu_dict:
            price = self.menu_dict[item]
            print("\nItem: {item}\nPrice: ${price}".format(item = item, price = price))

    def add_item(self, item, price):
        print("Adding {item} to menu...".format(item = item))
        self.menu_dict[item] = "{:.2f}".format(price)
        print("Added {item} to {menu_name} menu with price ${price}".format(item = item, menu_name = self.menu_name, price = "{:.2f}".format(price)))

    def remove_item(self, item):
        print("Removing {item} from menu...".format(item = item))
        if item in self.menu_dict.keys():
            self.menu_dict.pop(item)
            print("{item} has been removed from the {menu_name} menu.".format(item = item, menu_name = self.menu_name))
        else:
            print("Item does not appear on {menu_name} menu. Please enter a valid item to remove.".format(menu_name = self.menu_name))
            #Still need to test
            #Would be nice to add in some formatting and functionality here to say what menu it was removed from.

appetizers = Menu("Appetizers")
appetizers.add_item("Cheese Bread" , 6.0)
appetizers.add_item("Gluten-Free Cheese Bread", 9.0)
appetizers.add_item("Artichokes", 8.0)
appetizers.add_item("Meatballs", 5.0)
appetizers.add_item("Broccoli & Cauliflower", 6.0)
appetizers.view_menu()

salads = Menu("Salads")
salads.add_item("Small House Salad", 4.5)
salads.add_item("Large House Salad", 6.0)
salads.add_item("Small Caesar", 5.0)
salads.add_item("Large Caesar", 8.0)
salads.add_item("Antipasto", 10.0)
salads.add_item("Beet Salad", 9.0)
salads.add_item("Arugula Salad", 8.0)

desserts = Menu("Desserts")
desserts.add_item("Cinnamon Sticks", 6.0)
desserts.add_item("GF!!! Cinnamon Sticks", 9.0)

#Probably need to add a new class for menu items in order to account for size, ingredients
#Price will also change based on size
#For online menu, need to add ability to change to out of stock