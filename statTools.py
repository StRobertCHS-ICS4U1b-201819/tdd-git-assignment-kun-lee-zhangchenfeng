def mean(data):
    """
    Returns the average of the integers in the list

    :param data: list of integers
    :return: Float rounded up to four decimals the average value of the data. None if no data.
    """
    num = 0
    if len(data) == 0:
        return None
    else:
        for a in data:
            num += a
    return round(num / len(data), 4)


def median(data):
    """
    Returns the middle number of the list

    :param data: list of integers
    :return: the middle integer in the list. average of the 2 numbers if two middle integers. None if no data.
    """
    sorted_Data = sorted(data)
    num = 0
    if len(data) == 0:
        return None
    elif (len(data) % 2) != 0:
        return sorted_Data[len(data) // 2]
    else:
        return (sorted_Data[len(data) // 2] + (sorted_Data[(len(data) // 2) - 1])) / 2


def mode(data):
    """
    Returns the number that appears the most in the list.

    :param data: list of integers
    :return: the integer(s) with the most frequency in the list. None if no data.
    """
    if len(data) == 0:
        return None
    count = {}
    highest = 0
    for item in data:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
        if count[item] > highest:
            highest = count[item]
    out = []
    [out.append(unique) if count[unique] == highest else 0 for unique in count]
    if len(out) == 1:
        return out[0]
    return sorted(out)


def rng(data):
    sorted_Data = sorted(data)
    if len(data) == 0:
        return None
    else:
        return sorted_Data[len(data) -1] - sorted_Data[0]


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
