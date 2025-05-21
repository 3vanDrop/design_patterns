from resources.decorator_pattern import ConcreteComponent, ConcreteDecoratorA, \
    ConcreteDecoratorB


def test_base_component():
    component = ConcreteComponent()
    assert component.operation() == "ConcreteComponent"


def test_decorator_a():
    component = ConcreteComponent()
    decorator = ConcreteDecoratorA(component)
    assert decorator.operation() == "DecoratorA(ConcreteComponent)"


def test_decorator_b():
    component = ConcreteComponent()
    decorator = ConcreteDecoratorB(component)
    assert decorator.operation() == "DecoratorB(ConcreteComponent)"


def test_decorator_chain():
    component = ConcreteComponent()
    decorator_chain = ConcreteDecoratorB(ConcreteDecoratorA(component))
    assert decorator_chain.operation() == \
        "DecoratorB(DecoratorA(ConcreteComponent))"


def test_multiple_wrapping():
    component = ConcreteComponent()
    decorated = ConcreteDecoratorA(ConcreteDecoratorA(component))
    assert decorated.operation() == "DecoratorA(DecoratorA(ConcreteComponent))"
