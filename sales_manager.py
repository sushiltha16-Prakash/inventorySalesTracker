"""
Sales Manager
-------------
Handles sales recording, cancellation, and stock updates.
"""

from sale import Sale
from exceptions import OutOfStockError, InvalidQuantityError, ProductNotFoundError, SaleNotFoundError


class SalesManager:
    """Manages sales transactions and maintains sales history."""
    
    def __init__(self):
        """Initialize sales manager with empty sales list."""
        self.sales = []
        self.next_sale_id = 1

    def record_sale(self, product_id, quantity, inventory_manager):
        """
        Records a new sale transaction and reduces product stock.
        
        Args:
            product_id (int): ID of product being sold
            quantity (int): Quantity to sell
            inventory_manager (InventoryManager): Inventory manager instance
            
        Raises:
            InvalidQuantityError: If quantity is invalid
            ProductNotFoundError: If product doesn't exist
            OutOfStockError: If insufficient stock available
        """
        if not isinstance(quantity, int) or quantity <= 0:
            raise InvalidQuantityError(f"Sale quantity must be a positive integer. Received: {quantity}")
        
        product = inventory_manager.get_product(product_id)
        
        if product.stock < quantity:
            raise OutOfStockError(
                f"Insufficient stock for {product.name}. "
                f"Available: {product.stock}, Requested: {quantity}"
            )
        
        sale_id = self.next_sale_id
        self.next_sale_id += 1
        product.update_stock(-quantity)
        sale = Sale(sale_id, product, quantity)
        self.sales.append(sale)

    def list_sales(self):
        """Prints all sales transactions in chronological order."""
        if not self.sales:
            print("No sales recorded.")
            return
        print(f"\nTotal Sales: {len(self.sales)}")
        for sale in self.sales:
            print(sale)
    
    def get_sale(self, sale_id):
        """
        Retrieves a sale by ID.
        
        Args:
            sale_id (int): ID of sale to retrieve
            
        Returns:
            Sale: The requested sale
            
        Raises:
            SaleNotFoundError: If sale ID doesn't exist
        """
        for sale in self.sales:
            if sale.sale_id == sale_id:
                return sale
        raise SaleNotFoundError(f"Sale ID {sale_id} not found.")
    
    def cancel_sale(self, sale_id, inventory_manager):
        """
        Cancels a sale and restores stock if product still exists.
        
        Args:
            sale_id (int): ID of sale to cancel
            inventory_manager (InventoryManager): Inventory manager instance
            
        Raises:
            SaleNotFoundError: If sale ID doesn't exist
            ProductNotFoundError: If product was deleted (sale still cancelled)
        """
        sale = self.get_sale(sale_id)
        
        try:
            product = inventory_manager.get_product(sale.product.product_id)
            product.update_stock(sale.quantity)
            self.sales.remove(sale)
        except ProductNotFoundError:
            self.sales.remove(sale)
            raise ProductNotFoundError(
                f"Sale cancelled but product {sale.product.name} (ID: {sale.product.product_id}) "
                f"no longer exists. Stock could not be restored."
            )
    
    def get_total_revenue(self):
        """
        Calculates total revenue from all sales.
        
        Returns:
            float: Total revenue
        """
        return sum(sale.total_value for sale in self.sales)
    
    def get_sales_count(self):
        """
        Returns total number of sales transactions.
        
        Returns:
            int: Number of sales
        """
        return len(self.sales)
