# 8-bit-conversions

Two main files:
  * convert.py
  * conversions.py
    
## convert.py

 The convert.py file provides the Convert class.
  
 This class is used to convert between binary, hexadecimal, decimal, and ascii values.  All values are expected as " "-speparated strings of 8-bit characters e.g. `"00001111 10101010", "F0 5E", "129 255", "Hello There"`.  Convert also includes bitwise operations: and, or, xor, not (invert) and bitwise shifts.  Initialize the Convert object with `convert = Convert()`.
  
#### Examples:
<details><summary>Creating Binary Numbers</summary>
<p>

```python
bin_one = "01010101"
bin_two = "11100000"
bin_three = "00110011 01010101"
bin_four = "11100000 00001111"
```
</p>
</details>

<details><summary>Examples of all bitwise operations on four different binary numbers:</summary>
<p>

```python
binaries = [bin_one, bin_two, bin_three, bin_four]

print("Binaries:")
[print(bin) for bin in binaries]

print("\nNot:")
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

<details><summary>This will output:</summary>
<p>

```
Binaries:
01010101
11100000
00110011 01010101
11100000 00001111

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
</p>
</details>


## conversions.py

 The conversions.py file creates datatypes for Binary, Hexadecimal, Decimal, and Ascii.  The ConversionValue class is the base class, with each subtype inhieriting from it.  ConversionValue adds methods to convert easily between different datatypes with `self.binary(), self.hexadecimal(), self.decimal(), and self.ascii()`. 
 
 The ConversionValue class also adds operator overloading methods.  The `+` operator concatentates numbers of the same datatype.  The `&, |, ^, and ~` perform and, or, xor, and not operations respectivly. The `>> and <<` perform bitwise shifts on binary numbers.
  
#### Examples:
<details><summary>Creating numbers in each datatype</summary>
<p>

```python
bin_one = Binary("00001111")
bin_two = Binary("00110011")

hex_one = Hexadecimal("10")
hex_two = Hexadecimal("40")

dec_one = Decimal("16")
dec_two = Decimal("128")

ascii_one = Ascii(" ")
ascii_two = Ascii("a")

print("Basic Values:")
print(bin_one)
print(bin_two, "\n")
print(hex_one)
print(hex_two, "\n")
print(dec_one)
print(dec_two, "\n")
print(ascii_one)
print(ascii_two, "\n")
```

<details><summary>This will output</summary>
<p>

```
Basic Values:
00001111
00110011 

10
40 

16
128 

 
a 
```
</p>
</details>
</p>
</details>

<details><summary>Example of all operations</summary>
<p>
 
