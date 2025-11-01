# D:\Zollo\zollo\constants.py
import os

# For testing: user Python files inside the same zollo folder
ZOLLO_PY_PATH = os.path.join("zollo", "backend_files", "py")

# Output folders
ZOLLO_OUTPUT_DIR = ".zollo_build"
PYTHON_BUILD_DIR = os.path.join(ZOLLO_OUTPUT_DIR, "backend_bundle")

# Node folder (optional, for testing)
ZOLLO_NODE_PATH = os.path.join("zollo", "frontend_files", "js")
NODE_BUILD_DIR = os.path.join(ZOLLO_OUTPUT_DIR, "frontend_bundle")

# Config file
ZOLLO_CONFIG_FILE = "zollo.config.json"
