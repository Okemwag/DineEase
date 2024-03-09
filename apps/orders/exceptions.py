class OrderError(Exception):
    """Base class for order-related exceptions."""
    pass

class InvalidOrderError(OrderError):
    """Exception raised for invalid orders."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InsufficientFundsError(OrderError):
    """Exception raised when there are insufficient funds to complete an order."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class OrderNotFoundError(OrderError):
    """Exception raised when an order is not found."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class OrderAlreadyPaidError(OrderError):
    """Exception raised when an order has already been paid."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class OrderAlreadyCancelledError(OrderError):
    """Exception raised when an order has already been cancelled."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class OrderAlreadyCompletedError(OrderError):
    """Exception raised when an order has already been completed."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



