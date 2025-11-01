# D:\Zollo\zollo\utils.py
import os
import shutil

def ensure_dir_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)

def clear_dir(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def list_py_files(base_dir: str):
    py_files = []
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".py"):
                py_files.append(os.path.join(root, f))
    return py_files
