from resources.observer_pattern import NewsPublisher, Subscriber


def test_subscriber_receives_news():
    publisher = NewsPublisher()
    sub = Subscriber("Alice")
    publisher.register(sub)
    publisher.publish("News1")
    assert sub.get_news() == [("Alice", "News1")]


def test_unsubscribe():
    publisher = NewsPublisher()
    sub = Subscriber("Bob")
    publisher.register(sub)
    publisher.unregister(sub)
    publisher.publish("News2")
    assert sub.get_news() == []


def test_multiple_subscribers():
    publisher = NewsPublisher()
    sub1 = Subscriber("A")
    sub2 = Subscriber("B")
    publisher.register(sub1)
    publisher.register(sub2)
    publisher.publish("World")
    assert ("A", "World") in sub1.get_news()
    assert ("B", "World") in sub2.get_news()


def test_register_twice():
    publisher = NewsPublisher()
    sub = Subscriber("C")
    publisher.register(sub)
    publisher.register(sub)
    publisher.publish("X")
    # duplicated observer should get notified twice
    assert sub.get_news().count(("C", "X")) == 2


def test_sequence_of_messages():
    publisher = NewsPublisher()
    sub = Subscriber("D")
    publisher.register(sub)
    messages = ["M1", "M2", "M3"]
    for m in messages:
        publisher.publish(m)
    assert sub.get_news() == [("D", m) for m in messages]
