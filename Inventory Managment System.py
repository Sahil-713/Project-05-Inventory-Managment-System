
import csv
import os
from datetime import datetime


PRODUCT_FILE = "products.csv"
REPORT_FILE = "inventory_report.txt"


# ==============================
# Product Class
# ==============================
class Product:

    def __init__(self, product_id, name, category, price, quantity):

        self.__product_id = product_id
        self.__name = name
        self.__category = category
        self.__price = float(price)
        self.__quantity = int(quantity)

        if self.__price < 0 or self.__quantity < 0:
            raise ValueError("Price and quantity cannot be negative.")

    # Getters
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    # Setters
    def set_name(self, name):
        if not name.strip():
            raise ValueError("Product name cannot be empty.")
        self.__name = name.strip()

    def set_category(self, category):
        if not category.strip():
            raise ValueError("Category cannot be empty.")
        self.__category = category.strip()

    def set_price(self, price):
        price = float(price)
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price

    def set_quantity(self, quantity):
        quantity = int(quantity)
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = quantity

    # Calculate total value of product stock
    def calculate_stock_value(self):
        return self.__price * self.__quantity

    # Convert product details into dictionary for CSV
    def to_csv_row(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "category": self.__category,
            "price": self.__price,
            "quantity": self.__quantity
        }


