import os
import json
import sys

# The name of the environment variable that holds the JSON string
CONFIG_ENV_VAR = "OPENBB_ENV_VARS"

def populate_env_from_json():
    """
    Reads a JSON string from the secure environment variable and prints
    key-value pairs to standard output in the SHELL EXPORT format
    (export KEY="VALUE").
    """
    
    # 1. Get the JSON string from the environment
    json_str = os.environ.get(CONFIG_ENV_VAR)
    
    if not json_str:
        # Use sys.stderr so this message doesn't pollute the standard output
        print(f"Info: '{CONFIG_ENV_VAR}' environment variable not found. Using defaults.", file=sys.stderr)
        return
        
    try:
        # 2. Parse the JSON string into a Python dictionary
        config_dict = json.loads(json_str)
        
        # 3. Print the variables in the required 'export KEY="VALUE"' format
        for key, value in config_dict.items():
            env_key = str(key)
            
            # Escape double quotes within the value to prevent shell parsing errors
            # We use triple-quotes to handle the single JSON string that may contain quotes
            env_value = str(value).replace('"', '\\"') 
            
            # Print the SHELL EXPORT command to standard output (stdout).
            # The shell will redirect this output to /tmp/codespace_env_exports.
            print(f'export {env_key}="{env_value}"')
            
        print("✅ Success: Generated shell export commands to stdout.", file=sys.stderr)
            
    except json.JSONDecodeError as e:
        print(f"❌ Error: Failed to decode JSON from {CONFIG_ENV_VAR}. Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    populate_env_from_json()

# Note: The copy_env_to_ide_file function was removed because the shell 
# command in devcontainer.json now handles copying the /tmp file to .env.