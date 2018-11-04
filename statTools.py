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

def lower_quart():0

def upper_quart():0


def variance(data, sample=False):
    """
    Returns the variance of a list of Integers
    Method of calculation is dependent on whether the data is from a population
    Assumes not sample by default

    :param data: list of Integers
    :param sample: Boolean if the data is from a sample
    :return: Float rounded to 4 decimal places variance of the data
    """
    if len(data) <= 1:
        return 0
    if sample:
        denominator = len(data) - 1
    else:
        denominator = len(data)
    mean = sum(data) / len(data)
    return round(sum([(item - mean) ** 2 for item in data]) / denominator, 4)


def standard_dev(data, sample=False):
    from math import sqrt
    if len(data) <= 1:
        return 0
    if sample:
        denominator = len(data) - 1
    else:
        denominator = len(data)
    mean = sum(data) / len(data)
    return round(sqrt(sum([(item - mean) ** 2 for item in data]) / denominator), 4)
