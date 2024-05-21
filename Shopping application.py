#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("***Welcome To Apna Bazaar***")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def authenticate(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user.username == username and user.password == password:
            return True
    print("Authentication failed.")
    return False

def display_categories():
    print("1. Clothes")
    print("2. Grocery")
    print("3. Electronics")

def display_items(category):
    if category == 1:  # Clothes
        print("1. T-shirt - $10")
        print("2. Jeans - $20")
        print("3. Dress - $30")
    elif category == 2:  # Grocery
        print("1. Bread - $2")
        print("2. Milk - $3")
        print("3. Eggs - $4")
    elif category == 3:  # Electronics
        print("1. Laptop - $500")
        print("2. Smartphone - $300")
        print("3. Headphones - $50")

def add_to_cart(cart, item, price):
    cart.append((item, price))

def view_cart(cart):
    print("Items in Cart:")
    for item, price in cart:
        print(f"{item} - ${price}")

def delete_from_cart(cart, item):
    for i, (cart_item, _) in enumerate(cart):
        if cart_item == item:
            del cart[i]
            print(f"{item} removed from cart.")
            return
    print("Item not found in cart.")

def calculate_total(cart):
    total = sum(price for _, price in cart)
    return total

def main():
    users = [User("username", "password")]  

    if authenticate(users):
        print("Authentication successful.")
        cart = []

        while True:
            print("\nChoose an option:")
            print("1. Add item to cart")
            print("2. View cart")
            print("3. Remove items from cart")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                print("\nChoose a category:")
                display_categories()
                category_choice = int(input("Enter your choice (1-3): "))

                if category_choice in [1, 2, 3]:
                    display_items(category_choice)
                    item_choice = int(input("Enter item number to add to cart (1-3): "))

                    if category_choice == 1:
                        items = {1: "T-shirt", 2: "Jeans", 3: "Dress"}
                        prices = {1: 10, 2: 20, 3: 30}
                    elif category_choice == 2:
                        items = {1: "Bread", 2: "Milk", 3: "Eggs"}
                        prices = {1: 2, 2: 3, 3: 4}
                    elif category_choice == 3:
                        items = {1: "Laptop", 2: "Smartphone", 3: "Headphones"}
                        prices = {1: 500, 2: 300, 3: 50}

                    add_to_cart(cart, items[item_choice], prices[item_choice])
                    print(f"{items[item_choice]} added to cart.")
                else:
                    print("Invalid choice. Please choose again.")

            elif choice == '2':
                view_cart(cart)
                total = calculate_total(cart)
                print(f"Total: ${total}")

            elif choice == '3':
                item_to_remove = input("Enter the name of the item to remove from cart: ")
                delete_from_cart(cart, item_to_remove)

            elif choice == '4':
                print("\nThank you for shopping with us.")
                print("Items purchased:")
                for item, price in cart:
                    print(f"{item} - ${price}")
                total = calculate_total(cart)
                print(f"Total: ${total}")
                break

            else:
                print("Invalid choice. Please choose again.")

    else:
        print("Authentication failed. Exiting...")

if __name__ == "__main__":
    main()


# In[ ]:




