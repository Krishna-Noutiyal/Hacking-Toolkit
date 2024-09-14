import hashlib as hs
from pathvalidate import sanitize_filepath, ValidationError
from os import path


class hash:
    objects = []

    def __init__(self) -> None:
        """
        \nThis class implements the hash algorithm
        \nfor strings, files etc
        \n\nFirst you will need to create a hasher and then give it some input
        \n\thasher = hash()
        \n\thasher.text("Enter a String")
        \nAfter which you can call hasher.md5 to get md5 hash or .sha1 etc...

        \n\nThe Class have 5 variables
        \nhashText is the text being hashed
        \nby default the hastText = "text"
        \n\nYou can update hashText by using .text() method
        """
        self.__class__.objects.append(self)
        self.hashText = "text"
        self.md5 = self._md5()
        self.sha1 = self._sha1()
        self.sha256 = self._sha256()
        self.sha512 = self._sha512()

    def text(self, hashtext=str):
        """Updates the text to be Hashed"""
        self.hashText = hashtext
        return self

    def _md5(self):
        """
        \nThis method hashes self.hashText using md5 algorithm
        \nreturns the md5 hast of self.hashText
        """
        try:
            hash = hs.md5(self.hashText.encode("utf-8")).hexdigest()
            return hash
        except:
            raise ValueError("The encoding of the text is not utf-8 !!")

    def _sha1(self):
        """
        \nThis method hashes self.hashText using sha1 algorithm
        \nreturns the sha1 hast of self.hashText
        """
        try:
            hash = hs.sha1(self.hashText.encode("utf-8")).hexdigest()
            return hash
        except:
            raise ValueError("The encoding of the text is not utf-8 !!")

    def _sha256(self):
        """
        \nThis method hashes self.hashText using sha256 algorithm
        \nreturns the sha256 hast of self.hashText
        """
        try:
            hash = hs.sha256(self.hashText.encode("utf-8")).hexdigest()
            return hash
        except:
            raise ValueError("The encoding of the text is not utf-8 !!")

    def _sha512(self):
        """
        \nThis method hashes self.hashText using sha512 algorithm
        \nreturns the sha512 hast of self.hashText
        """
        try:
            hash = hs.sha512(self.hashText.encode("utf-8")).hexdigest()
            return hash
        except:
            raise ValueError("The encoding of the text is not utf-8 !!")

    def sanatize_path(self, file_path):
        """Strips the filepath to remove any trailing characters
                Then seperates the drive and filepath and then sanatize the file path.
                After sanitization joins both the drive and filepath together
            ### Returns
            ``'"F:/Folder/subfolder"'`` -> ``"F:/Folder/subfolder"``
        """
        try:
            # Extract drive letter
            drive, path_without_drive = path.splitdrive(file_path.strip(r'"\n\' '))
            print(f"Drive: {drive} and Path: {path_without_drive}")
            # Sanitize the path without the drive letter using pathvalidate
            sanitized_path = sanitize_filepath(path_without_drive)

            # Concatenate the drive letter and sanitized path
            final_path = drive + sanitized_path

            return final_path
        except ValidationError as e:
            print(f"Validation error in file path: {e}")
            return None

    def hashfile(self, FilePath: str, hash_algorithm="md5", chunk=65536) -> str:
        """
        \nThis method hashed a whole file in md5 by default
        \nyou can give sha1, sha256, sha512 in hash_algorithm argument
        \n\nArguments:
        \n\tFilePath = raw string path to the file eg. r"Path\\to\\file"
        \n\nOptional Arguments :
        \n\tchunk = divides the whole file in chunks ( 64KB by default )
        """
        # Create a hash object for the specified algorithm
        if hash_algorithm not in hs.algorithms_available:
            raise ValueError(f"Hash algorithm {hash_algorithm} is not available.")

        hasher = hs.new(hash_algorithm)
        
        # Open the file in binary mode and read it in chunks
        with open(self.sanatize_path(FilePath), "rb") as file:
            while True:
                data = file.read(
                    chunk
                )  # Read 64KB at a time (adjust the chunk size as needed)
                if not data:
                    break
                hasher.update(data)
        # Get the hexadecimal representation of the hash
        file_hash = hasher.hexdigest()

        return file_hash


# print(f"Krishna in md5 : {hasher.md5}")
# print(f"Krishna in sha1 : {hasher.sha1}")
# print(f"Krishna in sha256 : {hasher.sha256}")
# print(f"Krishna in sha512 : {hasher.sha512}")

# hasher = hash()
# print(hasher.text("Helppp").md5)
# print(hasher.sha256)
# print(hasher.sha512)
