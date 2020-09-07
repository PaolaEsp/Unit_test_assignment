import pytest

@pytest.mark.parametrize("number, expected", [
    (5, 13), # y = 2x + 3
    (8, 19),
    (10, 23),
    ])
def test_y_value(number, expected):
    from line_fun import y_value
    result = y_value(number)
    assert result == expected
