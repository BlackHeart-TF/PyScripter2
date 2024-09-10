import tempfile
import subprocess
import sys

import os

# Directory to store custom modules
MODULES_DIR = 'modules'

# Ensure the directory exists
os.makedirs(MODULES_DIR, exist_ok=True)

script_imports = (
    "from modules.Key import Key\n"+
    "from modules.Window import Window\n"+
    "from modules.Image import Image\n"+
    #"from time import delay_ms as delay\n"
    "\n"
    )

def run_user_script(script_content):
    # Save the script to a temporary file
    # with tempfile.NamedTemporaryFile(delete=False, suffix='.py') as temp_script:
    #     temp_script.write((script_imports+script_content).encode('utf-8'))
    #     temp_script_path = temp_script.name
    temp_script_path = "./run.py"
    with open(temp_script_path, 'w', encoding='utf-8') as script_file:
        script_file.write(script_imports + script_content)
    # Add the custom modules directory to the PYTHONPATH
    old_path = sys.path.copy()
    sys.path.append(MODULES_DIR)

    try:
        # Run the script using subprocess
        result = subprocess.run([sys.executable, temp_script_path], capture_output=True, text=True)
        print("Script Output:", result.stdout)
        if result.stderr:
            print("Script Errors:", result.stderr)
    finally:
        # Restore the old PYTHONPATH
        sys.path = old_path
        os.remove(temp_script_path)
