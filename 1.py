# FruitManager.py
class FruitManager:
    def __init__(self):
        self.fruit_stock = {}
        self.transaction_log = []

    def add_fruit_stock(self, fruit_name, quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] += quantity
        else:
            self.fruit_stock[fruit_name] = quantity
        self.transaction_log.append(f"Added {quantity} {fruit_name} to stock")

    def view_fruit_stock(self):
        return self.fruit_stock

    def update_fruit_stock(self, fruit_name, new_quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] = new_quantity
            self.transaction_log.append(f"Updated {fruit_name} stock to {new_quantity}")
        else:
            self.transaction_log.append(f"{fruit_name} not found in stock")

    def get_transaction_log(self):
        return self.transaction_log


# Customer.py
class Customer:
    def __init__(self, fruit_manager):
        self.fruit_manager = fruit_manager

    def display_menu(self):
        print("\n1. View All Stocks")
        print("2. Add Fruit Stock")
        print("3. Update Fruit Stock")
        print("4. Exit")

    def execute_menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                print("Fruit Stock:")
                print(self.fruit_manager.view_fruit_stock())
            elif choice == '2':
                fruit_name = input("Enter fruit name: ")
                quantity = int(input("Enter quantity to add: "))
                self.fruit_manager.add_fruit_stock(fruit_name, quantity)
                print("Fruit stock added successfully.")
            elif choice == '3':
                fruit_name = input("Enter fruit name to update: ")
                new_quantity = int(input("Enter new quantity: "))
                self.fruit_manager.update_fruit_stock(fruit_name, new_quantity)
                print("Fruit stock updated successfully.")
            elif choice == '4':
                self.save_transaction_log()
                print("Exiting the Fruit Store Console application. Thank you!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def save_transaction_log(self):
        with open("transaction_log.txt", "w") as file:
            for entry in self.fruit_manager.get_transaction_log():
                file.write(entry + "\n")


# Main.py
from FruitManager import FruitManager
from Customer import Customer

def main():
    fruit_manager = FruitManager()
    customer = Customer(fruit_manager)

    print("Welcome to the Fruit Store Console Application!")

    customer.execute_menu()

if __name__ == "__main__":
    main()
