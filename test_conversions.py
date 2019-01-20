from conversions import *

# --- Sets Basic Values --- #
bin_one = Binary("00001111")
bin_two = Binary("00110011")

hex_one = Hexadecimal("10")
hex_two = Hexadecimal("40")

dec_one = Decimal("16")
dec_two = Decimal("128")

ascii_one = Ascii(" ")
ascii_two = Ascii("a")

# --- Prints Basic Values --- #
print("Basic Values:")
print(bin_one)
print(bin_two, "\n")
print(hex_one)
print(hex_two, "\n")
print(dec_one)
print(dec_two, "\n")
print(ascii_one)
print(ascii_two, "\n")

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