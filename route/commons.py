from itertools import groupby
from operator import itemgetter


def filter_consecutive_duplicates(iterable):
    """Filters consecutive duplicates from an iterable

    :param iterable: in iterable object
    :returns: the iterable without the consecutive duplicates
    :rtype: map

    """

    return map(itemgetter(0), groupby(iterable))
