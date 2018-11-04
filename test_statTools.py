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
    assert(lower_quartile([0]) == 0)

def test_upper_quart():0

def test_variance():0

def test_std():0


