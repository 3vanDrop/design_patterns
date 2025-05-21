import pytest
from resources.strategy_pattern import Context, ConcreteStrategyAdd, ConcreteStrategyMultiply

def test_add_strategy():
    context = Context(ConcreteStrategyAdd())
    data = [1, 2, 3]
    assert context.execute_strategy(data) == 6

def test_multiply_strategy():
    context = Context(ConcreteStrategyMultiply())
    data = [2, 3, 4]
    assert context.execute_strategy(data) == 24

def test_change_strategy():
    context = Context(ConcreteStrategyAdd())
    data = [5, 5]
    assert context.execute_strategy(data) == 10
    context.set_strategy(ConcreteStrategyMultiply())
    assert context.execute_strategy(data) == 25

def test_empty_data_add():
    context = Context(ConcreteStrategyAdd())
    assert context.execute_strategy([]) == 0

def test_empty_data_multiply():
    context = Context(ConcreteStrategyMultiply())
    assert context.execute_strategy([]) == 1
