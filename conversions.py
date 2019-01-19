"""
Binary Conversions
--Conversion Types--

Author: Gavin Mallott
Created: March 18, 2018
Lasted Edited: March 21, 2018
Last Edit: Added general conversions
"""


import convert


DEFAULT_BIT_SIZE = 8


# --- Exceptions --- #
class InvalidOperationError(Exception):
    pass


class InvalidTypeError(Exception):
    pass


class BitLengthError(Exception):
    pass


# --- ConversionValue Objects --- #
class ConversionValue(object):
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        self.value = value
        self._check_value_type()

        self._strtype = None

        self._size = size
        self._string_type = None

        self._convert = convert.Convert()

    def __str__(self):
        return " ".join(self.value)

    # --- Operator Overloading --- #
    def __add__(self, other_value):
        if type(self) == type(other_value):
            return type(self)([*self.value, *other_value.value])
        else:
            raise InvalidOperationError

    def __and__(self, other_value):
        bin_one = str(self.binary())
        bin_two = str(other_value.binary())
        converted = Binary(self._convert.logical_and(bin_one, bin_two))
        return converted

    def __or__(self, other_value):
        original_type = type(self)
        bin_one = self.binary()
        bin_two = other_value.binary()
        return type(self)(self._convert.logical_or(str(bin_one), str(bin_two)))

    def __xor__(self, other_value):
        original_type = type(self)
        bin_one = self.binary()
        bin_two = other_value.binary()
        return type(self)(self._convert.logical_xor(str(bin_one), str(bin_two)))

    def __invert__(self):
        original_type = type(self)
        return type(self)(self._convert.logical_not(str(self.binary())))

    def _check_value_type(self):
        value_type = type(self.value)
        if value_type != str and value_type != list:
            raise InvalidTypeError
        elif value_type == list and type(self.value[0]) != str:
            raise InvalidTypeError

        self._value_type = value_type

    def binary(self):
        return Binary(self._convert.to_binary(**{self._strtype: str(self)}))

    def hexadecimal(self):
        return Hexadecimal(self._convert.to_hex(**{self._strtype: str(self)}))

    def decimal(self):
        return Decimal(self._convert.to_decimal(**{self._strtype: str(self)}))

    def ascii(self, force=False):
        if not force:
            try:
                return Ascii(self._convert.to_ascii(**{self._strtype: str(self)}))
            except convert.AsciiConversionError:
                raise convert.AsciiConversionError
        else:
            ascii_values = []
            for value in self.value:
                try:
                    ascii_values.append(self._convert.to_ascii(**{self._strtype: value}))
                except convert.AsciiConversionError:
                    ascii_values.append("X")

            return Ascii(ascii_values)


class Binary(ConversionValue):
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        ConversionValue.__init__(self, value, size)
        self._strtype = "binary"
        self._reset_value()
        #self._check_value_size()

    def _reset_value(self):
        if self._value_type == str:
            if " " in self.value:
                self.value = self.value.split(" ")
            else:
                self.value = [self.value]

    def _check_value_size(self):
        for value in self.value:
            if len(value) != self._size:
                raise BitLengthError


class Hexadecimal(ConversionValue):
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        ConversionValue.__init__(self, value, size)
        self._strtype = "hexadecimal"
        self._reset_value()

    def _reset_value(self):
        if self._value_type == str:
            if " " in self.value:
                self.value = self.value.split(" ")
            else:
                self.value = [self.value]


class Decimal(ConversionValue):
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        ConversionValue.__init__(self, value, size)
        self._strtype = "decimal"
        self._reset_value()
        self._check_value_size()

    def _reset_value(self):
        if self._value_type == str:
            if " " in self.value:
                self.value = self.value.split(" ")
            else:
                self.value = [self.value]

    def _check_value_size(self):
        '''
        for value in self.value:
            if int(value) > (2**self._size) - 1:
                raise BitLengthError
        '''


class Ascii(ConversionValue):
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        ConversionValue.__init__(self, value, size)
        self._strtype = "ascii"
        self._reset_value()
        self._check_value_size()

    def __str__(self):
        return ''.join(self.value)

    def _reset_value(self):
        if type(self.value) == str:
            self.value = [value for value in self.value]

    def _check_value_size(self):
        for value in self.value:
            if len(value) > 1:
                raise BitLengthError


if __name__ == '__main__':

    """
    binary_number = Binary("00110101")
    other_binary = Binary("11001100 10101010")
    decimal_number = Decimal("74 75 32 99")
    hexadecimal_number = Hexadecimal(["3E", "54"])
    ascii_string = Ascii("Hello There")
    ascii_string_two = Ascii(["G", "a", "v", "i", "n"])

    print(decimal_number.binary())
    print(binary_number)

    print(decimal_number.binary() & binary_number)

    print(binary_number.decimal())
    print(decimal_number.binary().decimal())

    print((decimal_number.binary() & binary_number.binary()).decimal())

    """
    # --- xor test --- #
    bin_one = Binary("00001111")
    bin_two = Binary("01000000")
    dec_one = Decimal("52")

    print(dec_one.binary())
    print(~dec_one.binary())

    print((~dec_one).decimal())


    #print(decimal_number & binary_number)

    