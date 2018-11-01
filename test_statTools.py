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
    assert(variance([16, 20, 3, 22, 24, 8]) == 57.92)
    assert(variance([]) == 0)
    assert(variance([6]) == 6)


def test_standard_dev():0
