from pytest import fixture

from route.outliners import get_outliner_indexes


@fixture
def no_outliners():
    return [1, 5, 6, 10, 7, 2, 8, 9, 4, 5, 1]


@fixture
def outliners():
    return [1, 2, 1, 100, 2, 1, 1, 200, 1, 2]


def test_get_outliners_without_outliners(no_outliners):
    assert get_outliner_indexes(no_outliners) == []


def test_get_outliners_with_outliners(outliners):
    assert get_outliner_indexes(outliners) == [3, 7]
