# 8-bit-conversions

Two main files:
  * convert.py
  * conversions.py
    
## convert.py:

  The convert.py file provides the Convert class.
  
  This class is used to convert between binary, hexadecimal, decimal, and ascii values.  All values are expected as " "-speparated strings of 8-bit characters e.g. "00001111 10101010", "F0 5E", "129 255", "Hello There".  Convert also includes bitwise operations: and, or, xor, not (invert) and bitwise shifts.
  
#### Examples:
<details><summary>Examples of all bitwise operations on four different binary numbers:</summary>
<p>

```python
binaries = [bin_one, bin_two, bin_three, bin_four]

print("Not:")
[print("NOT " + bin + ": " + convert.logical_not(bin)) for bin in binaries]
print("\nAnd:")
[[print(bin1 + " AND " + bin2 + ": " + convert.logical_and(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]
print("\nOr:")
[[print(bin1 + " OR " + bin2 + ": " + convert.logical_or(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]
print("\nXor:")
[[print(bin1 + " XOR " + bin2 + ": " + convert.logical_xor(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]
print("\nBitwise Shift:")
[print((bin + " >> " + "2" + ": " + convert.bitwise_shift(bin, 1, 2)) + ", " + bin + " << " + "2" + (convert.bitwise_shift(bin, 0, 2))) for bin in binaries]
```

Will output:

```
Not:
NOT 01010101: 10101010
NOT 11100000: 00011111
NOT 00110011 01010101: 11001100 10101010
NOT 11100000 00001111: 00011111 11110000

And:
01010101 AND 01010101: 01010101
11100000 AND 01010101: 01000000
00110011 01010101 AND 01010101: 00010001 01010101
11100000 00001111 AND 01010101: 01000000 00000101
01010101 AND 11100000: 01000000
11100000 AND 11100000: 11100000
00110011 01010101 AND 11100000: 00100000 01000000
11100000 00001111 AND 11100000: 11100000 00000000
01010101 AND 00110011 01010101: 00010001 01010101
11100000 AND 00110011 01010101: 00100000 01000000
00110011 01010101 AND 00110011 01010101: 00110011 01010101
11100000 00001111 AND 00110011 01010101: 00100000 00000101
01010101 AND 11100000 00001111: 01000000 00000101
11100000 AND 11100000 00001111: 11100000 00000000
00110011 01010101 AND 11100000 00001111: 00100000 00000101
11100000 00001111 AND 11100000 00001111: 11100000 00001111

Or:
01010101 OR 01010101: 01010101
11100000 OR 01010101: 11110101
00110011 01010101 OR 01010101: 01110111 01010101
11100000 00001111 OR 01010101: 11110101 01011111
01010101 OR 11100000: 11110101
11100000 OR 11100000: 11100000
00110011 01010101 OR 11100000: 11110011 11110101
11100000 00001111 OR 11100000: 11100000 11101111
01010101 OR 00110011 01010101: 01110111 01010101
11100000 OR 00110011 01010101: 11110011 11110101
00110011 01010101 OR 00110011 01010101: 00110011 01010101
11100000 00001111 OR 00110011 01010101: 11110011 01011111
01010101 OR 11100000 00001111: 11110101 01011111
11100000 OR 11100000 00001111: 11100000 11101111
00110011 01010101 OR 11100000 00001111: 11110011 01011111
11100000 00001111 OR 11100000 00001111: 11100000 00001111

Xor:
01010101 XOR 01010101: 00000000
11100000 XOR 01010101: 10110101
00110011 01010101 XOR 01010101: 01100110 00000000
11100000 00001111 XOR 01010101: 10110101 01011010
01010101 XOR 11100000: 10110101
11100000 XOR 11100000: 00000000
00110011 01010101 XOR 11100000: 11010011 10110101
11100000 00001111 XOR 11100000: 00000000 11101111
01010101 XOR 00110011 01010101: 01100110 00000000
11100000 XOR 00110011 01010101: 11010011 10110101
00110011 01010101 XOR 00110011 01010101: 00000000 00000000
11100000 00001111 XOR 00110011 01010101: 11010011 01011010
01010101 XOR 11100000 00001111: 10110101 01011010
11100000 XOR 11100000 00001111: 00000000 11101111
00110011 01010101 XOR 11100000 00001111: 11010011 01011010
11100000 00001111 XOR 11100000 00001111: 00000000 00000000

Bitwise Shift:
01010101 >> 2: 00010101, 01010101 << 2: 01010100
11100000 >> 2: 00111000, 11100000 << 2: 10000000
00110011 01010101 >> 2: 00001100 00010101, 00110011 01010101 << 2: 11001100 01010100
11100000 00001111 >> 2: 00111000 00000011, 11100000 00001111 << 2: 10000000 00111100
```
</p>
</details>
