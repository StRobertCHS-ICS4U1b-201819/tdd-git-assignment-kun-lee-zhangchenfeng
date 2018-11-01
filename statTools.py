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


def variance(data):
    if len(data) == 0:return 0
    mean = sum(data) / len(data)
    return round(sum([(item - mean) ** 2 for item in data]) / len(data), 4)


def standard_dev():0