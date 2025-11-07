#!/bin/bash

# --- env_setup.sh ---

# Define the file where we will write the variables. 
ENV_FILE="/workspaces/OpenBBTerminal/.codespace_env"

# 1. Get the source variable.
CONFIG_STRING="${OPENBB_ENV_VARS}"

if [ -z "$CONFIG_STRING" ]; then
    echo "Warning: OPENBB_ENV_VARS is not set or is empty. Skipping environment setup."
    exit 0
fi

# 2. Use Python to parse the JSON, clean the string, and write 'export KEY=VALUE' commands to the file
PYTHON_COMMAND="
import json
import os
import sys

# Get the output path from the shell argument
output_file = sys.argv[1] 
config_string = os.environ['OPENBB_ENV_VARS']

# CRITICAL FIX: Strip all newlines, carriage returns, and leading/trailing whitespace 
# before attempting to decode the JSON. This handles secrets formatting issues.
cleaned_config_string = config_string.replace('\n', '').replace('\r', '').strip() 

try:
    # Use the cleaned string for robust JSON loading
    config_dict = json.loads(cleaned_config_string)
except json.JSONDecodeError as e:
    print(f'Error: OPENBB_ENV_VARS is not valid JSON. {e}', file=sys.stderr)
    sys.exit(1)
except KeyError:
    # Should be caught by the shell script, but good practice
    sys.exit(0)

# Open the file and write the export commands
with open(output_file, 'w') as f:
    for key, value in config_dict.items():
        # Ensure values are quoted for safety
        f.write(f\"export {key}='{value}'\\n\")

print(f\"Successfully wrote environment variables to {output_file}\", file=sys.stderr)
"

# Execute the Python command, passing the output file path as an argument.
python3 -c "$PYTHON_COMMAND" "$ENV_FILE"