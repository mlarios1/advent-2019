from program_alarm import intcode_as_array, perform_list_operation


def test_array_has_ten_elements():
    intcode_list = intcode_as_array()
    assert len(intcode_list) > 9


def test_one_exists_at_position_four():
    intcode_list = intcode_as_array()
    assert intcode_list[4] == 1


def test_three_exists_at_position_seven():
    intcode_list = intcode_as_array()
    assert intcode_list[7] == 3


def test_list_operation_returns_int():
    assert isinstance(perform_list_operation(), int)
