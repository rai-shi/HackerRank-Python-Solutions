def romanToInt(s: str) -> int:
    roman_symbols = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
        "first" : 10000,
    }
    number = 0
    prev_symbol = 0
    for symbol in s:
        current_symbol = roman_symbols[symbol]
        if current_symbol > prev_symbol:
            # we add previous iteration so we need to substract 2 times
            number += current_symbol - (2*prev_symbol)
        else:
            number += current_symbol 
        prev_symbol = current_symbol
    return number
print()
print(romanToInt("MCMXCIV"))
print()
print(romanToInt("LVIII"))
print()
print(romanToInt("III"))
