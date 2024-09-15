from pathlib import Path
from tkinter import (
    Tk,
    Canvas,
    Entry,
    Text,
    Button,
    PhotoImage,
    messagebox,
    Label,
    StringVar,
)
from Scripts.Hash import hash

"""
ToDo:


Add Select File button in Hash Panel
Update the 64 bit and 128 bit keys button to 256 and 512 bit respectively
"""


def gethash(Canvas, tag, text, algorithm):
    """
    ## Working
    \nThe function hashes the given text and then configures the
    \ntext value of canvase item with specified tag
    ## Input
    \nNeeds 3 arguments
    \n\tCanvas : The current running canvas
    \n\tTag : The Tag of the canvas text that need to be edited
    \n\ttext : The text to be Hashed
    \n\talgorithm : The algorithm to be used to hash the text (md5,sha1,sha256,sha512)
    ### How the canvase item is configured
    \nAfter getting the hash for the given text
    \nIf the text is more then 256 characters long then it breaks it into two parts
    \nand adds a new line character in between
    """
    # Hasher to Hash the Entry Value
    hasher = hash()
    hasher.text(text)
    if algorithm == "md5":
        value = hasher._md5()
        Canvas.itemconfig(tag, text=value)

    elif algorithm == "sha1":
        value = hasher._sha1()
        Canvas.itemconfig(tag, text=value)

    elif algorithm == "sha256":
        value = hasher._sha256()
        Canvas.itemconfig(tag, text=value)

    elif algorithm == "sha512":
        hash_value = hasher._sha512()
        value = hash_value[:64] + "\n" + hash_value[64:]
        print(hash_value)
        print(value)
        Canvas.itemconfig(tag, text=value)


def getfilehash(Canvas, tag: str, filepath: str, algorithm: str):
    """
## Working
    \nThe function hashes a given file and then configures the
    \ntext value of canvase item with specified tag
## Input
    \nNeeds 3 arguments
    \n\tCanvas : The current running canvas
    \n\tTag : The Tag of the canvas text that need to be edited
    \n\ttext : The text to be Hashed
    \n\talgorithm : The algorithm to be used to hash the text (md5,sha1,sha256,sha512)
### How the canvase item is configured
    \nAfter getting the hash for the given text
    \nIf the text is more then 256 characters long then it breaks it into two parts
    \nand adds a new line character in between
    """
    # Hasher to Hash the Entry Value
    hasher = hash()
    algorithm = algorithm.lower()

    if algorithm == "md5":
        value = hasher.hashfile(filepath, "md5")
        Canvas.itemconfig(tag, text=value)

    elif algorithm == "sha1":
        value = hasher.hashfile(filepath, "sha1")
        Canvas.itemconfig(tag, text=value)

    elif algorithm == "sha256":
        value = hasher.hashfile(filepath, "sha256")
        Canvas.itemconfig(tag, text=value)

    elif algorithm == "sha512":
        hash_value = hasher.hashfile(filepath, "sha512")
        value = hash_value[:64] + "\n" + hash_value[64:]
        print(hash_value)
        print(value)
        Canvas.itemconfig(tag, text=value)

# Don't Change these variables hex_conersion and str_conversion will use them in the Strings Panel
str_to_hex_value = ""
str_to_Bytes_value = ""
str_to_Bits_value = ""

hex_to_str_value = ""
hex_to_int_value = ""


def hex_conversion(Canvas, text: str) -> None:
    """
    This fucntion is to use with the **Strings Panel** it takes the present canvas and the hex text
    present in the hex_conversion_entry and updates the following value you see on Strings Panel :
    \n
        1) Int Values (tag: hextoint)
        2) Str Value (tag: hextostr)

    The converted strings can overflow the canvas thus, the value is truncated to 20 characters
    for copy to clipboard purpose it updates the following global variables :
    \n
        1) hex_to_int_value
        2) hex_to_str_value


    **So, you can pass these variables to copyToClipboard() function to copy the value to clipboard.**
    """
    from Scripts.Strings import string

    global hex_to_str_value
    global hex_to_int_value

    int_value = string.hex_To_Int_Or_String(text)[1]
    str_value = string.hex_To_Int_Or_String(text)[0]

    hex_to_int_value = str(int_value)
    hex_to_str_value = str(str_value)

    try:

        Int_text = (
            int_value if (len(str(int_value)) < 20) else str(int_value)[:20] + " ..."
        )
    except:
        Int_text = "Error"
    try:
        Str_text = str_value if (len(str_value) < 20) else str_value[:20] + " ..."
    except:
        Str_text = "Error"

    Canvas.itemconfig("hextoint", text=Int_text)
    Canvas.itemconfig("hextostr", text=Str_text)


