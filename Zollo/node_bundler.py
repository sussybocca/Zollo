# D:\Zollo\zollo\node_bundler.py
import os
import subprocess
from zollo.constants import ZOLLO_NODE_PATH, NODE_BUILD_DIR
from zollo.utils import ensure_dir_exists

def bundle_node_files():
    print("[Zollo] Starting Node.js bundling...")

    if not os.path.exists(ZOLLO_NODE_PATH):
        print(f"[Zollo] Skipping: Node folder not found at {ZOLLO_NODE_PATH}")
        return

    ensure_dir_exists(NODE_BUILD_DIR)

    pkg_path = os.path.join(ZOLLO_NODE_PATH, "package.json")
    if not os.path.exists(pkg_path):
        print("[Zollo] No package.json found — skipping Node build.")
        return

    try:
        subprocess.run(["npm", "install"], cwd=ZOLLO_NODE_PATH, check=True)
        subprocess.run(["npm", "run", "build"], cwd=ZOLLO_NODE_PATH, check=True)
        print("[Zollo] Node build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[Zollo] Node build failed: {e}")

    build_dir = os.path.join(ZOLLO_NODE_PATH, "build")
    if os.path.exists(build_dir):
        import shutil
        shutil.copytree(build_dir, NODE_BUILD_DIR, dirs_exist_ok=True)
        print(f"[Zollo] Node build output copied to {NODE_BUILD_DIR}")
    else:
        print("[Zollo] No 'build/' directory found — did your build script output anything?")
