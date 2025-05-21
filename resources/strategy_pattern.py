class Strategy:
    """Strategy interface declares algorithm method."""
    def do_algorithm(self, data):
        raise NotImplementedError


class ConcreteStrategyAdd(Strategy):
    """Concrete Strategy for addition."""
    def do_algorithm(self, data):
        return sum(data)


class ConcreteStrategyMultiply(Strategy):
    """Concrete Strategy for multiplication."""
    def do_algorithm(self, data):
        result = 1
        for num in data:
            result *= num
        return result


class Context:
    """Context maintains a reference to a Strategy instance."""
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        """Change the strategy at runtime."""
        self._strategy = strategy

    def execute_strategy(self, data):
        """Execute the algorithm using the strategy."""
        return self._strategy.do_algorithm(data)
