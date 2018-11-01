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

def test_lower_quart():0

def test_upper_quart():0


def test_variance():
    assert(variance([0]) == 0)
    assert(variance([16, 20, 3, 22, 24, 8]) == 57.9167)
    assert(variance([]) == 0)
    assert(variance([6]) == 0)
    assert(variance([-34, -102, -82, 172, 140, -80, 167, -19, 6, 99, 132, -154, -200, 139, 53, 198, 173, -66, 87, -15, 1, 143, 83, -106, 167, -81, -1, -140, 47, -141, 42, -75, -41, 9, 123, 75, 9, 125, -173, 71, -107, 69, -184, 103, 162, -53, -170, 161, 51, -180]
) == 13281.6564)


def test_standard_dev():0
