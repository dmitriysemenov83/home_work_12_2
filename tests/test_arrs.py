from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([1, 2, 3], 1) == 2
    assert arrs.get([1, 2, 3], -1) is None
    assert arrs.get([1, 2, 3], -1, 'default') == 'default'


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4, 5], 10, 12) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, 10) == [3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], 3, 1) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, 2) == []
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], -6, 3) == [1, 2, 3]