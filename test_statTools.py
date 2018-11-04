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
    assert(lower_quart([0]) == 0);
    # parameter and return
    assert(lower_quart([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2.5000)
    # odd number of items in list- each half has even number of items
    assert(lower_quart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 3)
    # odd number of items in list- each half has odd number of items
    assert(lower_quart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 3)
    # even number of items in list- each half has odd number of items
    assert(lower_quart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 3.5000)
    # even number of items in list- each half has even number of items
    assert(lower_quart([]) == 0)
    # empty list
    assert(lower_quart([1, 2, 3]) == 0)
    # less than 4 items in list
    assert(lower_quart([21, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 3.5)
    # unsorted list


def test_upper_quart():
    assert(upper_quart([0]) == 0);
    # parameter and return
    assert(upper_quart([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 7.5)
    # odd number of items in list- each half has even number of items
    assert(upper_quart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 9)
    # odd number of items in list- each half has odd number of items
    assert(upper_quart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8)
    # even number of items in list- each half has odd number of items
    assert(upper_quart([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 9.5)
    # even number of items in list- each half has even number of items
    assert(upper_quart([]) == 0)
    # empty list
    assert(upper_quart([1, 2, 3]) == 0)
    # less than 4 items in list
    assert(upper_quart([21, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1]) == 9.5)
    # unsorted list


def test_variance():
    assert(variance([0], False) == 0)
    # parameter and returns
    assert(variance([16, 20, 3, 22, 24, 8], False) == 57.9167)
    assert(variance([], True) == 0)
    # empty list
    assert(variance([6], False) == 0)
    # 1 value
    assert(variance([-34, -102, -82, 172, 140, -80, 167, -19, 6, 99, 132, -154, -200, 139, 53, 198, 173, -66, 87, -15, 1, 143, 83, -106, 167, -81, -1, -140, 47, -141, 42, -75, -41, 9, 123, 75, 9, 125, -173, 71, -107, 69, -184, 103, 162, -53, -170, 161, 51, -180], True) == 13552.7106)
    # variance of sample
    assert(variance([-34, -102, -82, 172, 140, -80, 167, -19, 6, 99, 132, -154, -200, 139, 53, 198, 173, -66, 87, -15, 1, 143, 83, -106, 167, -81, -1, -140, 47, -141, 42, -75, -41, 9, 123, 75, 9, 125, -173, 71, -107, 69, -184, 103, 162, -53, -170, 161, 51, -180], False) == 13281.6564)
    # variance of population


def test_standard_dev():
    assert(standard_dev([0]) == 0)
    # parameter and return
    assert(standard_dev([-39, -4, -62, -27, -1, -29, -33, -105, -150, -147, 50, 59, 34, 42, -88, -7, -40, -23, 114, 102], False) == 70.4032)
    # std of population
    assert(standard_dev([-39, -4, -62, -27, -1, -29, -33, -105, -150, -147, 50, 59, 34, 42, -88, -7, -40, -23, 114, 102], True) == 72.2322)
    # std of sample
    assert(standard_dev([4], False) == 0)
    # 1 value list
    assert(standard_dev([], True) == 0)
    # empty list

