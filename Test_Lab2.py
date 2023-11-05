import main
import pytest

def test_find_min_max():
    assert main.find_min_max([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 9]
    assert main.find_min_max([7]) == [7, 7]
    # Handle the case when the input list is empty
    assert main.find_min_max([]) == [None, None]

def test_calc_average_temperature():
    num_list = [1, 2, 3, 4, 5]
    assert main.calc_average_temperature(num_list) == 3.0

def test_calc_median_temperature():
    assert main.calc_median_temperature([1, 2, 3, 4, 5]) == 3
    assert main.calc_median_temperature([1, 2, 3, 4]) == 2.5

if __name__ == '__main__':
    pytest.main()



