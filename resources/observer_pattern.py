class Subject:
    """Manages observers and notifications."""
    def __init__(self):
        self._observers = []

    def register(self, observer):
        """Attach an observer."""
        self._observers.append(observer)

    def unregister(self, observer):
        """Detach an observer."""
        self._observers.remove(observer)

    def notify(self, message):
        """Notify all observers with a message."""
        for observer in self._observers:
            observer.update(message)


class Observer:
    """Observer interface declares update method."""
    def update(self, message):
        raise NotImplementedError


class NewsPublisher(Subject):
    """Concrete Subject that publishes news."""
    def publish(self, news):
        """Publish news to all subscribers."""
        self.notify(news)


class Subscriber(Observer):
    """Concrete Observer that receives news."""
    def __init__(self, name):
        self.name = name
        self.news = []

    def update(self, message):
        """Receive update from publisher."""
        self.news.append((self.name, message))

    def get_news(self):
        """Retrieve received news."""
        return self.news
