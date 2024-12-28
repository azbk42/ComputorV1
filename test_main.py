import pytest
from computor import find_degres

@pytest.mark.parametrize("input_string, expected", [
    ("X^2 + X^1 = X^8", 8),  # Case with the highest degree
    ("X + X^2", 2),          # Case with multiple terms
    ("2 = 2", 0),            # No X, degree is 0
    ("X = 2", 1),            # Case with a single X
    ("X", 1),                # Simple case with only X
])
def test_find_degres(input_string, expected):
    assert find_degres(input_string) == expected