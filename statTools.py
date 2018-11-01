def mean(data):
    num = 0
    if len(data) == 0:
        return 0
    else:
        for a in data:
            num += a
        return round(num / len(data),4)

def median(data):
    num = 0
    sorted_Data = sorted(data)
    if len(data) == 0:
        return 0
    if (len(data)%2) != 0:
        return sorted_Data[len(data)//2]
    else:
        return (sorted_Data[len(data)//2] + (sorted_Data[(len(data)//2) -1])) /2

def mode(data):
    if len(data) == 0:
        return 0
    else:
        return max(set(data), key=data.count)
