import pytest


class NotInRange(Exception):
    def __init__(self, message = "Specified value is not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 2
    b = 2
    assert a == b


def test_exception():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
