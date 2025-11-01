# D:\Zollo\zollo\bundler.py
import os
import shutil
from zollo.constants import ZOLLO_PY_PATH, PYTHON_BUILD_DIR
from zollo.utils import list_py_files, ensure_dir_exists

def bundle_python_files():
    print("[Zollo] Starting Python bundling...")

    if not os.path.exists(ZOLLO_PY_PATH):
        print(f"[Zollo] Skipping: Python folder not found at {ZOLLO_PY_PATH}")
        return

    ensure_dir_exists(PYTHON_BUILD_DIR)
    py_files = list_py_files(ZOLLO_PY_PATH)
    print(f"[Zollo] Found {len(py_files)} Python files to bundle.")

    for file in py_files:
        rel_path = os.path.relpath(file, ZOLLO_PY_PATH)
        dest_path = os.path.join(PYTHON_BUILD_DIR, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(file, dest_path)

    print(f"[Zollo] Python bundling complete. Output in: {PYTHON_BUILD_DIR}")
