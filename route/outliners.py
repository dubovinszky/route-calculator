from statistics import median, stdev


def get_outliner_indexes(data, tolerance=7):
    """Detects outliners in a data sequence, and returns with it' indexes.

    :param data: the data sequence (type: list)
    :param tolerance: the tolerance of the detettor function
    :returns: the indexes of the detected outliner elements
    :rtype: list

    """

    outliner_indexes = []
    median_of_data = median(data)
    stdev_of_data = stdev(data)

    d_is = [abs(d - median_of_data) / stdev_of_data for d in data]
    median_of_dis = median(d_is)

    for i, di in enumerate(d_is):
        if di > median_of_dis * tolerance:
            outliner_indexes.append(i)

    return outliner_indexes
