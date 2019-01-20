"""
Binary Conversions
--Conversion Types--

Author: Gavin Mallott
Created: March 18, 2018
Lasted Edited: January 20, 2019
Last Edit: Added bitwise shift operators, improved documentation
"""


import convert


DEFAULT_BIT_SIZE = 8        #All the number of bits each value (decimal, binary, hexadecimal, and ascii characters) can have is defined here


# --- Exceptions --- #
class InvalidOperationError(Exception):
    """The operation called expects a different data type than the one given"""
    pass


class InvalidTypeError(Exception):
    """The function called expects a different data type than the one given"""
    pass


class BitLengthError(Exception):
    """The resulting value does not fit the bit-size defined by DEFAULT_BIT_SIZE"""
    pass


# --- ConversionValue Objects --- #
class ConversionValue(object):
    """ Base class for binary, decimal, hexadecimal, and ascii datatypes
        Contains methods for and, or, xor and not (inverse) logical operations
        Contains methods or converting between datatypes
    """
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        """ Sets value, _size, checks value size
            Initializes _strtype
            Initializes Convert() class, can be referenced by _convert
        """
        self.value = value
        self._size = size
        self._check_value_type()

        self._strtype = None

        self._convert = convert.Convert()

    def __str__(self) -> str:
        """When an instance of this class is called by itself, it will display it's self.value as a string"""
        return " ".join(self.value)

    # --- Operator Overloading --- #
    def __add__(self, other_value: 'ConversionValue') -> 'ConversionValue':
        """Concatenate instance of this object with any other object of the same datatype with the + operator"""
        if type(self) == type(other_value):
            return type(self)([*self.value, *other_value.value])
        else:
            raise InvalidOperationError

    def __and__(self, other_value: 'ConversionValue') -> 'Binary':
        """Return the AND result of this object and any other object inherited from this class with the & operator"""
        bin_one = str(self.binary())
        bin_two = str(other_value.binary())
        return Binary(self._convert.logical_and(bin_one, bin_two))

    def __or__(self, other_value: 'ConversionValue') -> 'Binary':
        """Return the OR result of this object and any other object inherited from this class with the | operator"""
        bin_one = self.binary()
        bin_two = other_value.binary()
        return Binary(self._convert.logical_or(str(bin_one), str(bin_two)))

    def __xor__(self, other_value: 'ConversionValue') -> 'Binary':
        """Return the AND result of this object and any other object inherited from this class with the ^ operator"""
        bin_one = self.binary()
        bin_two = other_value.binary()
        return Binary(self._convert.logical_xor(str(bin_one), str(bin_two)))

    def __invert__(self):
        """Return the inverted (NOT) of this object with the ~ operator"""
        return Binary(self._convert.logical_not(str(self.binary())))

    def __rshift__(self, bits: int) -> 'Binary':
        """Shifts binary value right by number of given bits with the >> operator"""
        return Binary(self._convert.bitwise_shift(str(self.binary()), 1, bits))

    def __lshift__(self, bits: int) -> 'Binary':
        """Shifts binary value left by number of given bits with the << operator"""
        return Binary(self._convert.bitwise_shift(str(self.binary()), 0, bits))

    # --- Converting Datatypes --- #
    def _check_value_type(self):
        """Checks to make sure the self.value of the object is either a string or a list, and fits the required bit-size"""
        value_type = type(self.value)
        if value_type != str and value_type != list:
            raise InvalidTypeError
        elif value_type == list and type(self.value[0]) != str:
            raise InvalidTypeError

        self._value_type = value_type

    def binary(self) -> 'Binary':
        """Converts object to Binary type"""
        return Binary(self._convert.to_binary(**{self._strtype: str(self)}))

    def hexadecimal(self) -> 'Hexadecimal':
        """Converts object to Hexadecimal type"""
        return Hexadecimal(self._convert.to_hex(**{self._strtype: str(self)}))

    def decimal(self) -> 'Decimal':
        """Converts object to Decimal type"""
        return Decimal(self._convert.to_decimal(**{self._strtype: str(self)}))

    def ascii(self, force=False) -> 'Ascii':
        """ Converts object to Ascii type
            Set force=True to disable value checking
        """
        if not force:
            try:
                return Ascii(self._convert.to_ascii(**{self._strtype: str(self)}))
            except convert.AsciiConversionError:
                pass
        else:
            ascii_values = []
            for value in self.value:
                try:
                    ascii_values.append(self._convert.to_ascii(**{self._strtype: value}))
                except convert.AsciiConversionError:
                    ascii_values.append("X")

            return Ascii(ascii_values)


