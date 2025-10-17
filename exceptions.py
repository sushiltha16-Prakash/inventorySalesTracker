"""
Custom Exceptions
-----------------
Handles business rule errors.
"""

# Product-related exceptions
class ProductAlreadyExistsError(Exception):
    """Raised when trying to add a product with an ID that already exists."""
    pass

class ProductNotFoundError(Exception):
    """Raised when a product ID is not found in the inventory."""
    pass

class InvalidProductDataError(Exception):
    """Raised when product data is invalid (e.g., negative price, empty name)."""
    pass

# Sales-related exceptions
class OutOfStockError(Exception):
    """Raised when trying to sell more stock than available."""
    pass

class InvalidQuantityError(Exception):
    """Raised when sale quantity is invalid (e.g., negative or zero)."""
    pass

class SaleNotFoundError(Exception):
    """Raised when a sale ID is not found."""
    pass

# Validation exceptions
class InvalidPriceError(Exception):
    """Raised when product price is invalid (e.g., negative or zero)."""
    pass

class InvalidStockError(Exception):
    """Raised when stock value is invalid (e.g., negative)."""
    pass

class InvalidProductIdError(Exception):
    """Raised when product ID is invalid (e.g., negative)."""
    pass
