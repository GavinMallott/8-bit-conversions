"""
Binary Conversions
--Convert Object--

Author: Gavin Mallott
Created: November 26, 2016
Lasted Edited: March 19, 2018
Last Edit: Improved logical operators
"""


import re


class AsciiConversionError(Exception):
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
        pass

    # General Conversions
    def to_binary(self, ascii=None, decimal=None, hexadecimal=None, binary=None):
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

    def to_hex(self, ascii=None, binary=None, decimal=None, hexadecimal=None):
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

    def to_decimal(self, ascii=None, binary=None, hexadecimal=None, decimal=None):
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

    def to_ascii(self, decimal=None, binary=None, hexadecimal=None, ascii=None):
        """ Takes a keyword value and returns it as a decimal
        """
        try:
            if decimal != None:
                return ' '.join([self.decimal_to_ascii(dec) for dec in decimal.split(" ")])
            elif binary != None:
                return ' '.join([self.binary_to_ascii(bin) for bin in binary.split(" ")])
            elif hexadecimal != None:
                return ' '.join([self.hex_to_ascii(hex) for hex in hexadecimal.split(" ")])
            elif ascii != None:
                return ascii
        except TypeError:
            raise AsciiConversionError

    # Number Conversions
    def decimal_to_binary(self, dec):
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

    def decimal_to_hex(self, dec):
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

    def binary_to_hex(self, bin):
        """Takes a given binary number and converts in into a hexadecimal number"""

        return self.decimal_to_hex(self.binary_to_decimal(bin))

    def binary_to_decimal(self, bin):
        """Takes a given binary number and converts it into a decimal number"""

        value = 128
        number_list = []
        for bit in str(bin):
            bit = int(bit)
            number_list.append(int(bit*value))
            value /= 2
        return str(sum(number_list))

    def hex_to_decimal(self, hex):
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

    def hex_to_binary(self, hex):
        """Takes a given hexadecimal number and converts it into a binary number"""

        return self.decimal_to_binary(self.hex_to_decimal(hex))

    # Text and number conversion
    def ascii_to_hex(self, ascii):
        """Takes a given ascii value and converts it into a hexadecimal number"""

        return self._interpret_ascii_to_hex(ascii)

    def hex_to_ascii(self, hex):
        """Takes a given hexadecimal number and converts it into an ascii value"""

        return self._interpret_hex_to_acii(hex)

    def ascii_to_binary(self, ascii):
        """Takes a given ascii value and converts it into a binary number"""

        return self.hex_to_binary(self.ascii_to_hex(ascii))

    def binary_to_ascii(self, bin):
        """Takes a given binary number and converts it into an ascii value"""

        return self.hex_to_ascii(self.binary_to_hex(bin))

    def ascii_to_decimal(self, ascii):
        """Takes a given ascii value and converts it into a decimal number"""

        return self.hex_to_decimal(self.ascii_to_hex(ascii))

    def decimal_to_ascii(self, dec):
        """Takes a given decimal number and converts it into an ascii value"""

        return self.hex_to_ascii(self.decimal_to_hex(dec))

    # Ascii Library
    def _interpret_hex_to_acii(self, hex):
        """Takes a given hexadecimal number and returns a matching ascii value"""

        if hex == '30': return '0'
        if hex == '31': return '1'
        if hex == '32': return '2'
        if hex == '33': return '3'
        if hex == '34': return '4'
        if hex == '35': return '5'
        if hex == '36': return '6'
        if hex == '37': return '7'
        if hex == '38': return '8'
        if hex == '39': return '9'

        if hex == '41': return 'A'
        if hex == '42': return 'B'
        if hex == '43': return 'C'
        if hex == '44': return 'D'
        if hex == '45': return 'E'
        if hex == '46': return 'F'
        if hex == '47': return 'G'
        if hex == '48': return 'H'
        if hex == '49': return 'I'
        if hex == '4A': return 'J'
        if hex == '4B': return 'K'
        if hex == '4C': return 'L'
        if hex == '4D': return 'M'
        if hex == '4E': return 'N'
        if hex == '4F': return 'O'
        if hex == '50': return 'P'
        if hex == '51': return 'Q'
        if hex == '52': return 'R'
        if hex == '53': return 'S'
        if hex == '54': return 'T'
        if hex == '55': return 'U'
        if hex == '56': return 'V'
        if hex == '57': return 'W'
        if hex == '58': return 'X'
        if hex == '59': return 'Y'
        if hex == '5A': return 'Z'

        if hex == '61': return 'a'
        if hex == '62': return 'b'
        if hex == '63': return 'c'
        if hex == '64': return 'd'
        if hex == '65': return 'e'
        if hex == '66': return 'f'
        if hex == '67': return 'g'
        if hex == '68': return 'h'
        if hex == '69': return 'i'
        if hex == '6A': return 'j'
        if hex == '6B': return 'k'
        if hex == '6C': return 'l'
        if hex == '6D': return 'm'
        if hex == '6E': return 'n'
        if hex == '6F': return 'o'
        if hex == '70': return 'p'
        if hex == '71': return 'q'
        if hex == '72': return 'r'
        if hex == '73': return 's'
        if hex == '74': return 't'
        if hex == '75': return 'u'
        if hex == '76': return 'v'
        if hex == '77': return 'w'
        if hex == '78': return 'x'
        if hex == '79': return 'y'
        if hex == '7A': return 'z'

        if hex == '20': return ' '
        if hex == '21': return '!'
        if hex == '22': return '"'
        if hex == '23': return '#'
        if hex == '24': return '$'
        if hex == '25': return '%'
        if hex == '26': return '&'
        if hex == '27': return "'"
        if hex == '28': return '('
        if hex == '29': return ')'
        if hex == '2A': return '*'
        if hex == '2B': return '+'
        if hex == '2C': return ','
        if hex == '2D': return '-'
        if hex == '2E': return '.'	
        if hex == '2F': return '/'

        if hex == '3A': return ':'
        if hex == '3B': return ';'
        if hex == '3C': return '<'
        if hex == '3D': return '='
        if hex == '3E': return '>'
        if hex == '3F': return '?'
        if hex == '40': return '@'

        if hex == '5B': return '['
        if hex == '5C': return "\\"
        if hex == '5D': return ']'
        if hex == '5E': return '^'
        if hex == '5F': return '_'
        if hex == '60': return '`'

        if hex == '7B': return '{'
        if hex == '7C': return '|'
        if hex == '7D': return '}'
        if hex == '7E': return '~'

    def _interpret_ascii_to_hex(self, ascii):
        """Takes a given ascii value and returns a matching hexadecimal number"""

        if ascii == '0': return '30'
        if ascii == '1': return '31'
        if ascii == '2': return '32'
        if ascii == '3': return '33'
        if ascii == '4': return '34'
        if ascii == '5': return '35'
        if ascii == '6': return '36'
        if ascii == '7': return '37'
        if ascii == '8': return '38'
        if ascii == '9': return '39'

        if ascii == 'A': return '41'
        if ascii == 'B': return '42'
        if ascii == 'C': return '43'
        if ascii == 'D': return '44'
        if ascii == 'E': return '45'
        if ascii == 'F': return '46'
        if ascii == 'G': return '47'
        if ascii == 'H': return '48'
        if ascii == 'I': return '49'
        if ascii == 'J': return '4A'
        if ascii == 'K': return '4B'
        if ascii == 'L': return '4C'
        if ascii == 'M': return '4D'
        if ascii == 'N': return '4E'
        if ascii == 'O': return '4F'
        if ascii == 'P': return '50'
        if ascii == 'Q': return '51'
        if ascii == 'R': return '52'
        if ascii == 'S': return '53'
        if ascii == 'T': return '54'
        if ascii == 'U': return '55'
        if ascii == 'V': return '56'
        if ascii == 'W': return '57'
        if ascii == 'X': return '58'
        if ascii == 'Y': return '59'
        if ascii == 'Z': return '5A'

        if ascii == 'a': return '61'
        if ascii == 'b': return '62'
        if ascii == 'c': return '63'
        if ascii == 'd': return '64'
        if ascii == 'e': return '65'
        if ascii == 'f': return '66'
        if ascii == 'g': return '67'
        if ascii == 'h': return '68'
        if ascii == 'i': return '69'
        if ascii == 'j': return '6A'
        if ascii == 'k': return '6B'
        if ascii == 'l': return '6C'
        if ascii == 'm': return '6D'
        if ascii == 'n': return '6E'
        if ascii == 'o': return '6F'
        if ascii == 'p': return '70'
        if ascii == 'q': return '71'
        if ascii == 'r': return '72'
        if ascii == 's': return '73'
        if ascii == 't': return '74'
        if ascii == 'u': return '75'
        if ascii == 'v': return '76'
        if ascii == 'w': return '77'
        if ascii == 'x': return '78'
        if ascii == 'y': return '79'
        if ascii == 'z': return '7A'

        if ascii == ' ': return '20'
        if ascii == '!': return '21'
        if ascii == '"': return '22'
        if ascii == '#': return '23'
        if ascii == '$': return '24'
        if ascii == '%': return '25'
        if ascii == '&': return '26'
        if ascii == "'": return '27'
        if ascii == '(': return '28'
        if ascii == ')': return '29'
        if ascii == '*': return '2A'
        if ascii == '+': return '2B'
        if ascii == ',': return '2C'
        if ascii == '-': return '2D'
        if ascii == '.': return '2E'
        if ascii == '/': return '2F'

        if ascii == ':': return '3A'
        if ascii == ';': return '3B'
        if ascii == '<': return '3C'
        if ascii == '=': return '3D'
        if ascii == '>': return '3E'
        if ascii == '?': return '3F'
        if ascii == '@': return '40'

        if ascii == '[': return '5B'
        if ascii == "\\": return '5C'
        if ascii == ']': return '5D'
        if ascii == '^': return '5E'
        if ascii == '_': return '5F'
        if ascii == '`': return '60'

        if ascii == '{': return '7B'
        if ascii == '|': return '7C'
        if ascii == '}': return '7D'
        if ascii == '~': return '7E'

    # Logical Operators
    def _multi_logical(self, logic_function, bin_one, bin_two):
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

    def _single_xor(self, bin_one, bin_two):
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

    def _single_and(self, bin_one, bin_two):
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

    def _single_or(self, bin_one, bin_two):
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

    def _single_not(self, bin):
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

    def logical_and(self, bin_one, bin_two):
        return self._multi_logical(self._single_and, bin_one, bin_two)

    def logical_or(self, bin_one, bin_two):
        return self._multi_logical(self._single_or, bin_one, bin_two)

    def logical_xor(self, bin_one, bin_two):
        return self._multi_logical(self._single_xor, bin_one, bin_two)

    def logical_not(self, bin_str):
        bins = bin_str.split(" ")
        notd_values = [self._single_not(bin) for bin in bins]
        return " ".join(notd_values)


if __name__ == '__main__':
    convert = Convert()

    bin_one = "01010101"
    bin_two = "11100000"
    bin_three = "00110011 " + "01010101"
    bin_four = "11100000" + " 00001111"

    binaries = [bin_one, bin_two, bin_three, bin_four]

    print("Not:")
    [print(convert.logical_not(bin)) for bin in binaries]
    print("\nAnd:")
    [[print(convert.logical_and(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]
    print("\nOr:")
    [[print(convert.logical_or(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]
    print("\nXor:")
    [[print(convert.logical_xor(bin1, bin2)) for bin1 in binaries] for bin2 in binaries]