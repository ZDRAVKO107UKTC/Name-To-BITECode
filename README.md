# Name to Binary and Decimal Converter

This project is a simple Python script that converts a given name (string) into its **decimal ASCII/Unicode codes** and their **8-bit binary representations**.

---

## Features
- Converts each character of a name into:
  - **Decimal code** (ASCII/Unicode value using `ord()`)
  - **Binary code** (8-bit binary string)
- Displays results in a clear table format.

---

## Example

**Input:**

Enter your name: Niky


**Output:**

Character Decimal Binary

N 78 01001110
i 105 01101001
k 107 01101011
y 121 01111001


---

## Usage

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run the script:
   ```bash
   python name_to_codes.py

    Enter a name when prompted.

Code

def name_to_codes(name):
    binary_codes = []
    decimal_codes = []

    for char in name:
        decimal_value = ord(char)              # ASCII/Unicode decimal
        binary_value = format(decimal_value, '08b')  # 8-bit binary
        decimal_codes.append(decimal_value)
        binary_codes.append(binary_value)

    return decimal_codes, binary_codes


# Example usage
name = input("Enter your name: ")
decimals, binaries = name_to_codes(name)

print("\nCharacter  Decimal   Binary")
print("-" * 30)
for char, d, b in zip(name, decimals, binaries):
    print(f"{char:10} {d:<9} {b}")

Future Improvements

    Add reverse conversion: from decimal/binary back to text.

    Add support for saving results to a file.

    GUI version for easier use.
