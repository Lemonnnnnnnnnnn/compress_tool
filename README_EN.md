# Secure File Compression Tool

简体中文 | [English](README_EN.md)

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A batch file compression tool developed for storing sensitive resources on Baidu Cloud Drive:
- 🔒 7Z file password protection (AES-256 encryption)
- 🔑 Filename hash encryption (MD5)
- 📁 Automatic decryption metadata generation

## Key Features

- Interactive CLI interface
- Double-layer compression
- Filename hash encryption
- Automatic large file splitting (>2GB)
- Detailed operation logs
- Cross-platform support (Windows/Linux/macOS)

## Quick Start

### Requirements
- Python 3.8+
- pip package manager
- 7-Zip command line tool
  - Windows: Included in the program
  - Linux: `sudo apt-get install p7zip-full`
  - macOS: `brew install p7zip`

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/secure-compressor.git
cd secure-compressor

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# Run the program
python src/main.py

# Follow the prompts to input:
# 1. Source folder path
# 2. Output folder path
# 3. First layer compression password (requires confirmation)
# 4. Second layer compression password (requires confirmation)
# 5. Metadata filename (optional)
```

### Building Executable

```bash
# Use PyInstaller to build
pyinstaller build.spec

# The executable will be in the dist/ directory
# Windows: compress_tool.exe
# Linux/macOS: compress_tool
```

## Project Structure

```
secure-compressor/
├── src/                 # Source code
│   ├── main.py         # Main program
│   ├── compression.py  # Compression module
│   ├── utils.py        # Utility functions
│   └── logger.py       # Logging module
├── resources/          # Resources
│   ├── 7z.exe         # 7-Zip executable
│   └── 7z.dll         # 7-Zip dependency
├── requirements.txt    # Dependencies list
├── build.spec         # Build configuration
├── README.md          # Documentation
└── .gitignore        # Version control ignore config
```

## Features

| Feature              | Description                                                         |
|---------------------|---------------------------------------------------------------------|
| Double Encryption   | Two layers of 7Z password protection                                |
| Filename Encryption | MD5 hash algorithm                                                  |
| Large File Handling | Automatic 2GB volume splitting                                      |
| Metadata Management | Auto-generates meta.json file with decryption information           |
| Error Handling      | Detailed error logging and user-friendly prompts                    |
| Cross-platform      | Compatible with Windows/Linux/macOS systems                         |

## Security Warning

⚠️ Please securely store the following information:
1. Generated `meta.json` file
2. First layer compression password
3. Second layer compression password

Lost information will result in **unrecoverable** encrypted files!

## Development Guide

1. Submit issues to report problems
2. Fork repository for feature development
3. Include when creating Pull Requests:
   - Feature description
   - Test results
   - Related documentation updates

## License

This project is open-source under the [MIT License](LICENSE) 