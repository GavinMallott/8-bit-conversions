"""
Binary Conversions
--Convert Object--

Author: Gavin Mallott
Created: November 26, 2016
Lasted Edited: January 20, 2019
Last Edit: Added bitwise shift function, improved documentation
"""


import re


class AsciiConversionError(Exception):
    """The given value does not have an ascii equivalent"""
    pass


# --- Convert Object --- #
class Convert(object):
    """ Controls the conversion of 
        Binary to Decimal,
        Deciamal to Binary,
        Hexadecimal to Decimal,
        Decimal to Hexadecimal,
        Binary to Hexadecimal,
        Hexadecimal to Binary,
        and ASCII Comparisons
    """
    def __init__(self):
        self.hex_to_ascii_dict = {
        '30': '0',
        '31': '1',
        '32': '2',
        '33': '3',
        '34': '4',
        '35': '5',
        '36': '6',
        '37': '7',
        '38': '8',
        '39': '9',

        '41': 'A',
        '42': 'B',
        '43': 'C',
        '44': 'D',
        '45': 'E',
        '46': 'F',
        '47': 'G',
        '48': 'H',
        '49': 'I',
        '4A': 'J',
        '4B': 'K',
        '4C': 'L',
        '4D': 'M',
        '4E': 'N',
        '4F': 'O',
        '50': 'P',
        '51': 'Q',
        '52': 'R',
        '53': 'S',
        '54': 'T',
        '55': 'U',
        '56': 'V',
        '57': 'W',
        '58': 'X',
        '59': 'Y',
        '5A': 'Z',

        '61': 'a',
        '62': 'b',
        '63': 'c',
        '64': 'd',
        '65': 'e',
        '66': 'f',
        '67': 'g',
        '68': 'h',
        '69': 'i',
        '6A': 'j',
        '6B': 'k',
        '6C': 'l',
        '6D': 'm',
        '6E': 'n',
        '6F': 'o',
        '70': 'p',
        '71': 'q',
        '72': 'r',
        '73': 's',
        '74': 't',
        '75': 'u',
        '76': 'v',
        '77': 'w',
        '78': 'x',
        '79': 'y',
        '7A': 'z',

        '20': ' ',
        '21': '!',
        '22': '"',
        '23': '#',
        '24': '$',
        '25': '%',
        '26': '&',
        '27': "'",
        '28': '(',
        '29': ')',
        '2A': '*',
        '2B': '+',
        '2C': ',',
        '2D': '-',
        '2E': '.',	
        '2F': '/',

        '3A': ':',
        '3B': ';',
        '3C': '<',
        '3D': '=',
        '3E': '>',
        '3F': '?',
        '40': '@',

        '5B': '[',
        '5C': "\\",
        '5D': ']',
        '5E': '^',
        '5F': '_',
        '60': '`',

        '7B': '{',
        '7C': '|',
        '7D': '}',
        '7E': '~'}

    # General Conversions
    def to_binary(self, ascii=None, decimal=None, hexadecimal=None, binary=None) -> str:
        """ Takes a keyword value and returns it as a binary
        """
        if ascii != None:
            return ' '.join([self.ascii_to_binary(char) for char in ascii])
        elif decimal != None:
            return ' '.join([self.decimal_to_binary(dec) for dec in decimal.split(" ")])
        elif hexadecimal != None:
            return ' '.join([self.hex_to_binary(hex) for hex in hexadecimal.split(" ")])
        elif binary != None:
            return binary

    def to_hex(self, ascii=None, binary=None, decimal=None, hexadecimal=None) -> str:
        """ Takes a keyword value and returns it as a hexadecimal
        """
        if ascii != None:
            return " ".join([self.ascii_to_hex(char) for char in ascii])
        elif binary != None:
            return ' '.join([self.binary_to_hex(bin) for bin in binary.split(" ")])
        elif decimal != None:
            return ' '.join([self.decimal_to_hex(dec) for dec in decimal.split(" ")])
        elif hexadecimal != None:
            return hexadecimal

    def to_decimal(self, ascii=None, binary=None, hexadecimal=None, decimal=None) -> str:
        """ Takes a keyword value and returns it as a decimal
        """
        if ascii != None:
            return ' '.join([self.ascii_to_decimal(char) for char in ascii])
        elif binary != None:
            return ' '.join([self.binary_to_decimal(bin) for bin in binary.split(" ")])
        elif hexadecimal != None:
            return ' '.join([self.hex_to_decimal(hex) for hex in hexadecimal.split(" ")])
        elif decimal != None:
            return decimal

    def to_ascii(self, decimal=None, binary=None, hexadecimal=None, ascii=None) -> str:
        """ Takes a keyword value and returns it as a decimal
        """
        try:
            if decimal != None:
                return ''.join([self.decimal_to_ascii(dec) for dec in decimal.split(" ")])
            elif binary != None:
                return ''.join([self.binary_to_ascii(bin) for bin in binary.split(" ")])
            elif hexadecimal != None:
                return ''.join([self.hex_to_ascii(hex) for hex in hexadecimal.split(" ")])
            elif ascii != None:
                return ascii
        except TypeError:
            raise AsciiConversionError

    # Number Conversions
    def decimal_to_binary(self, dec: str) -> str:
        """Takes a given decimal number and converts it into a binary number"""

        dec = int(dec)
        binary_number = []
        value = 128
        for x in range(0,8):
            if dec >= value:
                binary_number.append("1")
                dec -= value
                value /= 2		
            else:
                binary_number.append("0")
                value /= 2

        return "".join(binary_number)

    def decimal_to_hex(self, dec: str) -> str:
        """Takes a given decimal number and converts it into a hexadecimal number"""

        dec = int(dec)
        first = int(dec / 16)
        second = 0
        if first > 0:
            second = dec - (16*first)
        else:
            second = dec

        if first > 9:
            if first == 10: first = "A"
            if first == 11: first = "B"
            if first == 12: first = "C"
            if first == 13: first = "D"
            if first == 14: first = "E"
            if first == 15: first = "F"

        if second > 9:
            if second == 10: second = "A"
            if second == 11: second = "B"
            if second == 12: second = "C"
            if second == 13: second = "D"
            if second == 14: second = "E"
            if second == 15: second = "F"

        return str(first) + str(second)

    def binary_to_hex(self, bin: str) -> str:
        """Takes a given binary number and converts in into a hexadecimal number"""
        
        return self.decimal_to_hex(self.binary_to_decimal(bin))

    def binary_to_decimal(self, bin: str) -> str:
        """Takes a given binary number and converts it into a decimal number"""

        value = 128
        number_list = []
        for bit in str(bin):
            bit = int(bit)
            number_list.append(int(bit*value))
            value /= 2
        return str(sum(number_list))

    def hex_to_decimal(self, hex: str) -> str:
        """Takes a given hexadecimal number and converts it into a decimal number"""

        number = []
        value = 16
        for item in hex:

            if item == "A": item = 10
            if item == "B": item = 11
            if item == "C": item = 12
            if item == "D": item = 13
            if item == "E": item = 14
            if item == "F": item = 15
            number.append(int(int(item)*value))
            value /= 16
        return str(sum(number))

    def hex_to_binary(self, hex: str) -> str:
        """Takes a given hexadecimal number and converts it into a binary number"""

        return self.decimal_to_binary(self.hex_to_decimal(hex))

    # Text and number conversion
    def ascii_to_hex(self, ascii: str) -> str:
        """Takes a given ascii value and converts it into a hexadecimal number"""
        try:
            return [hex for hex, ascii_val in self.hex_to_ascii_dict.items() if ascii_val == ascii][0]
        except KeyError:
            pass

    def hex_to_ascii(self, hex: str) -> str:
        """Takes a given hexadecimal number and converts it into an ascii value"""
        try:
            return self.hex_to_ascii_dict[hex]
        except KeyError:
            pass

    def ascii_to_binary(self, ascii: str) -> str:
        """Takes a given ascii value and converts it into a binary number"""

        return self.hex_to_binary(self.ascii_to_hex(ascii))

    def binary_to_ascii(self, bin: str) -> str:
        """Takes a given binary number and converts it into an ascii value"""

        return self.hex_to_ascii(self.binary_to_hex(bin))

    def ascii_to_decimal(self, ascii: str) -> str:
        """Takes a given ascii value and converts it into a decimal number"""

        return self.hex_to_decimal(self.ascii_to_hex(ascii))

    def decimal_to_ascii(self, dec: str) -> str:
        """Takes a given decimal number and converts it into an ascii value"""

        return self.hex_to_ascii(self.decimal_to_hex(dec))

    # Logical Operators
    def _multi_logical(self, logic_function: 'function', bin_one: str, bin_two: str) -> str:
        """Given a logic funtion (and, or, not, xor) and two binary numbers, will return the result"""
        if len(bin_one.split(" ")) > 1 and len(bin_two.split(" ")) > 1:
            operated_list = []
            for x, bin_1 in enumerate(bin_one.split(" ")):
                operated_list.append(logic_function(bin_1, bin_two.split(" ")[x]))
            return ' '.join(operated_list)
        elif len(bin_one.split(" ")) > 1:
            return ' '.join([logic_function(bin, bin_two) for bin in bin_one.split(" ")])
        elif len(bin_two.split(" ")) > 1:
            return ' '.join([logic_function(bin_one, bin) for bin in bin_two.split(" ")])
        else:
            return logic_function(bin_one, bin_two)

    def _single_xor(self, bin_one: str, bin_two: str) -> str:
        """Takes two given binary numbers and returns the logical XOR of the numbers"""
        bin_one = str(bin_one)
        bin_two = str(bin_two)
        bin_one_int = [int(letter) for letter in bin_one]
        bin_two_int = [int(letter) for letter in bin_two]

        xord_values = []
        
        for value in range(0,8):
            if bin_one_int[value] == bin_two_int[value]:
                xord_values.append(str(0))
            else:
                xord_values.append(str(1))

        return ''.join(xord_values)

    def _single_and(self, bin_one: str, bin_two: str) -> str:
        """Takes two given binary numbers and returns the logical AND of the numbers"""

        bin_one_int = []
        bin_two_int = []

        for letter in bin_one:
            bin_one_int.append(int(letter))

        for letter in bin_two:
            bin_two_int.append(int(letter))

        andd_values = []

        for value in range(0,8):
            if bin_one_int[value] == 1 and bin_two_int[value] == 1:
                andd_values.append(str(1))
            else:
                andd_values.append(str(0))

        return "".join(andd_values)

    def _single_or(self, bin_one: str, bin_two: str) -> str:
        """Takes two given binary numbers and returns the logical OR of the numbers"""

        bin_one_int = []
        bin_two_int = []

        for letter in bin_one:
            bin_one_int.append(int(letter))

        for letter in bin_two:
            bin_two_int.append(int(letter))

        ord_values = []

        for value in range(0,8):
            if bin_one_int[value] == 1 or bin_two_int[value] == 1:
                ord_values.append(str(1))
            else:
                ord_values.append(str(0))

        return "".join(ord_values)

    def _single_not(self, bin: str) -> str:
        """Takes a given binary number and returns the logical NOT of the binary number"""

        bin_int = []

        for letter in bin:
            bin_int.append(int(letter))

        notd_values = []

        for value in range(0,8):
            if bin_int[value] == 1:
                notd_values.append(str(0))
            else:
                notd_values.append(str(1))

        return ''.join(notd_values)

    def _single_bitwise_shift(self, bin_str: str, direction: bool, bits: int) -> str:
        """Shifts binary number by given bits in given direction (1: right, 0: left)"""
        new_bin = ["0" for i in range(bits)]
        all_bits = list(bin_str)
        while len(new_bin) < 8:
            if direction:
                new_bin.append(all_bits[0])
                del all_bits[0]
            else:
                new_bin = [all_bits[-1]] + new_bin
                del all_bits[-1]

        return ''.join(new_bin)

    def logical_and(self, bin_one: str, bin_two: str) -> str:
        """Returns the AND operation on two binary numbers"""
        return self._multi_logical(self._single_and, bin_one, bin_two)

    def logical_or(self, bin_one: str, bin_two: str) -> str:
        """Returns the OR operation on two binary numbers"""
        return self._multi_logical(self._single_or, bin_one, bin_two)

    def logical_xor(self, bin_one: str, bin_two: str) -> str:
        """Returns the XOR operation on two binary numbers"""
        return self._multi_logical(self._single_xor, bin_one, bin_two)

    def logical_not(self, bin_str: str) -> str:
        """Returns the NOT operation on a binary number"""
        bins = bin_str.split(" ")
        notd_values = [self._single_not(bin) for bin in bins]
        return " ".join(notd_values)

    def bitwise_shift(self, bin_str: str, direction: bool, bits: int) -> str:
        """Shifts binary number by given bits in given direction (1: right, 0: left)"""
        bins = bin_str.split(" ")
        shifted_values = [self._single_bitwise_shift(bin, direction, bits) for bin in bins]
        return " ".join(shifted_values)


if __name__ == '__main__':
    convert = Convert()

    bin_one = "01010101"
    bin_two = "11100000"
    bin_three = "00110011 01010101"
    bin_four = "11100000 00001111"

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
    [print((bin + " >> " + "2" + ": " + convert.bitwise_shift(bin, 1, 2)) + ", " + bin + " << " + "2" + ": " + (convert.bitwise_shift(bin, 0, 2))) for bin in binaries]