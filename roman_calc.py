
def roman_to_int(roman_string: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M': 1000}
    count = 0
    for i in range(0, len(roman_string) - 1):
        if roman_map[roman_string[i + 1]] > roman_map[roman_string[i]]:
            count -= roman_map[roman_string[i]]
        else:
            count += roman_map[roman_string[i]]
    count += roman_map[roman_string[-1]]

    return count

def int_to_roman(number: int) -> str:
    roman_int_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    roman_arr = list(roman_int_map.keys())[::-1]
    return_str = ''
    for i in roman_arr:
        while number >= i:
            number -= i
            return_str += roman_int_map[i]
    return return_str