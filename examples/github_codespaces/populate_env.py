import os
import json
import sys

# The name of the environment variable that holds the JSON string
CONFIG_ENV_VAR = "OPENBB_ENV_VARS"

# The file that will hold the shell 'export' commands
OUTPUT_FILE = "/tmp/codespace_env_exports"

def populate_env_from_json():
    """
    Reads a JSON string from an environment variable, 
    generates 'export' commands for each key-value pair, 
    and writes them to a temporary file.
    """
    
    # 1. Get the JSON string from the environment
    json_str = os.environ.get(CONFIG_ENV_VAR)
    
    if not json_str:
        # Exit silently if the configuration variable isn't set
        return
        
    try:
        # 2. Parse the JSON string into a Python dictionary
        config_dict = json.loads(json_str)
        
        # 3. Generate the export commands
        exports = []
        for key, value in config_dict.items():
            # Ensure keys are valid environment variable names (conventionally uppercase)
            env_key = str(key)#.upper()
            
            # Escape value for shell safety and ensure it's a string
            env_value = str(value).replace("'", "'\\''")
            
            exports.append(f"export {env_key}='{env_value}'")
        
        # 4. Write the exports to the temporary file
        with open(OUTPUT_FILE, "w") as f:
            f.write("\n".join(exports))
            
        print(f"Successfully generated environment variables from '{CONFIG_ENV_VAR}' in {OUTPUT_FILE}")
        
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from {CONFIG_ENV_VAR}. Check syntax. Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    populate_env_from_json()