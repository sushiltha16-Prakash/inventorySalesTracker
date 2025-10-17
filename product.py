"""
Product Class
-------------
Represents a product in the inventory.
"""

from exceptions import InvalidPriceError, InvalidStockError, InvalidProductIdError, InvalidProductDataError


class Product:
    """Represents a single product with ID, name, price, and stock quantity."""
    
    def __init__(self, product_id, name, price, stock):
        """
        Initialize a new Product.
        
        Args:
            product_id (int): Unique positive integer identifier
            name (str): Non-empty product name
            price (float): Positive price value
            stock (int): Non-negative stock quantity
            
        Raises:
            InvalidProductIdError: If product_id is not a positive integer
            InvalidProductDataError: If name is empty or invalid
            InvalidPriceError: If price is not positive
            InvalidStockError: If stock is negative
        """
        if not isinstance(product_id, int) or product_id <= 0:
            raise InvalidProductIdError(f"Product ID must be a positive integer. Received: {product_id}")
        
        if not name or not isinstance(name, str) or not name.strip():
            raise InvalidProductDataError("Product name cannot be empty.")
        
        if not isinstance(price, (int, float)) or price <= 0:
            raise InvalidPriceError(f"Product price must be a positive number. Received: {price}")
        
        if not isinstance(stock, int) or stock < 0:
            raise InvalidStockError(f"Product stock must be a non-negative integer. Received: {stock}")
        
        self.product_id = product_id
        self.name = name.strip()
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """
        Updates stock by adding or subtracting quantity.
        
        Args:
            quantity (int): Amount to add (positive) or subtract (negative)
            
        Raises:
            InvalidStockError: If quantity is not an integer or results in negative stock
        """
        if not isinstance(quantity, int):
            raise InvalidStockError(f"Stock quantity must be an integer. Received: {quantity}")
        
        new_stock = self.stock + quantity
        if new_stock < 0:
            raise InvalidStockError(f"Cannot reduce stock below 0. Current: {self.stock}, Requested change: {quantity}")
        
        self.stock = new_stock

    def __str__(self):
        """Returns formatted product information."""
        return f"ID: {self.product_id} | Name: {self.name} | Stock: {self.stock} | Price: ${self.price:.2f}"
    
    def __repr__(self):
        """Returns developer-friendly representation."""
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price}, stock={self.stock})"
