# D:\Zollo\zollo\cli.py
import argparse
import os
from zollo.bundler import bundle_python_files
from zollo.node_bundler import bundle_node_files
from zollo.constants import ZOLLO_OUTPUT_DIR

def main():
    parser = argparse.ArgumentParser(prog="zollo", description="Zollo Hybrid Bundler")
    parser.add_argument("command", choices=["bundle", "unhide", "clean"], help="Command to execute")

    args = parser.parse_args()

    if args.command == "bundle":
        print("[Zollo] Running hybrid bundler...")
        bundle_python_files()
        bundle_node_files()
        print(f"[Zollo] Bundling finished. Output is in {ZOLLO_OUTPUT_DIR}")

    elif args.command == "unhide":
        if os.path.exists(ZOLLO_OUTPUT_DIR):
            new_name = ZOLLO_OUTPUT_DIR.replace(".", "", 1)
            os.rename(ZOLLO_OUTPUT_DIR, new_name)
            print(f"[Zollo] Output unhidden: {new_name}")
        else:
            print("[Zollo] No hidden output found.")

    elif args.command == "clean":
        import shutil
        if os.path.exists(ZOLLO_OUTPUT_DIR):
            shutil.rmtree(ZOLLO_OUTPUT_DIR)
            print("[Zollo] Cleaned build output.")
        else:
            print("[Zollo] Nothing to clean.")

if __name__ == "__main__":
    main()
