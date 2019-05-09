def find_outlier(integers):
    even = [n for n in integers if n % 2 == 0]
    odd = [n for n in integers if n % 2 != 0]

    return odd[0] if len(even) > len(odd) else even[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))