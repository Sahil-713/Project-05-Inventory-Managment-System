# Project 05 – Inventory Management System

## Overview

The Inventory Management System is a Python-based application developed using Object-Oriented Programming (OOP) concepts. It helps users manage product information, monitor stock quantities, maintain inventory records, and generate inventory reports.

The project provides a menu-driven interface that allows users to perform different inventory management operations through a simple terminal.

## Features

- **Add Products:** Add new products with product ID, name, category, price, and quantity.
- **Display Products:** View all available products and their details.
- **Update Products:** Modify product name, category, price, or quantity.
- **Delete Products:** Remove products from the inventory with confirmation.
- **Search Products:** Find products using their unique product ID.
- **Inventory Reports:** Generate reports containing total products, stock quantity, inventory value, and low-stock products.
- **CSV File Handling:** Automatically save and load product records using CSV files.
- **Exception Handling:** Handle invalid inputs, negative values, and file-related errors.

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- CSV Module
- OS Module
- Datetime Module
- Exception Handling

## OOP Concepts Implemented

1. **Encapsulation:** Product attributes are kept private and accessed through getter and setter methods.
2. **Classes and Objects:** The project uses `Product` and `InventoryManagement` classes.
3. **Data Abstraction:** Product operations are organized into reusable methods.

## Project Structure

```text
Project-05-Inventory-Management-System/
│
├── Screenshots/
│
├── Inventory Management System.py
├── products.csv
├── inventory_report.txt
└── README.md
```

*Note: `products.csv` and `inventory_report.txt` are generated automatically when the application saves product records or generates an inventory report.*

## How to Run the Project

**Step 1:** Install Python 3 on your system.

**Step 2:** Clone the repository:

```bash
git clone https://github.com/Sahil-713/Project-05-Inventory-Management-System.git
```

**Step 3:** Open the project directory:

```bash
cd Project-05-Inventory-Management-System
```

**Step 4:** Run the Python program:

```bash
python "Inventory Management System.py"
```

## Application Menu

```text
=============================================
       INVENTORY MANAGEMENT SYSTEM
=============================================
1. Add Product
2. Display All Products
3. Update Product
4. Delete Product
5. Search Product
6. Generate Inventory Report
7. Exit
=============================================
```

## Inventory Report

The application generates an inventory report containing:

- Total number of products
- Total stock quantity
- Total inventory value
- Individual product details
- Low-stock products (quantity of 5 or less)

The report is saved automatically as `inventory_report.txt`.

## Learning Outcomes

Through this project, I practised:

- Implementing classes and objects in Python.
- Using encapsulation and data validation.
- Performing CRUD operations (Create, Read, Update, Delete).
- Reading and writing CSV files.
- Handling invalid inputs using try-except blocks.
- Generating reports using Python.

## Author

**Sahil Singh**

GitHub: [Sahil-713](https://github.com/Sahil-713)

---

*This project was developed as part of Python programming and Object-Oriented Programming practice.*
