import pytest
from resources.factory_pattern import Creator, ConcreteProductA, \
    ConcreteProductB


def test_create_product_a():
    creator = Creator()
    product = creator.factory_method("A")
    assert isinstance(product, ConcreteProductA)
    assert product.operation() == "Result of Product A"


def test_create_product_b():
    creator = Creator()
    product = creator.factory_method("B")
    assert isinstance(product, ConcreteProductB)
    assert product.operation() == "Result of Product B"


def test_creator_some_operation_a():
    creator = Creator()
    result = creator.some_operation("A")
    assert "Worked with Result of Product A" in result


def test_creator_some_operation_b():
    creator = Creator()
    result = creator.some_operation("B")
    assert "Worked with Result of Product B" in result


def test_unknown_product_type():
    creator = Creator()
    with pytest.raises(ValueError):
        creator.factory_method("C")
