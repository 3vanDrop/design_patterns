
# Design Patterns in Python

A collection of five fundamental object-oriented design patterns implemented in Python.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Design Patterns](#design-patterns)
   - [Singleton Pattern](#singleton-pattern)
   - [Observer Pattern](#observer-pattern)
   - [Factory Method Pattern](#factory-method-pattern)
   - [Strategy Pattern](#strategy-pattern)
   - [Decorator Pattern](#decorator-pattern)
3. [Setup and Usage](#setup-and-usage)
   - [Generate Code](#generate-code)
   - [Generate README](#generate-readme)
   - [Running Tests](#running-tests)
4. [Requirements](#requirements)
5. [Contributing](#contributing)
6. [License](#license)

## Project Structure

```text
.
├── resources
│   ├── singleton_pattern.py
│   ├── observer_pattern.py
│   ├── factory_pattern.py
│   ├── strategy_pattern.py
│   └── decorator_pattern.py
├── tests
│   ├── test_singleton_pattern.py
│   ├── test_observer_pattern.py
│   ├── test_factory_pattern.py
│   ├── test_strategy_pattern.py
│   └── test_decorator_pattern.py
├── main.py
└── readme.py
```

## Design Patterns

### Singleton Pattern
Ensures a class has only one instance and provides a global point of access.
- File: 'resources/singleton_pattern.py'

Example usage:
```python
from resources.singleton_pattern import Logger

logger1 = Logger()
logger2 = Logger()
assert logger1 is logger2
logger1.log("Hello")
print(logger2.get_logs())  # ["Hello"]
```

### Observer Pattern
Defines a one-to-many dependency so that when one object changes state, all its dependents are notified.
- File: 'resources/observer_pattern.py'

Example usage:
```python
from resources.observer_pattern import NewsPublisher, Subscriber

publisher = NewsPublisher()
alice = Subscriber("Alice")
publisher.register(alice)
publisher.publish("Breaking News!")
print(alice.get_news())  # [("Alice", "Breaking News!")]
```

### Factory Method Pattern
Defines an interface for creating an object, but lets subclasses decide which concrete class to instantiate.
- File: 'resources/factory_pattern.py'

Example usage:
```python
from resources.factory_pattern import Creator

creator = Creator()
product_a = creator.factory_method("A")
print(product_a.operation())  # Result of Product A
```

### Strategy Pattern
Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- File: 'resources/strategy_pattern.py'

Example usage:
```python
from resources.strategy_pattern import Context, ConcreteStrategyAdd, ConcreteStrategyMultiply

context = Context(ConcreteStrategyAdd())
print(context.execute_strategy([1, 2, 3]))  # 6
context.set_strategy(ConcreteStrategyMultiply())
print(context.execute_strategy([2, 3, 4]))  # 24
```

### Decorator Pattern
Attaches additional responsibilities to an object dynamically.
- File: 'resources/decorator_pattern.py'

Example usage:
```python
from resources.decorator_pattern import ConcreteComponent, ConcreteDecoratorA, ConcreteDecoratorB

component = ConcreteComponent()
decorated = ConcreteDecoratorB(ConcreteDecoratorA(component))
print(decorated.operation())  # DecoratorB(DecoratorA(ConcreteComponent))
```

## Setup and Usage

### Generate Code
Run the following to generate todos los m�dulos y tests:
```bash
python3 main.py
```

### Running Tests
Ejecuta las pruebas con pytest:
```bash
pytest -q
```

## Requirements
- Python 3.6+
- pytest

## Contributing
Contributions are welcome! Open issues or submit pull requests.
