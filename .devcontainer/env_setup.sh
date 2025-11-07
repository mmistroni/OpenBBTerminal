#!/bin/bash

# --- env_setup.sh (Pure Shell Eval) ---

# 1. Get the source variable.
CONFIG_STRING="${OPENBB_ENV_VARS}"

# 2. Check if the variable is set and not empty
if [ -z "$CONFIG_STRING" ]; then
    echo "Warning: OPENBB_ENV_VARS is not set or is empty. Skipping environment setup."
    exit 0
fi

# 3. Clean the string and generate 'export' commands
#    The variable likely looks like: '{"KEY": "VALUE", "KEY2": "VALUE2"}'
#    We need to transform this into: 'export KEY="VALUE"; export KEY2="VALUE2";'

# A. Remove surrounding braces, spaces, newlines, and quotes
#    The input is of the form: { "key": "value", "key2": "value2" }

CLEANED_STRING=$(echo "$CONFIG_STRING" | \
    tr -d '[:space:]' | \
    sed -e 's/^{//' -e 's/}$//' -e 's/"//g' -e 's/:/="/g' -e 's/,/\" /g')

# B. Add the final quote to the last variable and prefix with export
# The result looks like: export KEY="VALUE" export KEY2="VALUE2"
EXPORT_COMMANDS=$(echo "$CLEANED_STRING" | sed -e 's/^/export /' -e 's/$/\"/')

# 4. Execute the cleaned string as shell commands using eval
#    This sets the variables in the current shell.
eval "$EXPORT_COMMANDS"

echo "Success: Environment variables loaded from OPENBB_ENV_VARS using shell eval."