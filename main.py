class Department:
    def __init__(self):
        self.fruits = []
        self.vegetables = []
        self.dry_products = []
        self.meat = []
        self.rated_products = []

    def seller_department(self):
        while True:
            print("\nSeller's Department:")
            print("1. Add a Fruit")
            print("2. Add a Vegetable")
            print("3. Add a Dry Product")
            print("4. Add Meat")
            print("5. Rate a Product")
            print("6. Exit Seller's Department")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter the name of the fruit: ")
                price = float(input("Enter the price: "))
                self.fruits.append((name, price))
                print(f"{name} added to the fruits list.")
            elif choice == '2':
                name = input("Enter the name of the vegetable: ")
                price = float(input("Enter the price: "))
                self.vegetables.append((name, price))
                print(f"{name} added to the vegetables list.")
            elif choice == '3':
                name = input("Enter the name of the dry product: ")
                price = float(input("Enter the price: "))
                self.dry_products.append((name, price))
                print(f"{name} added to the dry products list.")
            elif choice == '4':
                name = input("Enter the name of the meat: ")
                price = float(input("Enter the price: "))
                self.meat.append((name, price))
                print(f"{name} added to the meat list.")
            elif choice == '5':
                self.rate_product()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def rate_product(self):
        print("Rated Products:")
        for idx, product in enumerate(self.rated_products):
            print(f"{idx + 1}. {product}")
        print("Enter the number of the product to rate (# to stop rating): ")
        while True:
            rating_choice = input()
            if rating_choice == "#":
                break
            try:
                rating_choice = int(rating_choice)
                if 1 <= rating_choice <= len(self.rated_products):
                    product = self.rated_products.pop(rating_choice - 1)
                    print(f"{product} rated successfully.")
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input. Please enter a valid product number or # to stop.")

    def buyer_department(self):
        total_cost = 0
        while True:
            print("\nBuyer's Department:")
            print("1. Buy a Fruit")
            print("2. Buy a Vegetable")
            print("3. Buy a Dry Product")
            print("4. Buy Meat")
            print("5. End Purchase")

            choice = input("Enter your choice: ")

            if choice in ['1', '2', '3', '4']:
                department = None
                if choice == '1':
                    department = self.fruits
                elif choice == '2':
                    department = self.vegetables
                elif choice == '3':
                    department = self.dry_products
                elif choice == '4':
                    department = self.meat

                print("Available Products:")
                for idx, (name, price) in enumerate(department):
                    print(f"{idx + 1}. {name} - {price} so'm")

                product_choice = int(input("Enter the number of the product to buy: ")) - 1
                if 0 <= product_choice < len(department):
                    product_name, product_price = department[product_choice]
                    quantity = int(input(f"Enter the quantity of {product_name} to buy: "))
                    total_cost += product_price * quantity
                    print(f"You bought {quantity} {product_name}(s) for {product_price * quantity} so'm.")
                else:
                    print("Invalid product number. Please try again.")
            elif choice == '5':
                print(f"\nTotal Cost of Purchase: ${total_cost}")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def run(self):
        while True:
            print("\nMain Menu:")
            print("1. Seller's Department")
            print("2. Buyer's Department")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.seller_department()
            elif choice == '2':
                self.buyer_department()
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    store = Department()
    store.run()
      
