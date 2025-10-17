# Inventory & Sales Tracking System

##  Domain
Retail / Sales Operations

## Problem Statement
Build a system that manages products in inventory and tracks their sales.
The system must:
- Store product details (ID, Name, Price, Stock).
- Record sales transactions.
- Update stock automatically after each sale.
- Prevent overselling with proper error handling.
- Generate reports on inventory and sales.

---

## Topics Covered
- Python basics (loops, conditionals, functions)
- Object-Oriented Programming
- Exception handling
- Modular programming
- Reports & Summaries
- (Optional) Database Integration (SQLite/MySQL)

---

## Project Structure

inventory_sales_system
│── main.py
│── product.py
│── sale.py
│── inventory_manager.py
│── sales_manager.py
│── reports.py
│── exceptions.py
│── README.md

inventory_sales_system/
│── main.py # Menu-driven program
│── product.py # Product class
│── sale.py # Sale class
│── inventory_manager.py # Handles inventory operations
│── sales_manager.py # Handles sales operations
│── reports.py # Reporting module
│── exceptions.py # Custom exceptions
│── README.md # Project documentation


## Student Task Breakdown
- **Student A (Inventory):** `product.py`,`inventory_manager.py`
- **Student B (Sales):** `sale.py`, `sales_manager.py`
- **Student C (Reports & UI):** `reports.py`, `exceptions.py`, `main.py`

## Features

### Product Management
- Add, update, and remove products
- Search products by name or ID
- Filter products by price range
- Filter products by stock level
- Comprehensive validation with custom exceptions

### Sales Management
- Record sales transactions
- Cancel/refund sales with stock restoration
- Track sales history
- Automatic stock updates

### Reports & Analytics
- Detailed inventory reports with:
  - Total inventory value
  - Low stock alerts
  - Out of stock alerts
  - Product statistics
  
- Comprehensive sales reports with:
  - Total revenue and transactions
  - Average sale value
  - Top-selling products
  - Revenue breakdown by product

### User Experience
- Menu-driven interface
- Input validation with helpful error messages
- Confirmation prompts for destructive operations
- Professional formatting with visual indicators
- Search and filter capabilities

## Recent Improvements
- ✅ Refactored code with extracted functions
- ✅ Enhanced reports with detailed statistics
- ✅ Improved currency and data formatting
- ✅ Added comprehensive docstrings
- ✅ Implemented helper functions for better UX
- ✅ Used list comprehensions for better performance
- ✅ Added 9 custom exceptions for specific error handling

## How to Run
1. Navigate to the project folder
2. Run the program:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu to manage inventory and sales
