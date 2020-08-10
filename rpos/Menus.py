###This is the code for the menu class.

class Menu:
    def __init__(self):
        self.menu_dict = {}

    def view_menu(self):
        for item in self.menu_dict:
            price = self.menu_dict[item]
            print("\nItem: {item}\nPrice: {price}".format(item = item, price = price))
            #Works
    def add_item(self, item, price):
        print("Adding item to menu...")
        self.menu_dict[item] = price
        return "Added {item} to menu with price ${price}".format(item = item, price = price)
        #Works as is
        #Try adding in two decimal places using {:20.2f} for price.


    def remove_item(self, item):
        print("Removing item from menu...")
        if item in self.menu_dict.keys():
            removed_item = self.menu_dict.pop(item)
            return "{removed_item} has been removed from the menu.".format(removed_item = removed_item)
        else:
            return "Item does not appear on menu. Please enter a valid item to remove."
            #Still need to test
            #Would be nice to add in some formatting and functionality here to say what menu it was removed from.

appetizers = Menu()
appetizers.add_item("Cheese Bread" , 6.0)
appetizers.add_item("Gluten-Free Cheese Bread", 9.0)
appetizers.add_item("Artichokes", 8.0)
appetizers.add_item("Meatballs", 5.0)
appetizers.add_item("Broccoli & Cauliflower", 6.0)
print(appetizers.view_menu())

#Still need to add some functionality for ingredients.

        