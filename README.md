# 🛡️ Hacking Toolkit

A comprehensive cybersecurity toolkit built with Python and Tkinter, designed for security professionals, ethical hackers, and cybersecurity enthusiasts. This all-in-one application provides essential tools for hashing, string manipulation, file encryption, and cryptographic operations.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🚀 Features

### 🔐 Hash Panel
- **Multiple Hashing Algorithms**: Support for MD5, SHA1, SHA256, and SHA512
- **Text Hashing**: Hash any text string with your chosen algorithm
- **File Hashing**: Generate hash checksums for files of any size
- **Click-to-Copy**: One-click copying of hash values to clipboard
- **File Selection**: Built-in file browser for easy file selection

### 🔤 Strings Panel
- **String Comparison**: Compare up to 5 strings simultaneously to check for similarities
- **Format Conversion**: Convert strings to multiple formats:
  - **Hexadecimal**: String to hex representation
  - **Bytes**: String to byte values
  - **Bits**: String to binary representation
- **Hex Decoder**: Convert hexadecimal back to integers and strings
- **Interactive Results**: Click any result to copy it to clipboard

### 🔒 F-Crypt Panel (File Encryption)
- **Advanced Encryption**: Secure file encryption using industry-standard algorithms
- **Key Generation**: Generate 256-bit and 512-bit encryption keys
- **File Operations**:
  - Encrypt files with custom or generated keys
  - Decrypt previously encrypted files
  - Key management and storage
- **User-Friendly Interface**: Simple encrypt/decrypt workflow with status feedback

### 🎯 Additional Features
- **Intuitive Navigation**: Clean, modern interface with easy panel switching
- **Clipboard Integration**: Seamless copying of results to system clipboard
- **Error Handling**: Comprehensive error management with user feedback
- **Cross-Panel Navigation**: Quick access buttons between different tools

## 📥 Installation & Usage

### For Windows Users (Recommended)
Download the compiled executable from the releases section:
1. Go to [Releases](../../releases)
2. Download the latest `.exe` file
3. Run the executable - no installation required!

### For Developers
If you want to run from source or contribute:

```bash
# Clone the repository
git clone https://github.com/yourusername/hacking-toolkit.git
cd hacking-toolkit

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## 🖥️ System Requirements

- **Operating System**: Windows 10/11 (64-bit)
- **RAM**: Minimum 2GB
- **Storage**: 50MB free space
- **Python**: 3.7+ (if running from source)

## 📖 User Guide

### Getting Started
1. Launch the application
2. Choose your desired tool from the main menu:
   - **Hash**: For file and text hashing operations
   - **Strings**: For string manipulation and comparison
   - **F-Crypt**: For file encryption/decryption
   - **Sub-Domber**: Coming soon!

### Hash Panel Usage
1. **For Text Hashing**:
   - Enter your text in the input field
   - Click the desired algorithm button (MD5, SHA1, SHA256, SHA512)
   - Click the result to copy to clipboard

2. **For File Hashing**:
   - Click "Select File" to choose your file
   - Click the desired algorithm button
   - The hash will appear below - click to copy

### Strings Panel Usage
1. **String Comparison**:
   - Enter up to 5 strings in the input fields
   - Click "Check" to see if they're similar
   - Result shows "True" or "False"

2. **String Conversion**:
   - Enter text in the conversion field
   - Click "Convert" to see Hex, Bytes, and Bits representations
   - Click any result to copy to clipboard

3. **Hex Conversion**:
   - Enter hex values in the hex input field
   - Automatically converts to Integer and String
   - Click results to copy

### F-Crypt Panel Usage
1. **Generate Encryption Key**:
   - Click "256 Bit" or "512 Bit" to generate a key
   - Click "Copy to Entry" to use the generated key

2. **Encrypt Files**:
   - Select file using "Select File" button
   - Enter or generate encryption key
   - Click "Encrypt" - encrypted file will be saved

3. **Decrypt Files**:
   - Select the encrypted file
   - Enter the correct encryption key
   - Click "Decrypt" to restore original file

## 🛠️ Developer Information

### Architecture
- **Frontend**: Tkinter with custom styling and assets
- **Backend**: Modular Python scripts for each functionality
- **File Structure**:
  ```
  ├── app.py              # Main application file
  ├── Scripts/
  │   ├── Hash.py         # Hashing algorithms
  │   ├── Strings.py      # String manipulation
  │   └── Baval.py        # Encryption/decryption
  └── assets/             # UI assets and images
  ```

### Key Classes and Methods
- **`app`**: Main application class handling UI and navigation
- **`gethash()`**: Text hashing functionality
- **`getfilehash()`**: File hashing functionality
- **`str_conversion()`**: String format conversion
- **`hex_conversion()`**: Hexadecimal conversion
- **`encrypt_file()`/`decrypt_file()`**: File encryption operations

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Dependencies
```python
tkinter          # GUI framework
pathlib          # File path handling
hashlib          # Hashing algorithms
cryptography     # Encryption operations
```

## ⚠️ Disclaimer

This tool is designed for **educational purposes** and **authorized security testing only**. Users are responsible for ensuring they have proper authorization before using these tools on any systems or files. The developers are not responsible for any misuse of this software.

## 🔮 Roadmap

- [ ] **Sub-Domber Panel**: Subdomain enumeration tool
- [ ] **Linux/Mac Support**: Cross-platform compatibility
- [ ] **Advanced Encryption**: Additional encryption algorithms
- [ ] **Batch Operations**: Process multiple files simultaneously
- [ ] **Plugin System**: Extensible architecture for custom tools
- [ ] **Dark/Light Theme**: UI theme options

## 📞 Support

Having issues? Here's how to get help:

1. Check the [Issues](../../issues) page for known problems
2. Create a new issue with:
   - Detailed description of the problem
   - Steps to reproduce
   - System information
   - Screenshots (if applicable)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Acknowledgments

- Built with Python and Tkinter
- Icons and UI elements designed for modern cybersecurity workflows
- Inspired by the need for consolidated security tools

---

**⭐ If you find this tool useful, please consider starring the repository!**

Made with ❤️ for the cybersecurity community