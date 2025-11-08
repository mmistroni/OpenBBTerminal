#!/bin/bash

# --- env_setup.sh (EVAL VERSION) ---

# Define the files where we will write the variables and the error log
ENV_FILE="/workspaces/OpenBBTerminal/.codespace_env"
ERROR_FILE="/workspaces/OpenBBTerminal/.codespace_env_error.log"

# Define the source variable.
CONFIG_STRING="${OPENBB_ENV_VARS}"

if [ -z "$CONFIG_STRING" ]; then
    echo "Warning: OPENBB_ENV_VARS is not set or is empty. Skipping environment setup." >&2
    exit 0
fi

# 2. Use Python to parse the dictionary and handle errors.
PYTHON_COMMAND="
import os
import sys

output_file = sys.argv[1] 
error_file = sys.argv[2]
config_string = os.environ['OPENBB_ENV_VARS']

# CRITICAL: Clean up string, especially for multi-line secrets
cleaned_config_string = config_string.replace('\n', '').replace('\r', '').strip() 

try:
    # >>> CRITICAL CHANGE: Use eval() <<<
    # Note: Keys in the dictionary literal must be strings (e.g., {'KEY': 'value'})
    config_dict = eval(cleaned_config_string)
    
    if not isinstance(config_dict, dict):
        raise TypeError('Evaluated result was not a dictionary.')

except Exception as e:
    # WRITE THE ERROR MESSAGE TO THE ERROR LOG
    import traceback
    with open(error_file, 'w') as f:
        f.write(f'--- EVAL PARSE ERROR ---\\n')
        f.write(f'Error Type: {type(e).__name__}\\n')
        f.write(f'Error Message: {e}\\n')
        f.write(f'Offending String (Truncated): {cleaned_config_string[:200]}...\\n')
        f.write('\\n--- Traceback ---\\n')
        traceback.print_exc(file=f)
    sys.exit(1) # Exit with failure

# Open the environment file and write the export commands
with open(output_file, 'w') as f:
    for key, value in config_dict.items():
        # Ensure keys and values are treated as strings for export
        f.write(f\"export {str(key)}='{str(value)}'\\n\")
"

# Execute the Python command, passing both file paths.
python3 -c "$PYTHON_COMMAND" "$ENV_FILE" "$ERROR_FILE"