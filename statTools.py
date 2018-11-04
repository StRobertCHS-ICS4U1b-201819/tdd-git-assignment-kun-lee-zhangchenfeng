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


def lower_quart(data):
    """
    Returns the lower quartile of a list of integers

    :param data: list of Integers
    :return: float rounded to 4 decimal the lower quartile of the data. None if no lower quartile
    """
    length = len(data)
    if length < 4:
        return None
    list.sort(data)
    if length % 4 == 3 or length % 4 == 2:
        raw_answer = data[length // 4]
    else:
        raw_answer = (data[length // 4] + data[length // 4 - 1]) / 2
    return round(raw_answer, 4)


def upper_quart(data):
    """
    Returns the upper quartile of a list of integers

    :param data: list of Integers
    :return: float rounded to 4 decimal the upper quartile of the data. None if no upper quartile
    """
    length = len(data)
    if length < 4:
        return None
    list.sort(data)
    if length % 4 == 3 or length % 4 == 2:
        raw_answer = data[-length // 4]
    else:
        raw_answer = (data[-(length // 4)] + data[-(length // 4) - 1]) / 2
    return round(raw_answer, 4)


def variance(data, sample=False):
    """
    Returns the variance of a list of Integers
    Method of calculation is dependent on whether the data is from a population
    Assumes not sample by default

    :param data: list of Integers
    :param sample: Boolean if the data is from a sample
    :return: Float rounded to 4 decimal places variance of the data. None if no data
    """
    if len(data) == 0:
        return None
    if len(data) == 1:
        return 0;
    if sample:
        denominator = len(data) - 1
    else:
        denominator = len(data)
    mean = sum(data) / len(data)
    return round(sum([(item - mean) ** 2 for item in data]) / denominator, 4)


def standard_dev(data, sample=False):
    """
    Returns the standard deviation of a list of Integers
    Method of calculation is dependent on whether the data is from a population
    Assumes not sample by default

    :param data: list of Integers
    :param sample: Boolean if the data is from a sample
    :return: Float rounded to 4 decimal places variance of the data. None if no data
    """
    from math import sqrt
    if len(data) == 0:
        return None
    if len(data) == 1:
        return 0
    if sample:
        denominator = len(data) - 1
    else:
        denominator = len(data)
    mean = sum(data) / len(data)
    return round(sqrt(sum([(item - mean) ** 2 for item in data]) / denominator), 4)
