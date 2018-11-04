def mean(data):
    num = 0
    if len(data) == 0:
        return 0
    else:
        for a in data:
            num += a
    return round(num / len(data), 4)

def median():0

def mode():0

def rng():0


def lower_quartile(data):
    """
    Returns the lower quartile of a list of integers

    :param data: list of Integers
    :return: float rounded to 4 decimal the lower quartile of the data. None if no lower quartile
    """
    length = len(data)
    if length < 4:
        return None
    list.sort(data)
    if length % 4 in [2, 3]:
        raw_answer = data[length // 4]
    else:
        raw_answer = (data[length // 4] + data[length // 4 - 1]) / 2
    return round(raw_answer, 4)


def upper_quartile(data):
    """
    Returns the upper quartile of a list of integers

    :param data: list of Integers
    :return: float rounded to 4 decimal the upper quartile of the data. None if no upper quartile
    """
    length = len(data)
    if length < 4:
        return None
    list.sort(data)
    if length % 4 in [2, 3]:
        raw_answer = data[-length // 4]
    else:
        raw_answer = (data[-(length // 4)] + data[-(length // 4) - 1]) / 2
    return round(raw_answer, 4)


def variance(data):
    mew = sum(data) / len(data)
    return round(sum([(item - mew) ** 2 for item in data]) / len(data), 4)


def standard_dev():0