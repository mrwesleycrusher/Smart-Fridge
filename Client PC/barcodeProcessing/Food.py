'''Provide a class to store information on a food item being tracked by Fridgekeeper, and classes for exceptions.

    Class Foodstuff

    Init Function:
    __init__ - Create a new object from a barcode and a quantity (default 1.0)

    Del Function:
    __del__ - Delete object and all its members.

    Data Members:
    code - The raw barcode for a food item.
    name - The name of the item (how it would be written on a grocery list).
    quantity - The number of this item that is stored.

    Member Functions:
    lookup - Get name data for a given barcode.
    get_name - Accessor for name data member
    get_code - Accessor for code data member
    get_num - Accessor for quantity data member
    add_items - Add a given number to the quantity data member (default 1.0)
    remove_items - Subtract a given number to the quantity data member (default 1.0)

    Operators:
    __add__ - Add quantity data members, returning new object.
    __sub__ - Subtract quantity data members, returning new object.
    __iadd__ - Add quantity of right hand argument to left hand argument.
    __isub__ - Subtract quantity of right hand argument from left hand argument.
    __eq__ - True if code data members are equal.
    __ne__ - True if code data members are not equal.

    Exceptions (each its own class:

    NegativeError - Raise if quantity < 0.0.
    NoSuchCode - Raise if API call fails to produce a product
    BadLookup - Raise if API authentication fails'''

import requests
import re

class Foodstuff:
    #TODO: Add docstrings for members, classes, etc.
    #TODO: Replace Assertions with NegativeErrors
    #TODO: Consider moving away from overloading, as per Fluff's advice

    # global key = '1C80BFC893597FD1915C0611541EEBA1'

    # == and != match barcodes
    def __eq__(self, other):
        return self.code == other.code

    def __ne__(self, other):
        return not self == other

    # Add and subtract work solely on the quantity of items, and only on items that are equal
    # Negative quantities are not allowed
    def __add__(self, other):
        assert self == other
        return Foodstuff(self.code, self.quantity + other.quantity)

    def __sub__(self, other):
        assert self == other
        assert self.quantity >= other.quantity
        return Foodstuff(self.code, self.quantity - other.quantity)

    def __iadd__(self, other):
        assert self == other
        self.quantity += other.quantity
        return self

    def __isub__(self, other):
        assert self == other
        assert self.quantity >= other.quantity
        self.quantity -= other.quantity
        return self

    # Mutators for quantity
    def add_items(self, num=1.0):
        self.quantity += num

    def remove_items(self, num=1.0):
        self.quantity -= num

    # # Helper for formatting API responses
    # def format_response(text):
    #     newtext = text.strip('\"').strip('\:').strip('{}').split(',')
    #     return newtext

    #Helper for removing whitespace from name
    def remove_extra_chars(self):
        self.name = self.name.strip(' \r\n\t\\r\\n\\t')
    

    # API CALL CENTRAL
    def lookup(self,barcode):
        try:
            response = requests.get('https://api.upcdatabase.org/product/' + barcode +
                                    '/' + '1C80BFC893597FD1915C0611541EEBA1')
            status = response.status_code
            if status == 200:
                # Match title field in list and return corresponding name
                response_name = re.search('\"title\"\:\".*?\"', response.text)
                return response_name.group(0)[9:len(response_name.group())-1]
            elif status == 403:
                raise BadLookup
            else:
                raise NoSuchCode
        except BadLookup as err:
            print('Could not connect to UPC Database with key ' + '1C80BFC893597FD1915C0611541EEBA1')
            return 'BadLookup'
        except NoSuchCode as err:
            print('Could not find product for code: ' + barcode)
            return 'NoSuchCode'

    # Constructor. Optional argument for initializing with several food items
    def __init__(self, barcode, num=1.0):
        self.code = barcode
        self.name = self.lookup(barcode)
        self.remove_extra_chars()
        self.quantity = num

    # Destructor
    # def __del__(self):
    #     del self.code
    #     del self.name
    #     del self.quantity

    # Accessors
    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_num(self):
        return self.quantity

class NegativeError(Exception):
    pass

class NoSuchCode(Exception):
    pass

class BadLookup(Exception):
    pass
