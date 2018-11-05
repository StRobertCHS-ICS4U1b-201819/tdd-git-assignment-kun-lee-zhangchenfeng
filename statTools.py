def mean(data):
    num = 0
    if len(data) == 0:
        return None
    else:
        for a in data:
            num += a
    return round(num / len(data), 4)

def median(data):
    sorted_Data = sorted(data)
    num = 0
    if len(data) == 0:
        return None
    elif (len(data) % 2) != 0:
        return sorted_Data[len(data) // 2]
    else:
        return (sorted_Data[len(data) // 2] + (sorted_Data[(len(data) // 2) - 1])) / 2

def mode(data):
    if len(data) == 0:
        return None
    else:
        return max(set(data), key=data.count)

def rng():0


def lower_quartile(data):
    """
    Returns the lower quartile of a list of integers

    :param data: list of Integers
    :return: float rounded to 4 decimal the lower quartile of the data. None if no lower quartile
    """
    length = len(data)
    if length < 4:return None
    list.sort(data)
    return round(data[length // 4] if length % 4 in [2, 3] else (data[length // 4] + data[length // 4 - 1]) / 2, 4)


def upper_quartile(data):
    """
    Returns the upper quartile of a list of integers

    :param data: list of Integers
    :return: float rounded to 4 decimal the upper quartile of the data. None if no upper quartile
    """
    length = len(data)
    if length < 4: return None
    list.sort(data)
    return round(data[-length // 4]if length % 4 in [2, 3] else(data[-(length // 4)] + data[-(length // 4) - 1]) / 2, 4)


def variance(data, sample=False):
    """
    Returns the variance of a list of Integers
    Method of calculation is dependent on whether the data is from a population
    Assumes not sample by default

    :param data: list of Integers
    :param sample: Boolean if the data is from a sample
    :return: Float rounded to 4 decimal places variance of the data. None if no data
    """
    if len(data) == 0: return None
    mew = sum(data) / len(data)
    return round(sum([(item - mew) ** 2 for item in data]) / (len(data) + (-1 if sample else 0)), 4)


def standard_dev(data, sample=False):
    """
    Returns the standard deviation of a list of Integers
    Method of calculation is dependent on whether the data is from a population
    Assumes not sample by default

    :param data: list of Integers
    :param sample: Boolean if the data is from a sample
    :return: Float rounded to 4 decimal places variance of the data. None if no data
    """
    if len(data) == 0: return None
    from math import sqrt
    mew = sum(data) / len(data)
    return round(sqrt(sum([(item - mew) ** 2 for item in data]) / (len(data) + (-1 if sample else 0))), 4)
