"""
Main Program
------------
Provides a menu-driven interface for the Inventory & Sales Tracking System.
"""

import sys
from inventory_manager import InventoryManager
from sales_manager import SalesManager
from reports import Report
from exceptions import (
    OutOfStockError,
    ProductAlreadyExistsError,
    ProductNotFoundError,
    InvalidProductDataError,
    InvalidQuantityError,
    InvalidPriceError,
    InvalidStockError,
    InvalidProductIdError,
    SaleNotFoundError
)


def get_int_input(prompt):
    """Helper function to get integer input with error handling."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_float_input(prompt):
    """Helper function to get float input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


def get_confirmation(prompt="Are you sure? (yes/no): "):
    """Helper function to get yes/no confirmation."""
    response = input(prompt).strip().lower()
    return response in ['yes', 'y']


def handle_add_product(inventory_manager):
    """Handle adding a new product."""
    try:
        product_id = get_int_input("Product ID: ")
        name = input("Name: ")
        price = get_float_input("Price: ")
        stock = get_int_input("Initial Stock: ")
        inventory_manager.add_product(product_id, name, price, stock)
        print("✓ Product added successfully.")
    except (ProductAlreadyExistsError, InvalidProductDataError, 
            InvalidPriceError, InvalidStockError, InvalidProductIdError) as e:
        print(f"Error: {e}")


def handle_update_product(inventory_manager):
    """Handle updating an existing product."""
    try:
        product_id = get_int_input("Product ID: ")
        name = input("New Name (or press Enter to skip): ") or None
        price_input = input("New Price (or press Enter to skip): ")
        price = float(price_input) if price_input.strip() else None
        stock_input = input("New Stock (or press Enter to skip): ")
        stock = int(stock_input) if stock_input.strip() else None
        inventory_manager.update_product(product_id, name, price, stock)
        print("✓ Product updated successfully.")
    except (ProductNotFoundError, InvalidProductDataError, 
            InvalidPriceError, InvalidStockError) as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: Invalid input format - {e}")


def handle_remove_product(inventory_manager):
    """Handle removing a product with confirmation."""
    try:
        product_id = get_int_input("Product ID: ")
        product = inventory_manager.get_product(product_id)
        print(f"\nProduct to delete: {product}")
        if get_confirmation("Are you sure you want to delete this product? (yes/no): "):
            inventory_manager.remove_product(product_id)
            print("✓ Product removed successfully.")
        else:
            print("Product deletion cancelled.")
    except ProductNotFoundError as e:
        print(f"Error: {e}")


def handle_record_sale(sales_manager, inventory_manager):
    """Handle recording a new sale."""
    try:
        product_id = get_int_input("Product ID: ")
        quantity = get_int_input("Quantity: ")
        sales_manager.record_sale(product_id, quantity, inventory_manager)
        print("✓ Sale recorded successfully.")
    except OutOfStockError as e:
        print(f"Error: {e}")
    except (ProductNotFoundError, InvalidQuantityError) as e:
        print(f"Error: {e}")


def handle_search_filter(inventory_manager):
    """Handle search/filter submenu."""
    print("\n--- Search/Filter Products ---")
    print("1. Search by Name/ID")
    print("2. Filter by Price Range")
    print("3. Filter by Stock Level")
    sub_choice = input("Enter choice: ").strip()
    
    if sub_choice == '1':
        search_term = input("Enter product name or ID: ").strip()
        results = inventory_manager.search_products(search_term)
        if results:
            print(f"\n✓ Found {len(results)} product(s):")
            for product in results:
                print(product)
        else:
            print("No products found matching your search.")
    
    elif sub_choice == '2':
        try:
            min_price_input = input("Minimum price (or press Enter to skip): ").strip()
            min_price = float(min_price_input) if min_price_input else None
            max_price_input = input("Maximum price (or press Enter to skip): ").strip()
            max_price = float(max_price_input) if max_price_input else None
            
            results = inventory_manager.filter_by_price_range(min_price, max_price)
            if results:
                print(f"\n✓ Found {len(results)} product(s):")
                for product in results:
                    print(product)
            else:
                print("No products found in the specified price range.")
        except ValueError as e:
            print(f"Error: Invalid price format - {e}")
    
    elif sub_choice == '3':
        try:
            threshold_input = input("Stock threshold (default 10): ").strip()
            threshold = int(threshold_input) if threshold_input else 10
            level = input("Show low stock products? (yes/no, default yes): ").strip().lower()
            low_stock = level != 'no'
            
            results = inventory_manager.filter_by_stock_level(threshold, low_stock)
            status = "low stock" if low_stock else "adequate stock"
            if results:
                print(f"\n✓ Found {len(results)} product(s) with {status}:")
                for product in results:
                    print(product)
            else:
                print(f"No products found with {status}.")
        except ValueError as e:
            print(f"Error: Invalid input - {e}")
    
    else:
        print("Invalid choice.")


def handle_cancel_sale(sales_manager, inventory_manager):
    """Handle cancelling/refunding a sale."""
    try:
        sale_id = get_int_input("Sale ID to cancel/refund: ")
        sale = sales_manager.get_sale(sale_id)
        print(f"\nSale to cancel: {sale}")
        if get_confirmation("Are you sure you want to cancel this sale? (yes/no): "):
            sales_manager.cancel_sale(sale_id, inventory_manager)
            print("✓ Sale cancelled and stock restored successfully.")
        else:
            print("Sale cancellation aborted.")
    except (SaleNotFoundError, ProductNotFoundError) as e:
        print(f"Error: {e}")


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("  INVENTORY & SALES TRACKING SYSTEM")
    print("="*50)
    print("1.  Add Product")
    print("2.  Update Product")
    print("3.  Remove Product")
    print("4.  List Products")
    print("5.  Record Sale")
    print("6.  List Sales")
    print("7.  Inventory Report")
    print("8.  Sales Report")
    print("9.  Search/Filter Products")
    print("10. Cancel/Refund Sale")
    print("11. Exit")
    print("="*50)


def main():
    """Main program loop."""
    inventory_manager = InventoryManager()
    sales_manager = SalesManager()
    report = Report()

    print("\nWelcome to the Inventory & Sales Tracking System!")
    
    while True:
        display_menu()
        choice = input("Enter choice (1-11): ").strip()
        
        # Validate menu choice
        valid_choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        if choice not in valid_choices:
            print(f"❌ Invalid choice '{choice}'. Please enter a number between 1 and 11.")
            continue
        
        if choice == '1':
            handle_add_product(inventory_manager)
        
        elif choice == '2':
            handle_update_product(inventory_manager)
        
        elif choice == '3':
            handle_remove_product(inventory_manager)
        
        elif choice == '4':
            inventory_manager.list_products()
        
        elif choice == '5':
            handle_record_sale(sales_manager, inventory_manager)
        
        elif choice == '6':
            sales_manager.list_sales()
        
        elif choice == '7':
            report.inventory_report(inventory_manager)
        
        elif choice == '8':
            report.sales_report(sales_manager)
        
        elif choice == '9':
            handle_search_filter(inventory_manager)
        
        elif choice == '10':
            handle_cancel_sale(sales_manager, inventory_manager)
        
        elif choice == '11':
            if get_confirmation("Are you sure you want to exit? (yes/no): "):
                print("\n" + "="*50)
                print("Thank you for using the Inventory & Sales System!")
                print("Goodbye!")
                print("="*50 + "\n")
                sys.exit(0)
            else:
                print("Exit cancelled.")


if __name__ == "__main__":
    main()
