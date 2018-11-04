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


def lower_quartile(data):
    length = len(data)
    if length<4:return None
    if length%4in[2, 3]:raw_output = data[length//4]
    else:raw_output = (data[length//4] + data[length//4-1])/2
    return round(raw_output, 4)


def upper_quartile():0


def variance():0


def standard_dev():0