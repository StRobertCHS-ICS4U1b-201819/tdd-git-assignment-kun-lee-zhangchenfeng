import pytest
from statTools import *

def test_mean_basic1():
    assert(mean([1, 2, 3, 4, 5]) == 3)

def test_mean_basic2():
    assert(mean([66, 74, 75, 78, 82, 89]) == 77.3333)

def test_mean_emptyList():
    assert(mean([]) == 0)

def test_median():0

def test_mode():0

def test_rng():0


def test_lower_quart():
    assert(lower_quartile([0]) is None)
    # parameter and return
    assert(lower_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2.5000)
    # odd number of items in list- each half has even number of items
    assert(lower_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 3)
    # odd number of items in list- each half has odd number of items
    assert(lower_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3)
    # even number of items in list- each half has odd number of items
    assert(lower_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 3.5000)
    # even number of items in list- each half has even number of items
    assert(lower_quartile([]) is None)
    # empty list
    assert(lower_quartile([1, 2, 3]) is None)
    # less than 4 items in list
    assert(lower_quartile([21, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 3.5)
    # unsorted list


def test_upper_quart():
    assert(upper_quartile([0]) is None);
    # parameter and return
    assert(upper_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 7.5)
    # odd number of items in list- each half has even number of items
    assert(upper_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 9)
    # odd number of items in list- each half has odd number of items
    assert(upper_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8)
    # even number of items in list- each half has odd number of items
    assert(upper_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 9.5)
    # even number of items in list- each half has even number of items


def test_variance():0

def test_std():0
