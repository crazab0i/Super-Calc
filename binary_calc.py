    

def int_to_binary(integer: int) -> int:
    if integer == 0:
        return 0
    binary_str = ''

    while integer > 0:
        remainder = integer % 2
        binary_str = str(remainder) + binary_str
        integer //= 2
    return int(binary_str)

def binary_to_int(binary: int) -> int:
    length = len(str(binary))
    count = 0
    position = 0
    for i in str(binary):
        position += 1
        if i == '1':
            count += 2 ** (length - position)
    return count