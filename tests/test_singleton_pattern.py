from resources.singleton_pattern import Logger


def setup_function():
    # Ensure the singleton is in a clean state before each test
    Logger().clear()


def test_singleton_same_instance():
    logger1 = Logger()
    logger2 = Logger()
    assert logger1 is logger2


def test_singleton_logging():
    logger = Logger()
    logger.log("first")
    assert logger.get_logs() == ["first"]


def test_singleton_logs_persistent():
    logger1 = Logger()
    logger1.log("second")
    logger2 = Logger()
    assert logger2.get_logs() == ["second"]


def test_singleton_multiple_messages():
    logger = Logger()
    logger.log("msg1")
    logger.log("msg2")
    assert logger.get_logs() == ["msg1", "msg2"]


def test_singleton_clear_logs():
    logger = Logger()
    logger.log("x")
    logger.clear()
    assert logger.get_logs() == []
