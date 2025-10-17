"""
Inventory Manager
-----------------
Handles all product-related operations including CRUD operations and search/filter.
"""

from product import Product
from exceptions import (
    ProductAlreadyExistsError, 
    ProductNotFoundError,
    InvalidProductIdError,
    InvalidPriceError,
    InvalidStockError,
    InvalidProductDataError
)


class InventoryManager:
    """Manages the product inventory with CRUD and search operations."""
    
    def __init__(self):
        """Initialize inventory with empty product dictionary."""
        self.products = {}

    def add_product(self, product_id, name, price, stock):
        """
        Adds a new product to inventory.
        
        Args:
            product_id (int): Unique positive integer identifier
            name (str): Product name
            price (float): Product price
            stock (int): Initial stock quantity
            
        Raises:
            ProductAlreadyExistsError: If product ID already exists
            InvalidProductIdError: If product_id is invalid
            InvalidProductDataError: If name is invalid
            InvalidPriceError: If price is invalid
            InvalidStockError: If stock is invalid
        """
        if not isinstance(product_id, int) or product_id <= 0:
            raise InvalidProductIdError(f"Product ID must be a positive integer. Received: {product_id}")
        
        if product_id in self.products:
            raise ProductAlreadyExistsError(f"Product ID {product_id} already exists.")
        
        if not name or not name.strip():
            raise InvalidProductDataError("Product name cannot be empty.")
        
        if not isinstance(price, (int, float)) or price <= 0:
            raise InvalidPriceError(f"Product price must be a positive number. Received: {price}")
        
        if not isinstance(stock, int) or stock < 0:
            raise InvalidStockError(f"Product stock must be a non-negative integer. Received: {stock}")
        
        self.products[product_id] = Product(product_id, name, price, stock)

    def update_product(self, product_id, name=None, price=None, stock=None):
        """
        Updates product details. Only non-None parameters are updated.
        
        Args:
            product_id (int): ID of product to update
            name (str, optional): New product name
            price (float, optional): New product price
            stock (int, optional): New stock quantity
            
        Raises:
            ProductNotFoundError: If product ID doesn't exist
            InvalidProductDataError: If name is invalid
            InvalidPriceError: If price is invalid
            InvalidStockError: If stock is invalid
        """
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
        
        if name is not None and (not name or not name.strip()):
            raise InvalidProductDataError("Product name cannot be empty.")
        
        if price is not None and (not isinstance(price, (int, float)) or price <= 0):
            raise InvalidPriceError(f"Product price must be a positive number. Received: {price}")
        
        if stock is not None and (not isinstance(stock, int) or stock < 0):
            raise InvalidStockError(f"Product stock must be a non-negative integer. Received: {stock}")
        
        product = self.products[product_id]
        if name is not None:
            product.name = name.strip()
        if price is not None:
            product.price = price
        if stock is not None:
            product.stock = stock

    def remove_product(self, product_id):
        """
        Removes product from inventory.
        
        Args:
            product_id (int): ID of product to remove
            
        Raises:
            ProductNotFoundError: If product ID doesn't exist
        """
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
        del self.products[product_id]

    def list_products(self):
        """Prints all products in inventory."""
        if not self.products:
            print("No products in inventory.")
            return
        print(f"\nTotal Products: {len(self.products)}")
        for product in sorted(self.products.values(), key=lambda p: p.product_id):
            print(product)

    def get_product(self, product_id):
        """
        Returns a product object by ID.
        
        Args:
            product_id (int): ID of product to retrieve
            
        Returns:
            Product: The requested product
            
        Raises:
            ProductNotFoundError: If product ID doesn't exist
        """
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
        return self.products[product_id]
    
    def search_products(self, search_term):
        """
        Searches products by name or ID (partial match for name).
        
        Args:
            search_term (str or int): Search term to match
            
        Returns:
            list[Product]: List of matching products
        """
        search_term = str(search_term).lower().strip()
        results = []
        
        # Search by ID if search term is numeric
        if search_term.isdigit():
            product_id = int(search_term)
            if product_id in self.products:
                return [self.products[product_id]]
        
        # Search by name (partial match)
        results = [
            product for product in self.products.values()
            if search_term in product.name.lower()
        ]
        
        return results
    
    def filter_by_price_range(self, min_price=None, max_price=None):
        """
        Filters products by price range.
        
        Args:
            min_price (float, optional): Minimum price (inclusive)
            max_price (float, optional): Maximum price (inclusive)
            
        Returns:
            list[Product]: Products within specified price range
        """
        return [
            product for product in self.products.values()
            if (min_price is None or product.price >= min_price) and
               (max_price is None or product.price <= max_price)
        ]
    
    def filter_by_stock_level(self, threshold=10, low_stock=True):
        """
        Filters products by stock level relative to threshold.
        
        Args:
            threshold (int): Stock level threshold (default: 10)
            low_stock (bool): If True, returns products with stock <= threshold;
                            If False, returns products with stock > threshold
            
        Returns:
            list[Product]: Filtered products
        """
        if low_stock:
            return [p for p in self.products.values() if p.stock <= threshold]
        return [p for p in self.products.values() if p.stock > threshold]
    
    def get_total_inventory_value(self):
        """
        Calculates total value of all inventory.
        
        Returns:
            float: Total inventory value (sum of price * stock for all products)
        """
        return sum(product.price * product.stock for product in self.products.values())