# ==============================
# Inventory Management Class
# ==============================
class InventoryManagement:

    FIELDNAMES = [
        "product_id", "name", "category", "price", "quantity"
    ]

    def __init__(self):
        self.__products = []
        self.load_products()

    # Find product using ID
    def find_product(self, product_id):

        for product in self.__products:
            if product.get_product_id().lower() == product_id.lower():
                return product

        return None

    # Add a new product
    def add_product(self, product):

        if self.find_product(product.get_product_id()):
            raise ValueError("Product ID already exists.")

        self.__products.append(product)
        self.save_products()

    # Load products from CSV file
    def load_products(self):

        if not os.path.exists(PRODUCT_FILE):
            return

        try:
            with open(PRODUCT_FILE, "r", newline="", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for row in reader:
                    product = Product(
                        row["product_id"],
                        row["name"],
                        row["category"],
                        float(row["price"]),
                        int(row["quantity"])
                    )

                    if not self.find_product(product.get_product_id()):
                        self.__products.append(product)

        except (OSError, csv.Error, ValueError, KeyError) as error:
            print("Error loading products:", error)

    # Save products to CSV file
    def save_products(self):

        try:
            with open(PRODUCT_FILE, "w", newline="", encoding="utf-8") as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=self.FIELDNAMES
                )

                writer.writeheader()

                for product in self.__products:
                    writer.writerow(product.to_csv_row())

        except OSError as error:
            print("Error saving products:", error)

    # Display all products
    def display_products(self):

        if not self.__products:
            print("\nNo products available in inventory.")
            return

        print("\n" + "=" * 85)
        print(
            f"{'ID':<12}{'NAME':<22}{'CATEGORY':<18}"
            f"{'PRICE':>13}{'QUANTITY':>12}{'STOCK VALUE':>15}"
        )
        print("=" * 85)

        for product in self.__products:

            print(
                f"{product.get_product_id():<12}"
                f"{product.get_name():<22}"
                f"{product.get_category():<18}"
                f"{product.get_price():>13.2f}"
                f"{product.get_quantity():>12}"
                f"{product.calculate_stock_value():>15.2f}"
            )

        print("=" * 85)

    # Search product using ID
    def search_product(self, product_id):

        product = self.find_product(product_id)

        if product:
            print("\nProduct Found!")
            print("Product ID:", product.get_product_id())
            print("Name:", product.get_name())
            print("Category:", product.get_category())
            print(f"Price: Rs. {product.get_price():,.2f}")
            print("Quantity:", product.get_quantity())
            print(
                f"Stock Value: Rs. "
                f"{product.calculate_stock_value():,.2f}"
            )

        else:
            print("Product not found.")

    # Update existing product
    def update_product(self, product_id):

        product = self.find_product(product_id)

        if not product:
            print("Product not found.")
            return

        print("\nCurrent Product Details:")
        print("1. Update Name")
        print("2. Update Category")
        print("3. Update Price")
        print("4. Update Quantity")
        print("5. Update All Details")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = get_non_empty_input("Enter new product name: ")
                product.set_name(name)

            elif choice == "2":
                category = get_non_empty_input("Enter new category: ")
                product.set_category(category)

            elif choice == "3":
                price = get_non_negative_float("Enter new price: ")
                product.set_price(price)

            elif choice == "4":
                quantity = get_non_negative_integer("Enter new quantity: ")
                product.set_quantity(quantity)

            elif choice == "5":
                name = get_non_empty_input("Enter new name: ")
                category = get_non_empty_input("Enter new category: ")
                price = get_non_negative_float("Enter new price: ")
                quantity = get_non_negative_integer("Enter new quantity: ")

                product.set_name(name)
                product.set_category(category)
                product.set_price(price)
                product.set_quantity(quantity)

            else:
                print("Invalid choice.")
                return

            self.save_products()
            print("Product updated successfully.")

        except ValueError as error:
            print("Could not update product:", error)

    # Delete product
    def delete_product(self, product_id):

        product = self.find_product(product_id)

        if not product:
            print("Product not found.")
            return

        confirmation = input(
            f"Are you sure you want to delete "
            f"{product.get_name()}? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":

            self.__products.remove(product)
            self.save_products()

            print("Product deleted successfully.")

        else:
            print("Deletion cancelled.")

    # Generate inventory report
    def generate_inventory_report(self):

        if not self.__products:
            print("\nNo products available to generate a report.")
            return

        total_products = len(self.__products)

        total_quantity = sum(
            product.get_quantity() for product in self.__products
        )

        total_value = sum(
            product.calculate_stock_value()
            for product in self.__products
        )

        low_stock = [
            product for product in self.__products
            if product.get_quantity() <= 5
        ]

        # Build report line by line
        report_lines = [
            "=" * 60,
            "              INVENTORY REPORT",
            "=" * 60,
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            "-" * 60,
            f"Total Products       : {total_products}",
            f"Total Stock Quantity : {total_quantity}",
            f"Total Inventory Value: Rs. {total_value:,.2f}",
            "-" * 60,
            "PRODUCT DETAILS",
            "-" * 60
        ]

        for product in self.__products:
            report_lines.append(
                f"ID: {product.get_product_id()} | "
                f"Name: {product.get_name()} | "
                f"Quantity: {product.get_quantity()} | "
                f"Value: Rs. {product.calculate_stock_value():,.2f}"
            )

        report_lines.extend([
            "-" * 60,
            "LOW STOCK PRODUCTS (5 OR LESS)"
        ])

        if low_stock:
            for product in low_stock:
                report_lines.append(
                    f"{product.get_name()} - "
                    f"Remaining Quantity: {product.get_quantity()}"
                )
        else:
            report_lines.append("No low stock products.")

        report_lines.append("=" * 60)

        report = "\n".join(report_lines) + "\n"

        try:
            with open(REPORT_FILE, "w", encoding="utf-8") as file:
                file.write(report)

            print("\nInventory report generated successfully.")
            print("Report saved to:", REPORT_FILE)

        except OSError as error:
            print("Error generating report:", error)


# ==============================
# Input Validation Functions
# ==============================
def get_non_empty_input(prompt):

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_non_negative_float(prompt):

    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Please enter zero or a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Enter a valid number.")


def get_non_negative_integer(prompt):

    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Please enter zero or a positive integer.")
                continue

            return value

        except ValueError:
            print("Invalid input. Enter a whole number.")


# ==============================
# Add Product Menu
# ==============================
def add_product_menu(inventory):

    print("\n--- Add New Product ---")

    product_id = get_non_empty_input("Enter product ID: ")

    if inventory.find_product(product_id):
        print("A product with this ID already exists.")
        return

    name = get_non_empty_input("Enter product name: ")
    category = get_non_empty_input("Enter product category: ")
    price = get_non_negative_float("Enter product price (Rs.): ")
    quantity = get_non_negative_integer("Enter product quantity: ")

    try:
        product = Product(
            product_id, name, category, price, quantity
        )

        inventory.add_product(product)

        print("Product added successfully.")

    except ValueError as error:
        print("Could not add product:", error)


# ==============================
# Search Product Menu
# ==============================
def search_product_menu(inventory):

    product_id = input("Enter product ID to search: ").strip()

    inventory.search_product(product_id)


# ==============================
# Update Product Menu
# ==============================
def update_product_menu(inventory):

    product_id = input("Enter product ID to update: ").strip()

    inventory.update_product(product_id)


# ==============================
# Delete Product Menu
# ==============================
def delete_product_menu(inventory):

    product_id = input("Enter product ID to delete: ").strip()

    inventory.delete_product(product_id)


# ==============================
# Main Function
# ==============================
def main():

    inventory = InventoryManagement()

    while True:

        print("\n" + "=" * 45)
        print("       INVENTORY MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Product")
        print("2. Display All Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Generate Inventory Report")
        print("7. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_product_menu(inventory)

        elif choice == "2":
            inventory.display_products()

        elif choice == "3":
            update_product_menu(inventory)

        elif choice == "4":
            delete_product_menu(inventory)

        elif choice == "5":
            search_product_menu(inventory)

        elif choice == "6":
            inventory.generate_inventory_report()

        elif choice == "7":
            inventory.save_products()
            print("Inventory saved. Thank you for using the system!")
            break

        else:
            print("Invalid choice. Please select between 1 and 7.")


# Start the program
if __name__ == "__main__":
    main()
