class string:
    """
    \nThis is a String class that performs different operations on string
    \nTo create an object you will need to provide a list of strings
    \nAfter which you can use the Features provided by the Class

    \n\nYou can also use some functions which doesn't require you to create any objects
    \nThey are :
    \n\tstring_To_Int
    \n\sStr_To_Hex
    \n\sStr_To_Bytes
    \n\sStr_To_Bits
    """

    objects = []

    def __init__(self, StringList=[]) -> None:
        self.__class__.objects.append(self)
        self.strings = StringList
        self.byteStr = []
        self.similar = False

        self.remove_space_left_right()
        self.issame()

    def checkEmpty(self):
        """Checks if String List is Empty"""

        if len(self.strings) == 0:
            raise ValueError("Empty string")

    def issame(self):
        """Checks if strings are similar to each other"""
        self.checkEmpty()
        self.remove_space_left_right()  # Before Checking clears the left and right junk ins strings

        strlist = self.strings
        for i in range(0, len(strlist)):
            try:
                if strlist[i] != strlist[i + 1]:
                    return False
            except IndexError:
                continue
        return True

    def remove_space_left_right(self):
        """
        \nRemoves spaces and special characters from the end of the strings and
        \nstores them back to self.strings
        """
        self.checkEmpty()

        strlist = self.strings
        temp = strlist.copy()

        strlist.clear()

        for i in temp:
            strlist.append(i.strip())
        return strlist

    @classmethod
    def string_To_Int(cls, text:str):
        """
        \nChecks if the String only contains Numeric characters
        \nIf Yes, returns an integer
        \nElse returns the same string
        """
        text = text.strip()
        if isinstance(text, str):
            if text.isnumeric():
                return int(text)
            else:
                return text
        else:
            raise TypeError("Only String is allowed")

    @classmethod
    def str_To_Hex(cls, text:str, seperator=True) -> str:
        """
        \nSet sperator = False to remove spaces from the output hex representation !!
        \nConverts Given text into Hex
        \nFeature of the Function is that if the give string consists of only numbers
        \nThe Function automaticaly converts the given string into int and then
        \nReturns the Hex representation of that int
        """

        # Stores the text in string or int form
        text = cls.string_To_Int(text)

        if isinstance(text, str):
            str_Rep_with_Spaces = " ".join([hex(ord(char))[2:] for char in text])

            return (
                str_Rep_with_Spaces
                if seperator == True
                else str_Rep_with_Spaces.replace(" ", "")
            )

        else:
            hex_string = hex(text)[2:]
            str_Rep_with_Spaces = " ".join(
                [hex_string[i : i + 2] for i in range(0, len(hex_string), 2)]
            )

            return (
                str_Rep_with_Spaces
                if seperator == True
                else str_Rep_with_Spaces.replace(" ", "")
            )

    @classmethod
    def str_To_Bytes(cls, text:str) -> str:
        """
        \nConverts Given text into Bytes
        \nFeature of the Function is that if the give string consists of only numbers
        \nThe Function automaticaly converts the give string into int and then
        \nReturns the Bytes representation of that int
        """

        # Stores the text in string or int form
        text = cls.string_To_Int(text)

        if isinstance(text, str):
            return " ".join([bin(ord(char))[2:].zfill(8) for char in text])
        else:
            binary_string = bin(text)[2:]
            return " ".join(
                [
                    binary_string[i : i + 8].zfill(8)
                    for i in range(0, len(binary_string), 8)
                ]
            )

    @classmethod
    def str_To_Bits(cls, text:str) -> str:
        """
        \nConverts Given text into Bits
        \nFeature of the Function is that if the give string consists of only numbers
        \nThe Function automaticaly converts the give string into int and then
        \nReturns the Bits representation of that int
        """

        # Stores the text in string or int form
        text = cls.string_To_Int(text)

        if isinstance(text, str):
            return "".join([bin(ord(char))[2:] for char in text])
        else:
            binary_string = bin(text)[2:]
            return binary_string

    @classmethod
    def hex_To_Int_Or_String(cls, hex_string=str) -> tuple:
        """
        \nTakes a hex string as input and returns a tuple
        \nThe tuple contents are as follows:
        \n\t1) String Value : Hex converted to string
        \n\t2) Int Value : Hex converted to integer
        """
        # Remove spaces and junk char from the input string, if any
        hex_string = ''.join(filter(lambda char: char in '0123456789ABCDEFabcdef', hex_string))
        
        try:
            # Int Conversions of Hex
            int_value = int(hex_string, 16)
            str_value = None
            # String Conversion of Hex
            byte_data = bytes.fromhex(hex_string)
            str_value = byte_data.decode("utf-8")
        except:
            pass
        
        return (str_value,int_value)


# q = 1

# while q==1:
        
#     a = string.str_To_Hex(input("\n\nEnter a String : "),False)
#     print("\n\nHexadecimal Representation : {}".format(a))

#     b = string.hex_To_Int_Or_String(a)
#     print("String Representation : {}".format(b))


#     q = int(input("\nPress 1 to continue or 0 to quit  : "))
