"""
Reports Module
--------------
Generates comprehensive inventory and sales summaries with statistics.
"""


class Report:
    """Generates formatted reports for inventory and sales."""
    
    LOW_STOCK_THRESHOLD = 10  # Configurable low stock threshold
    
    def inventory_report(self, inventory_manager):
        """
        Prints comprehensive inventory report with statistics.
        
        Args:
            inventory_manager (InventoryManager): Inventory manager instance
        """
        print("\n" + "="*70)
        print(" "*25 + "INVENTORY REPORT")
        print("="*70)
        
        if not inventory_manager.products:
            print("No products in inventory.")
            return
        
        products = sorted(inventory_manager.products.values(), key=lambda p: p.product_id)
        low_stock_items = []
        out_of_stock_items = []
        
        for product in products:
            if product.stock == 0:
                status = "OUT OF STOCK"
                out_of_stock_items.append(product)
            elif product.stock <= self.LOW_STOCK_THRESHOLD:
                status = "LOW STOCK"
                low_stock_items.append(product)
            else:
                status = "In Stock"
            
            print(f"{product} | Status: {status}")
        
        # Summary statistics
        total_products = len(products)
        total_value = inventory_manager.get_total_inventory_value()
        total_items = sum(p.stock for p in products)
        
        print("\n" + "-"*70)
        print("SUMMARY:")
        print(f"  Total Products: {total_products}")
        print(f"  Total Items in Stock: {total_items}")
        print(f"  Total Inventory Value: ${total_value:.2f}")
        print(f"  Low Stock Items ({self.LOW_STOCK_THRESHOLD} or less): {len(low_stock_items)}")
        print(f"  Out of Stock Items: {len(out_of_stock_items)}")
        
        if low_stock_items:
            print(f"\n  ⚠️  Low Stock Alert: {', '.join(p.name for p in low_stock_items)}")
        if out_of_stock_items:
            print(f"  ❌ Out of Stock Alert: {', '.join(p.name for p in out_of_stock_items)}")
        
        print("="*70)

    def sales_report(self, sales_manager):
        """
        Prints comprehensive sales report with statistics.
        
        Args:
            sales_manager (SalesManager): Sales manager instance
        """
        print("\n" + "="*70)
        print(" "*27 + "SALES REPORT")
        print("="*70)
        
        if not sales_manager.sales:
            print("No sales recorded.")
            return
        
        total_revenue = sales_manager.get_total_revenue()
        total_sales_count = sales_manager.get_sales_count()
        
        print(f"Total Sales Transactions: {total_sales_count}")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"Average Sale Value: ${total_revenue / total_sales_count:.2f}")
        
        # Calculate product statistics
        product_sales = {}
        product_revenue = {}
        
        for sale in sales_manager.sales:
            prod_name = sale.product.name
            product_sales[prod_name] = product_sales.get(prod_name, 0) + sale.quantity
            product_revenue[prod_name] = product_revenue.get(prod_name, 0) + sale.total_value
        
        if product_sales:
            # Most sold by quantity
            most_sold = max(product_sales, key=product_sales.get)
            most_sold_qty = product_sales[most_sold]
            
            # Highest revenue
            highest_revenue = max(product_revenue, key=product_revenue.get)
            highest_revenue_amount = product_revenue[highest_revenue]
            
            print("\n" + "-"*70)
            print("TOP PRODUCTS:")
            print(f"  Most Sold by Quantity: {most_sold} ({most_sold_qty} units)")
            print(f"  Highest Revenue: {highest_revenue} (${highest_revenue_amount:.2f})")
            
            print("\n" + "-"*70)
            print("SALES BY PRODUCT:")
            for prod_name in sorted(product_sales.keys()):
                qty = product_sales[prod_name]
                revenue = product_revenue[prod_name]
                print(f"  {prod_name}: {qty} units, ${revenue:.2f} revenue")
        
        print("="*70)
