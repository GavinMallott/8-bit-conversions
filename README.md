# 8-bit-conversions

Two main files:
  * convert.py
  * conversions.py
    
## convert.py:

  The convert.py file provides the Convert class.
  
  This class is used to convert between binary, hexadecimal, decimal, and ascii values.  All values are expected as " "-speparated strings of 8-bit characters e.g. "00001111 10101010", "F0 5E", "129 255", "Hello There".  Convert also includes bitwise operations: and, or, xor, not (invert) and bitwise shifts.
  
#### Examples:
<details><summary>Examples of all bitwise operations on four different binary numbers:</summary>
```
binaries = [bin_one, bin_two, bin_three, bin_four]

print("Not:")
[print(convert.logical_not(bin)) for bin in binaries]
print("\nAnd:")
[[print(convert.logical_and(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]
print("\nOr:")
[[print(convert.logical_or(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]
print("\nXor:")
[[print(convert.logical_xor(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]
print("\nBitwise Shift:")
[[print((convert.bitwise_shift(bin, 1, 2)), (convert.bitwise_shift(bin, 0, 2))) for bin in binaries]
```

will output:

Not:
10101010
00011111
11001100 10101010
00011111 11110000

And:
01010101
01000000
00010001 01010101
01000000 00000101
01000000
11100000
00100000 01000000
11100000 00000000
00010001 01010101
00100000 01000000
00110011 01010101
00100000 00000101
01000000 00000101
11100000 00000000
00100000 00000101
11100000 00001111

Or:
01010101
11110101
01110111 01010101
11110101 01011111
11110101
11100000
11110011 11110101
11100000 11101111
01110111 01010101
11110011 11110101
00110011 01010101
11110011 01011111
11110101 01011111
11100000 11101111
11110011 01011111
11100000 00001111

Xor:
00000000
10110101
01100110 00000000
10110101 01011010
10110101
00000000
11010011 10110101
00000000 11101111
01100110 00000000
11010011 10110101
00000000 00000000
11010011 01011010
10110101 01011010
00000000 11101111
11010011 01011010
00000000 00000000

Bitwise Shift:
00010101 01010100
00111000 10000000
00001100 01010100
00111000 00111100</summary>
