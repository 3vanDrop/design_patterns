class Product:
    """Abstract product interface."""
    def operation(self):
        raise NotImplementedError


class ConcreteProductA(Product):
    """Implementation of Product A."""
    def operation(self):
        return "Result of Product A"


class ConcreteProductB(Product):
    """Implementation of Product B."""
    def operation(self):
        return "Result of Product B"


class Creator:
    """Creator with factory method."""
    def factory_method(self, type):
        """Create products based on type identifier."""
        if type == "A":
            return ConcreteProductA()
        elif type == "B":
            return ConcreteProductB()
        else:
            raise ValueError("Unknown product type")

    def some_operation(self, type):
        """Business logic that uses the factory method."""
        product = self.factory_method(type)
        return f"Creator: Worked with {product.operation()}"
