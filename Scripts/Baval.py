from cryptography.fernet import Fernet as f

import base64
import os
import typing
import binascii
from time import time
class bvl(f):
    """
    \nThis is a wrapper class for the Fernet Class in cryptography package
    \nIt provides a simple way to encrypt and decrypt data or files
    \n
    \n## Example Usage
    \n
    \nTo Use this class, you will need to create an object of the class and then use the methods of the class
    \n
    \nExample:
    ```
    # Initalize the class
    bvl = bvl(bvl.generate_key(bites = 256))
    
    # To encrypt a file
    bvl.encrypt_file(path)
    
    # To decrypt a file
    bvl.decrypt_file(path)
    ```
    \n## Features:
    \n\t- Encrypts and Decrypts data or files
    \n\t- Has a simple API
    \n\t- Can be used with the default key or a custom key
    \n\t- Can be used to encrypt or decrypt data or files

    \n\n## Methods:
    \n\t- encrypt(data) : Encrypts data with the key
    \n\t- decrypt(data) : Decrypts data with the key
    \n\t- encrypt_file(path,save_key=False) : Encrypts a file and returns the encryption key
    \n\t- decrypt_file(path) : Decrypts a file and returns the decryption key
    """
    def __init__(
        self,
        key: typing.Union[bytes, str],
    ) -> None:
        self.key = key
        try:
            key = base64.urlsafe_b64decode(key)
        except binascii.Error as exc:
            raise ValueError(
                "bvl key must be a 32,64 bit key url-safe base64-encoded bytes."
            ) from exc
        if len(key) not in [32,64]:
            raise ValueError(
                "bvl key must be a 32,64 bit key url-safe base64-encoded bytes."
            )

        self._signing_key = key[:int(len(key)/2)]
        self._encryption_key = key[int(len(key)/2):]

    def encrypt_file(self,path:str,save_key=False) -> float:
        """
        \nEncryptes a file and returns the encryption key
        \n\tInputs:
        \n\t\tpath: File to be encrypted
        \n\t\tsave_key: Whether to save the encryption key in a file in same path
        \n\n\tReturns:
        \n\t\tTime Took To Encrypt
        """
        if save_key:
            with open(os.path.dirname(path)+"\\encryptionkey.key","wb") as key_file:
                key_file.write(self.get_key())

        s_time = time()
        with open(path, "rb") as file:
            data = file.read()

        encrypted_data = self.encrypt(data)

        with open(path,"wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        return time() - s_time

    def decrypt_file(self,path:str) -> str:
        """
        \nEncryptes a file and returns the encryption key
        \n\tInputs:
        \n\t\tpath: File to be decrypted
        \n\n\tReturns:
        \n\t\tTime Took to Decrypt
        \n# NOTE
        \n##### The function takes the default key given when creating the class object
        \n##### You need to give the same key by which the file was encrypted else
        \n##### Decryption is not possible
        """

        s_time = time()

        with open(path, "rb") as file:
            encrypted_data = file.read()

        original_data = self.decrypt(encrypted_data)

        with open(path,"wb") as original_file:
            original_file.write(original_data)

        return time() - s_time

    @classmethod
    def generate_key(cls,bites = 256) -> bytes:
        """
        Generates a key of given bits
        Args:
            bites (int): The number of bits for the key, Defaults to 256
        Returns:
            bytes: The generated key

        Important:
        **To encrypt or decrypt data or file, this class uses utmost 512 bit key**
        **so createing a key that's beyond that is not necessary !!**

        """

        byte = int(bites/8)

        return base64.urlsafe_b64encode(os.urandom(byte))

    def get_key(self):
        return self.key

test = bvl(bvl.generate_key())