```python
# --- Prints binary version of Basic Values --- #
print("Binary Values:")
print(bin_one.binary())
print(bin_two.binary(), "\n")
print(hex_one.binary())
print(hex_two.binary(), "\n")
print(dec_one.binary())
print(dec_two.binary(), "\n")
print(ascii_one.binary())
print(ascii_two.binary(), "\n")

# --- Prints hexadecimal version of Basic Values --- #
print("Hexadecimal Values:")
print(bin_one.hexadecimal())
print(bin_two.hexadecimal(), "\n")
print(hex_one.hexadecimal())
print(hex_two.hexadecimal(), "\n")
print(dec_one.hexadecimal())
print(dec_two.hexadecimal(), "\n")
print(ascii_one.hexadecimal())
print(ascii_two.hexadecimal(), "\n")

# --- Prints decimal version of Basic Values --- #
print("Decimal Values:")
print(bin_one.decimal())
print(bin_two.decimal(), "\n")
print(hex_one.decimal())
print(hex_two.decimal(), "\n")
print(dec_one.decimal())
print(dec_two.decimal(), "\n")
print(ascii_one.decimal())
print(ascii_two.decimal(), "\n")

# --- Prints ascii version (if possible) of Basic Values --- #
print("Ascii Values:")
print(bin_one.ascii())
print(bin_two.ascii(), "\n")
print(hex_one.ascii())
print(hex_two.ascii(), "\n")
print(dec_one.ascii())
print(dec_two.ascii(), "\n")
print(ascii_one.ascii())
print(ascii_two.ascii(), "\n")

# --- Adds same datatypes --- #
print("Adds same datatypes:")
print(bin_one + bin_two)
print(hex_one + hex_two)
print(dec_one + dec_two)
print(ascii_one + ascii_two)

# --- ANDs same datatypes --- #
print("\nANDs same datatypes:")
print(bin_one & bin_two)
print(hex_one & hex_two)
print(dec_one & dec_two)
print(ascii_one & ascii_two)

# --- ORs same datatypes --- #
print("\nORs same datatypes:")
print(bin_one | bin_two)
print(hex_one | hex_two)
print(dec_one | dec_two)
print(ascii_one | ascii_two)

# --- XORs same datatypes --- #
print("\nXORs same datatypes:")
print(bin_one ^ bin_two)
print(hex_one ^ hex_two)
print(dec_one ^ dec_two)
print(ascii_one ^ ascii_two)

# --- Inverts values --- #
print("\nInverts values:")
print(~bin_one)
print(~hex_one)
print(~dec_one)
print(~ascii_one)

# --- Bitwise Shift --- #
print("\nShift all values left and right by 2 bits:")
print((bin_one >> 2), (bin_one << 2))
print((hex_one >> 2), (hex_one << 2))
print((dec_one >> 2), (dec_one << 2))
print((ascii_one >> 2), (ascii_one << 2))

# --- ANDs same datatypes conserves type --- #
print("\nANDs same datatypes conserves type:")
print(bin_one & bin_two)
print((hex_one & hex_two).hexadecimal())
print((dec_one & dec_two).decimal())
print((ascii_one & ascii_two).ascii())

# --- ORs same datatypes conserves type --- #
print("\nORs same datatypes conserves type:")
print(bin_one | bin_two)
print((hex_one | hex_two).hexadecimal())
print((dec_one | dec_two).decimal())
print((ascii_one | ascii_two).ascii())

# --- XORs same datatypes conserves type --- #
print("\nXORs same datatypes conserves type:")
print(bin_one ^ bin_two)
print((hex_one ^ hex_two).hexadecimal())
print((dec_one ^ dec_two).decimal())
print((ascii_one ^ ascii_two).ascii())

# --- Inverts values conserves type --- #
print("\nInverts values conserves type:")
print(~bin_one)
print((~hex_one).hexadecimal())
print((~dec_one).decimal())
print((~ascii_one).ascii())

# --- Bitwise Shift conserves type --- #
print("\nShift all values left and right by 2 bits and conserves type:")
print((bin_one >> 2), (bin_one << 2))
print((hex_one >> 2).hexadecimal(), (hex_one << 2).hexadecimal())
print((dec_one >> 2).decimal(), (dec_one << 2).decimal())
print((ascii_one >> 2).ascii(), (ascii_one << 2).ascii())
```

<details><summary>This will output</summary>
<p>

```
Binary Values:
00001111
00110011 

00010000
01000000 

00010000
10000000 

00100000
01100001 

Hexadecimal Values:
0F
33 

10
40 

10
80 

20
61 

Decimal Values:
15
51 

16
64 

16
128 

32
97 

Ascii Values:
None
3 

None
@ 

None
None 

 
a 

Adds same datatypes:
00001111 00110011
10 40
16 128
 a

ANDs same datatypes:
00000011
00000000
00000000
00100000

ORs same datatypes:
00111111
01010000
10010000
01100001

XORs same datatypes:
00111100
01010000
10010000
01000001

Inverts values:
11110000
11101111
11101111
11011111

Shift all values left and right by 2 bits:
00000011 00111100
00000100 01000000
00000100 01000000
00001000 10000000

ANDs same datatypes conserves type:
00000011
00
0
 

ORs same datatypes conserves type:
00111111
50
144
a

XORs same datatypes conserves type:
00111100
50
144
A

Inverts values conserves type:
11110000
EF
239
None

Shift all values left and right by 2 bits and conserves type:
00000011 00111100
04 40
4 64
None None
```

</p>
</details>
</p>
</details>
 