class Binary(ConversionValue):
    """ Binary datatype inhierited from ConversionValue class
        Sets the value syntax to common form
        Checks value to fit in desired bit-size
        Creates _strtype to reference data type
    """
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        """Calls super().__init__()
            Sets _strtype to binary
            Normalizes value syntax
            Checks value size
        """
        ConversionValue.__init__(self, value, size)
        self._strtype = "binary"
        self._reset_value()
        self._check_value_size()

    def _reset_value(self):
        """Converts given self.value to a common syntax"""
        if self._value_type == str:
            if " " in self.value:
                self.value = self.value.split(" ")
            else:
                self.value = [self.value]

    def _check_value_size(self):
        """Checks to make sure the given value fits in the desired bit-size"""
        for value in self.value:
            if len(value) != self._size:
                raise BitLengthError


class Hexadecimal(ConversionValue):
    """ Hexadecimal datatype inhierited from ConversionValue class
        Sets the value syntax to common form
        Checks value to fit in desired bit-size
        Creates _strtype to reference data type
    """
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        """Calls super().__init__()
            Sets _strtype to hexadecimal
            Normalizes value syntax
        """
        ConversionValue.__init__(self, value, size)
        self._strtype = "hexadecimal"
        self._reset_value()

    def _reset_value(self):
        """Converts given self.value to a common syntax"""
        if self._value_type == str:
            if " " in self.value:
                self.value = self.value.split(" ")
            else:
                self.value = [self.value]


class Decimal(ConversionValue):
    """ Decimal datatype inhierited from ConversionValue class
        Sets the value syntax to common form
        Checks value to fit in desired bit-size
        Creates _strtype to reference data type
    """
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        """Calls super().__init__()
            Sets _strtype to decimal
            Normalizes value syntax
            Checks value size
        """
        ConversionValue.__init__(self, value, size)
        self._strtype = "decimal"
        self._reset_value()
        self._check_value_size()

    def _reset_value(self):
        """Converts given self.value to a common syntax"""
        if self._value_type == str:
            if " " in self.value:
                self.value = self.value.split(" ")
            else:
                self.value = [self.value]

    def _check_value_size(self):
        """Checks to make sure the given value fits in the desired bit-size"""
        for value in self.value:
            if int(value) > (2**self._size) - 1:
                raise BitLengthError


class Ascii(ConversionValue):
    """ Ascii datatype inhierited from ConversionValue class
        Sets the value syntax to common form
        Checks value to fit in desired bit-size
        Creates _strtype to reference data type
        Alters __str__ method to display ascii characters without a space between them
    """
    def __init__(self, value: str, size=DEFAULT_BIT_SIZE):
        """Calls super().__init__()
            Sets _strtype to ascii
            Normalizes value syntax
            Checks value size
        """
        ConversionValue.__init__(self, value, size)
        self._strtype = "ascii"
        self._reset_value()
        self._check_value_size()

    def __str__(self) -> str:
        """When an instance of this class is called by itself, it will display it's self.value as a string with no spaces"""
        return ''.join(self.value)

    def _reset_value(self):
        """Converts given self.value to a common syntax"""
        if type(self.value) == str:
            self.value = [value for value in self.value]

    def _check_value_size(self):
        """Checks to make sure the given value fits in the desired bit-size"""
        for value in self.value:
            if len(value) > 1:
                raise BitLengthError


if __name__ == '__main__':
    pass

    