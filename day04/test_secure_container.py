from secure_container import is_six_digits, contains_adjacent_digits,\
    digit_increase_check


def test_six_digit_function_works():
    assert is_six_digits(251903)
    assert not is_six_digits(3256)


def test_contains_adjacent_works():
    assert contains_adjacent_digits(122545)
    assert not contains_adjacent_digits(412390)


def test_digits_never_decrease():
    assert digit_increase_check(122567)
    assert digit_increase_check(225434)