def str_conversion(Canvas, text: str) -> None:
    """
    This fucntion is to use with the **Strings Panel** it takes the present canvas and the text
    present in the string_conversion_entry and updates the following value you see on Strings Panel :
    \n
        1) Hex Values (tag: Hex)
        2) Bytes Value (tag: Bytes)
        3) Bits Value (tag: Bits)

    The converted strings can overflow the canvas thus, the value is truncated to 40 characters
    for copy to clipboard purpose it updates the following global variables :
    \n
        1) str_to_hex_value
        2) str_to_Bytes_value
        3) str_to_Bits_value

    **So, you can pass these variables to copyToClipboard() function to copy the value to clipboard.**
    """
    from Scripts.Strings import string

    global str_to_hex_value
    global str_to_Bits_value
    global str_to_Bytes_value

    hex_value = string.str_To_Hex(text)
    bytes_value = string.str_To_Bytes(text)
    bits_value = string.str_To_Bits(text)

    str_to_hex_value = hex_value
    str_to_Bytes_value = bytes_value
    str_to_Bits_value = bits_value

    Hex_text = hex_value if (len(hex_value) < 40) else hex_value[:40] + " ..."

    Bytes_text = bytes_value if (len(bytes_value) < 40) else bytes_value[:40] + " ..."

    Bits_text = bits_value if (len(bits_value) < 40) else bits_value[:40] + " ..."

    Canvas.itemconfig("Hex", text=Hex_text)
    Canvas.itemconfig("Bytes", text=Bytes_text)
    Canvas.itemconfig("Bits", text=Bits_text)


def check_str(Canvas, *args : str) -> None:
    """
    This function works witht he Strings Panel and checks the 5 entry boxes
    and updates the **True** or **False** value in the Strings Panel
    """
    from Scripts.Strings import string

    text_list = [i for i in args if i]  # Remove empty strings

    stinger = string(text_list)
    if stinger.issame():
        Canvas.itemconfig("trueorfalse", text="True")
    else:
        Canvas.itemconfig("trueorfalse", text="False")
    print(text_list)

def get_key(Canvas, type=256) -> None:
    """
    This function works with the F-crypt Panel and updates the **keyvalue** tag in the canvas
    Args:
        type(int, optional): The number of bits for the key, Defaults to 256 bits
    """

    from Scripts.Baval import bvl
    bvl = bvl(bvl.generate_key(type))
    
    key = bvl.get_key()

    # Update the key in the canvas
    Canvas.itemconfig("keyvalue", text=key)

