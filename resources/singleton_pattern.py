class SingletonMeta(type):
    """A metaclass that creates a Singleton base type when called."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    """Example Singleton class, e.g., a Logger."""
    def __init__(self):
        self.logs = []

    def log(self, message):
        """Log a message to the internal list."""
        self.logs.append(message)

    def get_logs(self):
        """Retrieve all logged messages."""
        return self.logs

    def clear(self):
        """Clear all logged messages."""
        self.logs.clear()
