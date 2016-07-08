from pytest import fixture

from route.commons import filter_consecutive_duplicates


@fixture
def no_duplicates():
    return [(1, 1), (1, 2), (1, 3)]


@fixture
def more_duplicates():
    return [(1, 1), (1, 1), (1, 1), (1, 3)]


@fixture
def no_consecutve_duplicates():
    return [(1, 1), (1, 3), (1, 1)]


def test_filter_consecutive_duplicates_without_duplicates(no_duplicates):
    assert list(filter_consecutive_duplicates(no_duplicates)) == no_duplicates


def test_filter_consecutive_duplicates_with_more_duplicates(more_duplicates):
    assert list(filter_consecutive_duplicates(more_duplicates)) == [(1, 1), (1, 3)]


def test_filter_consecutive_duplicates_with_no_consecutive_duplicates(no_consecutve_duplicates):
    assert list(filter_consecutive_duplicates(no_consecutve_duplicates)) == no_consecutve_duplicates