class app:
    def __init__(self) -> None:
        """Toolkit Class"""
        self.window = Tk()
        self.window.geometry("1445x813")
        self.window.configure(bg="#053B50")
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./assets")

        self.build_Menu()

    def copyToClipboard(self, text):
        """\nCopies the given text to clipboard and returns True
        \nRemoves any \\n characters from the text
        """
        try:

            text = text.replace("\n", "")
        except:
            pass
        self.window.clipboard_clear()
        self.window.clipboard_append(text)

        print("Copied to clipboard : " + text)

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def destroy(self, frame):
        """
        \nInput:
        \n\tframe: int (used to call a build function that creates the windows for a given frame)
        \n## Frames:
        \n\t Menu: 1
        \n\t Strings: 2
        \n\t Hash: 3
        \n\t Fcrypt: 4
        \n\t Sub-Domber: 5 (Not implemented)
        \n### Output
        \n\tRemoves all the children and calls another build function for creating the specified frame

        """
        if frame in (1, 2, 3, 4):
            for i in self.window.winfo_children():
                i.destroy()
        else:
            messagebox.showerror(
                "Sub-Domber Not Available",
                "Sub-Domber is not yet implemented Please be Patient :)",
            )
        if frame == 1:
            self.build_Menu()
        elif frame == 2:
            self.build_String()
        elif frame == 3:
            self.build_Hash()
        elif frame == 4:
            self.build_Fcrypt()

    def build_Menu(self):
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./assets/menu_panel")

        canvas = Canvas(
            self.window,
            bg="#053B50",
            height=813,
            width=1445,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(x=0, y=0)
        canvas.create_text(
            453.0,
            7.0,
            anchor="nw",
            text="ToolKit",
            fill="#EEEEEE",
            font=("JetBrains Mono", 128 * -1, "bold"),
        )

        button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(3),
            relief="flat",
        )
        button_1.place(x=454.0, y=182.0, width=536.3670654296875, height=105.0)

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(2),
            relief="flat",
        )
        button_2.place(x=454.0, y=337.0, width=536.3670654296875, height=105.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(4),
            relief="flat",
        )
        button_3.place(x=454.0, y=491.0, width=536.3670654296875, height=105.0)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(5),
            relief="flat",
        )
        button_4.place(x=454.0, y=628.0, width=536.3670654296875, height=105.0)

        canvas.create_text(
            1000.0,
            658.0,
            anchor="nw",
            text="(Not Implemented)",
            fill="#b3b0b0",
            font=("JetBrains Mono", 32 * -1, "bold"),
        )

        self.window.mainloop()

    def build_Hash(self):
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(
            r"./assets/hashing_panel"
        )

        canvas = Canvas(
            self.window,
            bg="#053B50",
            height=813,
            width=1445,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        # Entery Variables
        string_entry_var = StringVar(self.window)
        file_entry_var = StringVar(self.window)

        # Entries
        string_entry = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=string_entry_var,
        )

        string_entry_Image = PhotoImage(file=self.relative_to_assets("entry_1.png"))

        string_entry.place(
            x=420.1837158203125,
            y=214.88853454589844,
            width=605.2891845703125,
            height=19.0,
        )

        canvas.create_image(
            722.8283081054688, 225.38853454589844, image=string_entry_Image
        )

        file_entry = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=file_entry_var,
        )
        file_entry_image = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        canvas.create_image(
            724.6285400390625, 533.7057952880859, image=file_entry_image
        )

        file_entry.place(
            x=312.2752685546875,
            y=521.3884887695312,
            width=824.70654296875,
            height=22.634613037109375,
        )

        canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(722.0, 290.0, image=image_image_1)

        image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(723.0, 609.0, image=image_image_2)

        # String Hash and Its Value
        canvas.create_text(
            420.0,
            337.0,
            anchor="nw",
            text=r"Hash:",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
        )

        canvas.create_text(
            500.0,
            343.0,
            anchor="nw",
            text="",
            fill="#FFFFFF",
            font=("JetBrains Mono", 14 * -1, "bold"),
            tags="stringhash",
        )

        # File hash and Its Value
        canvas.create_text(
            320.0,
            665.0,
            anchor="nw",
            text=r"File Hash:",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
        )

        canvas.create_text(
            470.0,
            672.0,
            anchor="nw",
            text=r"asdf198/*$sdasf%s133",
            fill="#FFFFFF",
            font=("JetBrains Mono", 14 * -1, "bold"),
            tags="filehash",
        )

        # canvas.itemcget() : Gets the Value of specified option from a tag or id
        # self.copyToClipboard : Saves the returned value to the clipboard
        canvas.tag_bind(
            "stringhash",
            "<Button-1>",
            lambda event, canvas=canvas: self.copyToClipboard(
                canvas.itemcget("stringhash", "text")
            ),
        )
        canvas.tag_bind(
            "filehash",
            "<Button-1>",
            lambda event, canvas=canvas: self.copyToClipboard(
                canvas.itemcget("filehash", "text")
            ),
        )

        image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            721.479248046875, 224.88853454589844, image=image_image_3
        )

        image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(
            722.97802734375, 534.00390625, image=image_image_4
        )

        # md5 text button
        md5_button_image_string = PhotoImage(
            file=self.relative_to_assets("button_1.png")
        )
        md5_string = Button(
            image=md5_button_image_string,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gethash(canvas, "stringhash", string_entry.get(), "md5"),
            relief="flat",
        )
        md5_string.place(x=552.0, y=263.0, width=70.0, height=45.0)

        # md5 file button
        md5_button_image_file = PhotoImage(file=self.relative_to_assets("button_2.png"))
        md5_file = Button(
            image=md5_button_image_file,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: getfilehash(canvas, "filehash", file_entry.get(), "md5"),
            relief="flat",
        )
        md5_file.place(
            x=488.0,
            y=583.0,
            width=95.375,
            height=52.7884521484375,
        )

        # SHA1 text button
        sha1_button_image_string = PhotoImage(
            file=self.relative_to_assets("button_3.png")
        )
        sha1_string = Button(
            image=sha1_button_image_string,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gethash(canvas, "stringhash", string_entry.get(), "sha1"),
            relief="flat",
        )
        sha1_string.place(x=643.0, y=263.0, width=70.0, height=45.0)

        # SHA1 file button
        sha1_button_image_file = PhotoImage(
            file=self.relative_to_assets("button_4.png")
        )
        sha1_file = Button(
            image=sha1_button_image_file,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: getfilehash(canvas, "filehash", file_entry.get(), "sha1"),
            relief="flat",
        )
        sha1_file.place(
            x=611.9874267578125,
            y=583.0,
            width=95.375,
            height=52.7884521484375,
        )

        # S256 text button
        sha256_button_image_string = PhotoImage(
            file=self.relative_to_assets("button_5.png")
        )
        sha256_string = Button(
            image=sha256_button_image_string,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gethash(canvas, "stringhash", string_entry.get(), "sha256"),
            relief="flat",
        )
        sha256_string.place(x=734.0, y=263.0, width=70.0, height=45.0)

        # S256 file button
        sha256_button_image_file = PhotoImage(
            file=self.relative_to_assets("button_6.png")
        )
        sha256_file = Button(
            image=sha256_button_image_file,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: getfilehash(canvas, "filehash", file_entry.get(), "sha256"),
            relief="flat",
        )
        sha256_file.place(
            x=735.9749755859375,
            y=583.0,
            width=95.375,
            height=52.7884521484375,
        )

        # S512 text button
        sha512_button_image_string = PhotoImage(
            file=self.relative_to_assets("button_7.png")
        )
        sha512_string = Button(
            image=sha512_button_image_string,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gethash(canvas, "stringhash", string_entry.get(), "sha512"),
            relief="flat",
        )
        sha512_string.place(
            x=825.0,
            y=263.0,
            width=70.0,
            height=45.0,
        )

        # S512 file button
        sha512_button_image_file = PhotoImage(
            file=self.relative_to_assets("button_8.png")
        )
        sha512_file = Button(
            image=sha512_button_image_file,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: getfilehash(canvas, "filehash", file_entry.get(), "sha512"),
            relief="flat",
        )
        sha512_file.place(
            x=859.9625244140625,
            y=583.0,
            width=95.375,
            height=52.7884521484375,
        )

        canvas.create_text(
            607.0,
            15.0,
            anchor="nw",
            text="Hash",
            fill="#EEEEEE",
            font=("JetBrains Mono", 96 * -1, "bold"),
        )

        button_image_11 = PhotoImage(file=self.relative_to_assets("button_11.png"))
        button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(1),
            relief="flat",
        )
        button_11.place(x=37.0, y=34.0, width=150.0, height=71.0)

        button_image_12 = PhotoImage(file=self.relative_to_assets("button_12.png"))
        button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(2),
            relief="flat",
        )
        button_12.place(x=1300.0, y=290.0, width=118.0, height=70.0)

        button_image_13 = PhotoImage(file=self.relative_to_assets("button_13.png"))
        button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(4),
            relief="flat",
        )
        button_13.place(x=1300.0, y=375.0, width=118.0, height=70.0)

        button_image_14 = PhotoImage(file=self.relative_to_assets("button_14.png"))
        button_14 = Button(
            image=button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(5),
            relief="flat",
        )
        button_14.place(x=1300.0, y=460.0, width=118.0, height=70.0)

        self.window.mainloop()

    def build_String(self):
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(
            r"./assets/strings_panel"
        )
        canvas = Canvas(
            self.window,
            bg="#053B50",
            height=813,
            width=1445,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(307.0, 416.8606872558594, image=image_image_1)

        canvas.create_rectangle(157.0, 474.0, 454.0, 479.0, fill="#E0E5E7", outline="")

        image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(308.0, 270.0, image=image_image_2)

        image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(308.0, 326.0, image=image_image_3)

        image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(308.0, 382.0, image=image_image_4)

        image_image_5 = PhotoImage(file=self.relative_to_assets("image_5.png"))
        image_5 = canvas.create_image(308.0, 438.0, image=image_image_5)

        # Similar String Entries
        # The entries are not in order okey
        entry_1_var = StringVar(self.window)
        entry_2_var = StringVar(self.window)
        entry_3_var = StringVar(self.window)
        entry_4_var = StringVar(self.window)
        entry_5_var = StringVar(self.window)

        string_conversion_entry_var = StringVar(self.window)
        hex_conversion_entry_var = StringVar(self.window)

        # From entry 5 to entry 1 : Check Similar Strings
        # Order of the entries
        # entrylst = [entry_5_var,entry_1_var,entry_2_var,entry_3_var,entry_4_var,entry_6_var,entry_7_var,]

        entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = canvas.create_image(
            306.62701416015625, 213.2492218017578, image=entry_image_5
        )
        entry_5 = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=entry_5_var,
        )
        entry_5.place(
            x=135,
            y=203,
            width=346.75,
            height=21,
        )

        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            306.62701416015625, 269.5154724121094, image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=entry_1_var,
        )
        entry_1.place(
            x=135,
            y=259,
            width=346.7459716796875,
            height=21,
        )

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            306.62701416015625, 325.78173828125, image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=entry_2_var,
        )
        entry_2.place(x=135, y=316, width=346.7459716796875, height=21)

        entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(
            306.62701416015625, 382.0479736328125, image=entry_image_3
        )
        entry_3 = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=entry_3_var,
        )
        entry_3.place(x=135, y=372, width=346.7459716796875, height=21)

        entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(
            306.62701416015625, 438.3142395019531, image=entry_image_4
        )
        entry_4 = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=entry_4_var,
        )
        entry_4.place(
            x=135,
            y=428,
            width=346.7459716796875,
            height=19.0,
        )

        # Background Colors using Images
        image_image_8 = PhotoImage(file=self.relative_to_assets("image_8.png"))
        image_8 = canvas.create_image(915.0, 324.0, image=image_image_8)

        image_image_9 = PhotoImage(file=self.relative_to_assets("image_9.png"))
        image_9 = canvas.create_image(
            914.479248046875, 212.88853454589844, image=image_image_9
        )

        image_image_10 = PhotoImage(file=self.relative_to_assets("image_10.png"))
        image_10 = canvas.create_image(914.0, 642.0, image=image_image_10)

        image_image_11 = PhotoImage(file=self.relative_to_assets("image_11.png"))
        image_11 = canvas.create_image(915.0, 606.0, image=image_image_11)

        # String to Hex, Bytes, Bits
        string_conversion_entry_image = PhotoImage(
            file=self.relative_to_assets("entry_6.png")
        )
        string_conversion_entry_bg = canvas.create_image(
            915.8283081054688, 213.38853454589844, image=string_conversion_entry_image
        )
        string_conversion_entry = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=string_conversion_entry_var,
        )
        string_conversion_entry.place(
            x=613.1837158203125,
            y=202.88853454589844,
            width=605.2891845703125,
            height=19.0,
        )

        # Convert Button
        convert_button_image = PhotoImage(file=self.relative_to_assets("button_1.png"))
        convert_button = Button(
            image=convert_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: str_conversion(canvas, string_conversion_entry.get()),
            relief="flat",
        )
        convert_button.place(
            x=798.0,
            y=244.0,
            width=233.453369140625,
            height=51.21671676635742,
        )

        # Hex and its Value
        canvas.create_text(
            613.472900390625,
            324.1393127441406,
            anchor="nw",
            text="Hex:",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
        )

        canvas.create_text(
            680,
            330,
            anchor="nw",
            text="4a f5 e9 07",
            fill="#FFFFFF",
            font=("JetBrains Mono", 16 * -1),
            tags="Hex",
        )

        # Bytes and its Value
        canvas.create_text(
            613.472900390625,
            372.1393127441406,
            anchor="nw",
            text="Bytes:",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
        )

        canvas.create_text(
            710.472900390625,
            378,
            anchor="nw",
            text="11100010 11110100 01110100 01010100",
            fill="#FFFFFF",
            font=("JetBrains Mono", 16 * -1),
            tags="Bytes",
        )

        # Bits and its Value
        canvas.create_text(
            613.472900390625,
            420.1393127441406,
            anchor="nw",
            text="Bits:",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
        )

        canvas.create_text(
            695,
            427,
            anchor="nw",
            text="111000101111010001110100010101000111",
            fill="#FFFFFF",
            font=("JetBrains Mono", 16 * -1),
            tags="Bits",
        )

        # Copy to Clipboard Hex, Bits and Bytes
        canvas.tag_bind(
            "Hex",
            "<Button-1>",
            lambda event, canvas=canvas: self.copyToClipboard(str_to_hex_value),
        )
        canvas.tag_bind(
            "Bits",
            "<Button-1>",
            lambda event, canvas=canvas: self.copyToClipboard(str_to_Bits_value),
        )

        canvas.tag_bind(
            "Bytes",
            "<Button-1>",
            lambda event, canvas=canvas: self.copyToClipboard(str_to_Bytes_value),
        )

        # Hex To Int,String
        hex_conversion_entry_image = PhotoImage(
            file=self.relative_to_assets("entry_7.png")
        )
        hex_conversion_entry_bg = canvas.create_image(
            917.0, 606.879150390625, image=hex_conversion_entry_image
        )
        hex_conversion_entry = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 24 * -1, "bold"),
            textvariable=hex_conversion_entry_var,
        )
        hex_conversion_entry.place(
            x=700.0, y=588.3198852539062, width=434.0, height=35.1185302734375
        )

        # Updateing Int and Str values in Hex Conversion for any update in hex_conersion_entry
        hex_conversion_entry_var.trace_add(
            "write",
            lambda name, index, mode, canvas=canvas: hex_conversion(
                canvas, hex_conversion_entry_var.get()
            ),
        )

        image_image_6 = PhotoImage(file=self.relative_to_assets("image_6.png"))
        image_6 = canvas.create_image(308.0, 213.0, image=image_image_6)

        image_image_7 = PhotoImage(file=self.relative_to_assets("image_7.png"))
        image_7 = canvas.create_image(
            307.4228210449219, 603.9876098632812, image=image_image_7
        )

        # Similar Text
        canvas.create_text(
            168.0,
            584.0,
            anchor="nw",
            text="Similar :",
            fill="#000000",
            font=("JetBrains Mono", 32 * -1, "bold"),
        )

        # True or False Text
        canvas.create_text(
            352.0,
            584.0,
            anchor="nw",
            text="False",
            fill="#E52D2D",
            font=("JetBrains Mono", 32 * -1, "bold"),
            tags="trueorfalse",
        )

        # Strings
        canvas.create_text(
            521.0,
            15.0,
            anchor="nw",
            text="Strings",
            fill="#EEEEEE",
            font=("JetBrains Mono", 96 * -1, "bold"),
        )

        # HEX To Int/String
        canvas.create_text(
            753.0,
            532.0,
            anchor="nw",
            text="HEX To Int/String",
            fill="#FFFFFF",
            font=("JetBrains Mono", 32 * -1, "bold"),
        )

        # Int : 4568
        canvas.create_text(
            674.0,
            642.0,
            anchor="nw",
            text="Int:",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
        )
        canvas.create_text(
            740.0,
            642.0,
            anchor="nw",
            text="4568",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
            tags="hextoint",
        )

        # Str : Hello
        canvas.create_text(
            673.0,
            688.0,
            anchor="nw",
            text="Str:",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
        )
        canvas.create_text(
            740.0,
            688.0,
            anchor="nw",
            text="Hello",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
            tags="hextostr",
        )

        canvas.tag_bind(
            "hextoint",
            "<Button-1>",
            lambda event, canvas=canvas: self.copyToClipboard(hex_to_int_value),
        )
        canvas.tag_bind(
            "hextostr",
            "<Button-1>",
            lambda event, canvas=canvas: self.copyToClipboard(hex_to_str_value),
        )

        button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(1),
            relief="flat",
        )
        button_2.place(x=37.0, y=34.0, width=150.0, height=71.0)

        # Check Button
        check_str_button_image = PhotoImage(
            file=self.relative_to_assets("button_3.png")
        )
        check_str_button = Button(
            image=check_str_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: check_str(canvas, entry_1_var.get(), entry_2_var.get(), entry_3_var.get(), entry_4_var.get(), entry_5_var.get()),
            relief="flat",
        )
        check_str_button.place(
            x=189.0, y=490.0, width=233.45333862304688, height=51.216705322265625
        )

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(3),
            relief="flat",
        )
        button_4.place(x=1300.0, y=290.0, width=118.0, height=70.0)

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(4),
            relief="flat",
        )
        button_5.place(x=1300.0, y=375.0, width=118.0, height=70.0)

        button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(5),
            relief="flat",
        )
        button_6.place(x=1300.0, y=460.0, width=118.0, height=70.0)

        self.window.mainloop()

    def build_Fcrypt(self):
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(
            r"./assets/fcrypt_panel"
        )
        canvas = Canvas(
            self.window,
            bg="#053B50",
            height=813,
            width=1445,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(723.0, 289.0, image=image_image_1)

        image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(722.0, 612.0, image=image_image_2)

        # Key Text
        canvas.create_text(
            479.0,
            284.0,
            anchor="nw",
            text="Key:",
            fill="#FFFFFF",
            font=("JetBrains Mono", 24 * -1, "bold"),
        )
        # Key value
        canvas.create_text(
            550.0,
            288.0,
            anchor="nw",
            text="asdfsdffsd6561$2342346",
            fill="#FFFFFF",
            font=("JetBrains Mono", 18 * -1, "bold"),
            tags="keyvalue"
        )

        image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(722.0, 514.00390625, image=image_image_3)

        image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(638, 568.0, image=image_image_4)

        # Entrie Variables

        entry_1_var = StringVar(self.window, "Encryption Key")
        entry_2_var = StringVar(self.window, "Select a File")

        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            722.353271484375, 513.7057952880859, image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=entry_1_var

        )
        entry_1.place(
            x=310.0,
            y=501.38848876953125,
            width=824.70654296875,
            height=22.634613037109375,
            
        )

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            722.353271484375, 567.7018899917603, image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#053B50",
            fg="#EEEEEE",
            highlightthickness=0,
            font=("JetBrains Mono", 16 * -1, "bold"),
            textvariable=entry_2_var
        )
        entry_2.place(
            x=310.0,
            y=555.3845825195312,
            width=660,
            height=22.634614944458008

        )

        button_64_image = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_64_bit = Button(
            image=button_64_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: get_key(canvas,256),
            relief="flat",
        )
        button_64_bit.place(x=521.0, y=180.0, width=185.0, height=55.0)

        button_128_bit_image = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_128_bit = Button(
            image=button_128_bit_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: get_key(canvas,512),
            relief="flat",
        )
        button_128_bit.place(x=737.0, y=180.0, width=185.0, height=55.0)

        button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat",
        )
        button_3.place(x=630.0, y=346.0, width=185.0, height=55.0)

        button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat",
        )
        button_4.place(x=613.0, y=681.0, width=220.0, height=75.0)

        select_file_button_image = PhotoImage(file=self.relative_to_assets("select_file_button.png"))
        select_file_button = Button(
            image=select_file_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("select_file_button clicked"),
            relief="flat"
        )
        select_file_button.place(
            x=1009.0,
            y=546.0,
            width=158.0,
            height=44.0
        )

        canvas.create_text(
            521.0,
            15.0,
            anchor="nw",
            text="F-Crypt",
            fill="#EEEEEE",
            font=("JetBrains Mono", 96 * -1, "bold"),
        )

        button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(1),
            relief="flat",
        )
        button_5.place(x=37.0, y=34.0, width=150.0, height=71.0)

        canvas.create_text(
            540.0,
            623.0,
            anchor="nw",
            text="Saves Encryption Key in a File",
            fill="#FFFFFF",
            font=("JetBrains Mono", 20 * -1, "bold"),
        )

        button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(3),
            relief="flat",
        )
        button_6.place(x=1300.0, y=290.0, width=118.0, height=70.0)

        button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(2),
            relief="flat",
        )
        button_7.place(x=1300.0, y=375.0, width=118.0, height=70.0)

        button_image_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.destroy(5),
            relief="flat",
        )
        button_8.place(x=1300.0, y=460.0, width=118.0, height=70.0)

        self.window.mainloop()


app().build_Menu()

# root.mainloop()
