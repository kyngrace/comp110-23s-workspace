"""Example function for unit tests"""

def oldsum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    # while loop
    sum_total: float = 0.0
    idx: int = 0
    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    return sum_total

def forsum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    # for...in loop
    sum_total: float = 0.0
    for elem in xs:
        sum_total += elem
    return sum_total

def rangesum(xs: list[float]) -> float:
    """return sum of all elements in xs"""
    # for...in...range loop
    sum_total: float = 0.0
    for idx in range(len(xs)):
        sum_total += xs[idx]
    return sum_total