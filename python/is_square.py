import math


def is_square(n):
    # return n > -1 and math.sqrt(n) % 1 == 0
    if n < 0:
        return False
    else:
        return True if n == 0 or n % math.sqrt(n) == 0 else False


print(is_square(-1))
