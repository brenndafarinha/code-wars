def is_prime(number):
    if number <= 3:
        return True
    if number > 3:
        for n in range(3, number):
            if number % n == 0:
                return False
        return True


def divisors(integer):
    # codewars solution return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)

    if is_prime(integer):
        return "{} is prime".format(integer)
    else:
        divisors_list = []
        for n in range(2, integer):
            if integer % n == 0:
                divisors_list.append(n)
        return divisors_list


print(divisors(25))
print(divisors(12))
print(divisors(11))
