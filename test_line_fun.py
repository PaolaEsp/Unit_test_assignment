import pytest

@pytest.mark.parametrize("coord1, coord2, number, expected", [
    ((1,5), (3,9), 5, 13), # y = 2x + 3
    ((1,-3), (2,-2), 8, 4),
    ((1,4), (2,8), 10, 40),
    ])
def test_y_value(coord1, coord2, number, expected):
    from line_fun import y_value
    result = y_value(coord1, coord2, number)
    assert result == expected
