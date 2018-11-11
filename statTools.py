"""
------------------------------------------------------------------------------------------------------------------------
Name: statTools.py
Purpose:
    Collection of functions calculating the central tendencies and spread of a set of numerical data
    - mean, median, mode - range, upper quartile, lower quartile, variance, standard deviation

Author: Lee.K, Zhang.C

Created: 2018/11/11
------------------------------------------------------------------------------------------------------------------------
"""


def mean(data):
    """
    Returns the average of the integers in the list

    :param data: list of integers
    :return: Float rounded up to four decimals the average value of the data. None if no data.
    """
    # raise error if input is not a list
    if type(data) != list: raise TypeError("input must be a list")
    num = 0
    # return none is empty list
    if len(data) == 0:
        return None
    # return the sum of the data divided by the number of data points
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
    # raise error if input is not a list
    if type(data) != list: raise TypeError("input must be a list")
    # return none is empty list
    if len(data) == 0:
        return None
    # sort data ascending
    sorted_data = sorted(data)
    # returns middle number is odd number of data points- otherwise the mean of the middle 2 data points
    if len(data) % 2 != 0:
        return sorted_data[len(data) // 2]
    else:
        return (sorted_data[len(data) // 2] + (sorted_data[(len(data) // 2) - 1])) / 2


def mode(data):
    """
    Returns the number that appears the most in the list.

    :param data: list of integers
    :return: list of integer(s) with the most frequency in the list. None if no data.
    """
    # raise error if input is not a list
    if type(data) != list: raise TypeError("input must be a list")
    # return none if empty list
    if len(data) == 0:
        return None
    count = {}
    highest = 0
    # adds every item occurrence to a dict mapping to the number of times the item appears
    # keep track of greatest occurrence
    for item in data:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
        if count[item] > highest:
            highest = count[item]
    # finds all values that have the same number of occurrences as the greatest number of occurrences
    out = [unique for unique in count if count[unique] == highest]
    # returns single value if only 1 mode- list of values if multiple
    return sorted(out)


def rng(data):
    """
    returns the difference between the greatest value and the smallest value in the data
    :param data: list of integers
    :return: the difference between the biggest and smallest number in the list
    """
    # raise error if input is not a list
    if type(data) != list: raise TypeError("input must be a list")
    # return none is empty list
    if len(data) == 0:
        return None
    # find the largest and smallest item in the list
    big, small = data[0], data[0]
    for item in data[1:]:
        if item < small:
            small = item
        if item > big:
            big = item
    # returns the difference between the biggest and smallest value
    return round(big - small, 4)


def lower_quartile(input_list):
    """
    Returns the median of the lower half of a list of integers not inclusive of the median of the whole list
    list must be at least 4 integers long. ignores non-numerical entries

    :param input_list: list of Integers
    :return: float rounded to 4 decimal the lower quartile of the data. None if no lower quartile
    """
    # raise error if input is not a list
    if type(input_list) != list: raise TypeError("input must be a list")
    # filter out non integers or floats
    data = [value for value in input_list if type(value) == int or type(value) == float]
    length = len(data)
    # return none if list is less than 4 numbers long
    if length < 4: return None
    # sort the data ascending
    data.sort()
    # return the lower quartile
    # if length mod 4 is 2 or 3 there is odd # of items in each half- returns the middle of the half
    # if length mod 4 is 0 or 1 there is even # of items in each half- returns the mean of the middle 2 nums in the half
    return round(data[length // 4] if length % 4 in [2, 3] else (data[length // 4] + data[length // 4 - 1]) / 2, 4)


def upper_quartile(input_list):
    """
    Returns the median of the upper half of a list of Integers not inclusive of the median of the whole list
    list must be at least 4 integers long. ignores non-numerical entries

    :param input_list: list of Integers
    :return: float rounded to 4 decimal the upper quartile of the data. None if no upper quartile
    """
    # raise error if input is not a list
    if type(input_list) != list: raise TypeError("input must be a list")
    # filter out non integers or floats
    data = [value for value in input_list if type(value) == int or type(value) == float]
    length = len(data)
    # return none if list is less than 4 numbers long
    if length < 4: return None
    # sort the data ascending
    data.sort()
    # return the upper quartile
    # if length mod 4 is 2 or 3 there is odd # of items in each half- returns the middle of the half
    # if length mod 4 is 0 or 1 there is even # of items in each half- returns the mean of the middle 2 nums in the half
    return round(data[-length // 4]if length % 4 in [2, 3] else(data[-(length // 4)] + data[-(length // 4) - 1]) / 2, 4)


def variance(input_list, sample=False):
    """
    Returns the variance of a list of Integers ignoring non-numerical entries
    Method of calculation is dependent on whether the data is from a population
    Assumes not sample by default

    :param input_list: list of Integers
    :param sample: Boolean if the data is from a sample
    :return: Float rounded to 4 decimal places variance of the data. None if no data
    """
    # raise exception if input is not list
    if type(input_list) != list: raise TypeError("input must be a list")
    # return none if list is empty
    if len(input_list) == 0: return None
    # filter out non integers or floats

    data = [value for value in input_list if type(value) == int or type(value) == float]
    # return variance: mew = μ = mean
    mew = sum(data) / len(data)
    # take all items subtract the mean then squared- summed up- then divide sum by number of items (-1 if sample)
    return round(sum([(item - mew) ** 2 for item in data]) / (len(data) + (-1 if sample else 0)), 4)


def standard_dev(input_list, sample=False):
    """
    Returns the standard deviation of a list of Integers ignoring non-numerical entries
    Method of calculation is dependent on whether the data is from a population
    Assumes not sample by default

    :param input_list: list of Integers
    :param sample: Boolean if the data is from a sample
    :return: Float rounded to 4 decimal places variance of the data. None if no data
    """
    # raise error if input is not list
    if type(input_list) != list: raise TypeError("input must be a list")
    # return none if list is empty
    if len(input_list) == 0: return None
    # filter out non integers or floats
    data = [value for value in input_list if type(value) == int or type(value) == float]
    # returns the standard deviation: mew = μ = mean
    mew = sum(data) / len(data)
    # take all items subtract the mean then squared- summed up then divided by length (-1 if sample) then square rooted
    return round((sum([(item - mew) ** 2 for item in data]) / (len(data) + (-1 if sample else 0))) ** 0.5, 4)
