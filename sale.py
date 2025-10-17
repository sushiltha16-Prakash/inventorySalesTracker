"""
Sale Class
----------
Represents a single sales transaction.
"""

from datetime import datetime


class Sale:
    """Represents a completed sales transaction."""
    
    def __init__(self, sale_id, product, quantity):
        """
        Initialize a new Sale.
        
        Args:
            sale_id (int): Unique sale identifier
            product (Product): The product being sold
            quantity (int): Quantity sold
        """
        self.sale_id = sale_id
        self.product = product
        self.quantity = quantity
        self.total_value = product.price * quantity
        self.date = datetime.now()

    def __str__(self):
        """Returns formatted sale information."""
        return (f"Sale ID: {self.sale_id} | Product: {self.product.name} | "
                f"Qty: {self.quantity} | Total: ${self.total_value:.2f} | "
                f"Date: {self.date.strftime('%Y-%m-%d %H:%M')}")
    
    def __repr__(self):
        """Returns developer-friendly representation."""
        return f"Sale(id={self.sale_id}, product='{self.product.name}', qty={self.quantity}, total={self.total_value})"
