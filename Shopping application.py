#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, apnabazaar, project):
        self.username = apnabazaar
        self.password = project
        
class ApnaBazaarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apna Bazaar")
        
        self.users = [User("apnabazaar", "project")]  
        self.cart = []
        self.items = {}
        self.prices = {}
        
        self.create_login_screen()

    def create_login_screen(self):
        self.clear_window()
        
        self.label = tk.Label(self.root, text="***Welcome To Apna Bazaar***", font=("Arial", 16))
        self.label.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", command=self.authenticate_user)
        self.login_button.pack(pady=20)

    def authenticate_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        for user in self.users:
            if user.username == username and user.password == password:
                self.login_successful()
                return
        messagebox.showerror("Authentication Failed", "Invalid username or password.")

    def login_successful(self):
        self.clear_window()
        
        self.main_menu_button = tk.Button(self.root, text="Go to Main Menu", command=self.show_main_menu)
        self.main_menu_button.pack(pady=20)

    def show_main_menu(self):
        self.clear_window()

        self.root.geometry("300x250")
        
        self.main_label = tk.Label(self.root, text="Choose an Option", font=("Arial", 14))
        self.main_label.pack(pady=10)

        self.add_to_cart_button = tk.Button(self.root, text="Add item to cart", command=self.add_item_to_cart)
        self.add_to_cart_button.pack(pady=10)

        self.view_cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        self.view_cart_button.pack(pady=10)

        self.remove_from_cart_button = tk.Button(self.root, text="Remove item from cart", command=self.remove_from_cart)
        self.remove_from_cart_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)
        self.exit_button.pack(pady=10)

    def add_item_to_cart(self):
        self.clear_window()

        self.category_label = tk.Label(self.root, text="Choose a category:", font=("Arial", 12))
        self.category_label.pack(pady=10)

        self.category_button_clothes = tk.Button(self.root, text="Clothes", command=lambda: self.show_items(1))
        self.category_button_clothes.pack(pady=5)

        self.category_button_grocery = tk.Button(self.root, text="Grocery", command=lambda: self.show_items(2))
        self.category_button_grocery.pack(pady=5)

        self.category_button_electronics = tk.Button(self.root, text="Electronics", command=lambda: self.show_items(3))
        self.category_button_electronics.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.show_main_menu)
        self.back_button.pack(pady=20)

    def show_items(self, category):
        self.clear_window()
        
        self.items = {}
        self.prices = {}
        
        if category == 1:  # Clothes
            self.items = {1: "T-shirt", 2: "Jeans", 3: "Dress"}
            self.prices = {1: 10, 2: 20, 3: 30}
        elif category == 2:  # Grocery
            self.items = {1: "Bread", 2: "Milk", 3: "Eggs"}
            self.prices = {1: 2, 2: 3, 3: 4}
        elif category == 3:  # Electronics
            self.items = {1: "Laptop", 2: "Smartphone", 3: "Headphones"}
            self.prices = {1: 500, 2: 300, 3: 50}

        self.item_label = tk.Label(self.root, text="Choose an item to add to the cart:", font=("Arial", 12))
        self.item_label.pack(pady=10)

        for item_num, item_name in self.items.items():
            button = tk.Button(self.root, text=f"{item_name} - ${self.prices[item_num]}", 
                               command=lambda item=item_name, price=self.prices[item_num]: self.add_to_cart(item, price))
            button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back to Categories", command=self.add_item_to_cart)
        self.back_button.pack(pady=20)

    def add_to_cart(self, item, price):
        self.cart.append((item, price))
        messagebox.showinfo("Item Added", f"{item} has been added to the cart.")

    def view_cart(self):
        self.clear_window()

        if not self.cart:
            messagebox.showinfo("Cart is Empty", "Your cart is empty.")
            self.show_main_menu()
            return
        
        cart_text = "\n".join([f"{item} - ${price}" for item, price in self.cart])
        total = sum(price for _, price in self.cart)

        cart_label = tk.Label(self.root, text=f"Items in Cart:\n{cart_text}\n\nTotal: ${total}", font=("Arial", 12))
        cart_label.pack(pady=20)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.show_main_menu)
        self.back_button.pack(pady=10)

    def remove_from_cart(self):
        self.clear_window()

        if not self.cart:
            messagebox.showinfo("Cart is Empty", "Your cart is empty.")
            self.show_main_menu()
            return

        # Show the current cart items before removing one
        cart_text = "\n".join([f"{item} - ${price}" for item, price in self.cart])
        remove_label = tk.Label(self.root, text=f"Current items in your cart:\n{cart_text}\n\nEnter item name to remove:", font=("Arial", 12))
        remove_label.pack(pady=10)

        self.remove_entry = tk.Entry(self.root)
        self.remove_entry.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Item", command=self.remove_item_from_cart)
        self.remove_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.show_main_menu)
        self.back_button.pack(pady=20)

    def remove_item_from_cart(self):
        item_to_remove = self.remove_entry.get()

        for i, (cart_item, _) in enumerate(self.cart):
            if cart_item.lower() == item_to_remove.lower():  # Case insensitive matching
                del self.cart[i]
                messagebox.showinfo("Item Removed", f"{item_to_remove} has been removed from the cart.")
                self.view_cart()  # Automatically show the updated cart
                return

        messagebox.showerror("Item Not Found", "Item not found in cart.")

    def exit_app(self):
        self.root.quit()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ApnaBazaarApp(root)
    root.mainloop()


# In[ ]:




