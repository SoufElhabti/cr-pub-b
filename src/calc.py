def divide(a, b):
    return a / b


def average(items):
    total = 0
    for i in range(len(items)):
        total += items[i]
    return total / len(items)


def parse_port(s):
    return int(s)
