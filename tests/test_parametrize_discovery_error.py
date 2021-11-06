import pytest


@pytest.mark.parametrize("id", [("("), (")"), ("["), ("]")])
def test_parametrize(id):
    pass
