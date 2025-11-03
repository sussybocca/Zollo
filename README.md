# Zollo

**Hybrid bundler for Python and Node.js projects**

Zollo is a Python-based CLI tool that can bundle user Python scripts and Node.js projects into a single build output. It’s perfect for hybrid projects that use both Python backend and Node frontend code.

---

## Why This Update Was Added

To improve **security, access control, and project workflow**, a dev-only encrypted release (`Zollo_dev-release.2.7z`) has been introduced:

- Certain development assets and build resources are sensitive and should only be accessed by **approved developers**.  
- Encrypted archives prevent unauthorized modification or redistribution of these critical files.  
- KeePassXC is used to manage the archive password, ensuring only approved devs can decrypt and use the files.  
- A clear approval and access policy via business email ensures accountability and proper collaboration.  

This update ensures that Zollo remains **secure, maintainable, and professional**, while still allowing personal use and local testing by authorized developers.

---

## Features

- Automatically detects and bundles Python scripts from `py/Zollo/backend/files/py/`  
- Bundles Node.js projects from `node/Zollo/frontend/files/js/`  
- CLI commands: `bundle`, `unhide`, `clean`  
- Supports hidden build output for secure packaging  
- Dev-only encrypted release for sensitive build resources

---

## Installation & Usage

```bash
# Clone the repository
git clone https://github.com/sussybocca/Zollo.git
cd Zollo

# Create virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
source .venv/bin/activate   # macOS/Linux

# Install editable package
pip install -e .

# Usage

# Show help
zollo --help

# Bundle Python and Node files
zollo bundle

# Unhide the build output folder
zollo unhide

# Clean the build output
zollo clean

