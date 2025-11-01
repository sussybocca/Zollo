# D:\Zollo\zollo\config.py
import json
from zollo.constants import ZOLLO_CONFIG_FILE

def load_config():
    try:
        with open(ZOLLO_CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "name": "my_zollo_project",
            "output": ".zollo_build",
            "hidden": True
        }
