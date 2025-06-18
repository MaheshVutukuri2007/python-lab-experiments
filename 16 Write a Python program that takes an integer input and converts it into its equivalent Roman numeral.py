def int_to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    
    for i in range(len(val)):
        while num >= val[i]:
            roman += syms[i]
            num -= val[i]
    return roman

# Input
number = int(input("Enter an integer (1 to 3999): "))

# Validation and conversion
if 1 <= number <= 3999:
    roman_numeral = int_to_roman(number)
    print(f"Roman numeral: {roman_numeral}")
else:
    print("Please enter a number between 1 and 3999.")
