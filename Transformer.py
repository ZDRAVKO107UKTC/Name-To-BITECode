def name_to_codes(name):
    binary_codes = []
    decimal_codes = []

    for char in name:
        decimal_value = ord(char)
        binary_value = format(decimal_value, '08b')
        decimal_codes.append(decimal_value)
        binary_codes.append(binary_value)

    return decimal_codes, binary_codes

name = input("Enter name: ")
decimals, binaries = name_to_codes(name)

print("\nCharacter  Decimal   Binary")
print("-" * 30)
for char, d, b in zip(name, decimals, binaries):
    print(f"{char:10} {d:<9} {b}")
