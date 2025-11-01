# Zollo

**Hybrid bundler for Python and Node.js projects**

Zollo is a Python-based CLI tool that can bundle user Python scripts and Node.js projects into a single build output. It’s perfect for hybrid projects that use both Python backend and Node frontend code.

---

## Features

- Automatically detects and bundles Python scripts from `py/Zollo/backend/files/py/`  
- Bundles Node.js projects from `node/Zollo/frontend/files/js/`  
- CLI commands: `bundle`, `unhide`, `clean`  
- Supports hidden build output for secure packaging

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
