class Component:
    """Base Component interface."""
    def operation(self):
        raise NotImplementedError


class ConcreteComponent(Component):
    """Concrete component providing default behavior."""
    def operation(self):
        return "ConcreteComponent"


class Decorator(Component):
    """Base Decorator maintaining a reference to a component."""
    def __init__(self, component: Component):
        self._component = component

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    """Concrete Decorator A adds behavior before/after widget."""
    def operation(self):
        return f"DecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    """Concrete Decorator B adds additional behavior."""
    def operation(self):
        return f"DecoratorB({self._component.operation()})"
