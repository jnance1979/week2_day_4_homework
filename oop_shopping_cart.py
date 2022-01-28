my_cart = []
class Cart:
    my_cart = []

    def __init__(self, name):
        self.name = name
    
    def remove(self, remove_item):
        my_cart.remove(remove_item)

    def add(self, new_item):
        my_cart.append(new_item)

    def clear(self):
        my_cart.clear()

item = Cart(my_cart)

def shopping_cart():
    while True:
        print("\nWelcome to the shopping cart. What would you like to do?")
        choice = input("\nTo add an item, enter 'a'\nTo remove an item, enter 'r'\nTo view all items, enter 'v'\nTo empty your cart, enter 'e'\nTo quit, enter 'q' ")
        if choice.lower() == 'a':
            new_item = input("What item would you like to add to your cart? ")
            item.add(new_item)
            print(f'{new_item} has been added.')
        elif choice.lower() == 'r':
            remove_item = input("What item would you like to remove from to your cart? ")
            if remove_item in my_cart:
                item.remove(remove_item)
                print(f'{remove_item} has been removed.')
            else:
                print(f'That item is not in your cart.')
                continue    
        elif choice.lower() == 'v':
            print (f'The items in your cart are: {my_cart}')
        elif choice.lower() == 'e':
            my_cart.clear()
            print("All items have been removed.")
        elif choice.lower() == 'q':
            print (f'The items in your cart are: {my_cart}. Goodbye!')
            break
        else:
            print ("Please choose an option from above.")

shopping_cart()