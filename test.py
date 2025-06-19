import tkinter as tk
from tkinter import Tk, Frame, Label, Button
from pathlib import Path


class YourApp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1445x813")
        self.window.configure(bg="#053B50")

        # FIRST - Test without removing default title bar
        # Comment out the next line to see if custom title bar works first
        # self.window.overrideredirect(True)

        # Asset and Output Path
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"./assets")

        # Try to set icon (with error handling)
        try:
            self.window.iconbitmap(self.OUTPUT_PATH / "assets" / "icon.ico")
        except:
            print("Icon file not found - continuing without icon")

        # Variables for window dragging
        self.x = 0
        self.y = 0

        # Your existing variables
        self.str_to_hex_value = ""
        self.str_to_Bytes_value = ""
        self.str_to_Bits_value = ""
        self.hex_to_str_value = ""
        self.hex_to_int_value = ""
        self.encryption_key = ""

        # Create custom title bar FIRST
        self.create_custom_titlebar()

        # Then build your menu
        self.build_Menu()

        print("App initialized successfully")

    def create_custom_titlebar(self):
        print("Creating custom title bar...")

        # Create a very visible title bar for testing
        self.title_bar = Frame(
            self.window,
            bg="#FF0000",  # RED for testing - you'll see this easily
            height=50,
            relief="solid",
            bd=2,
        )
        self.title_bar.pack(fill="x", side="top")
        self.title_bar.pack_propagate(False)

        # Title label
        self.title_label = Label(
            self.title_bar,
            text="Hacking Toolkit - CUSTOM TITLE BAR",
            bg="#FF0000",  # RED for testing
            fg="white",
            font=("Arial", 12, "bold"),
        )
        self.title_label.pack(side="left", padx=10, pady=10)

        # Simple close button for testing
        self.close_btn = Button(
            self.title_bar,
            text="X CLOSE",
            bg="#FF0000",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.close_window,
        )
        self.close_btn.pack(side="right", padx=10, pady=10)

        print("Title bar widgets created")

    def close_window(self):
        print("Closing window...")
        self.window.destroy()

    def build_Menu(self):
        print("Building menu...")

        # Create main content area
        self.main_frame = Frame(self.window, bg="#053B50")
        self.main_frame.pack(fill="both", expand=True)

        # Test content
        test_label = Label(
            self.main_frame,
            text="This is your main app content area",
            bg="#053B50",
            fg="white",
            font=("Arial", 16),
        )
        test_label.pack(pady=50)

        print("Menu built successfully")


# Run the test
if __name__ == "__main__":
    print("Starting app...")
    app = YourApp()
    app.window.mainloop()
