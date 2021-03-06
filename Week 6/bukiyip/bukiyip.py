def bukiyip_to_decimal(a):
    num = str(a)
    index = 0
    decimal = 0
    for i in range(len(num) - 1, -1, -1):
        decimal += int(num[i]) * 3 ** (index)
        index += 1
    return decimal


def decimal_to_bukiyip(a):
    bukiyip = ''
    while a > 0:
        bukiyip += str(a % 3)
        a = a // 3
    return int(bukiyip[::-1])


def test_num():
    for n in range(1, 13):
        x = decimal_to_bukiyip(n)
        print(str(x))


def bukiyip_add(a, b):
    a_10 = bukiyip_to_decimal(a)
    b_10 = bukiyip_to_decimal(b)
    sum_10 = a_10 + b_10
    sum = decimal_to_bukiyip(sum_10)
    return sum


def bukiyip_multiply(a, b):
    a_10 = bukiyip_to_decimal(a)
    b_10 = bukiyip_to_decimal(b)
    product_10 = a_10 * b_10
    product = decimal_to_bukiyip(product_10)
    return product