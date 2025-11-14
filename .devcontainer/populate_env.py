import os
import json
import sys

# The name of the environment variable that holds the JSON string
CONFIG_ENV_VAR = "OPENBB_ENV_VARS"

# NOTE: The OUTPUT_FILE is no longer used for writing content, 
# as the content is now redirected via the postStartCommand in devcontainer.json.

def populate_env_from_json():
    """
    Reads a JSON string from an environment variable and prints
    key-value pairs to standard output in .env format (KEY=VALUE).
    The shell then redirects this output to the temporary file 
    /tmp/codespace_env_exports.
    """
    
    # 1. Get the JSON string from the environment
    json_str = os.environ.get(CONFIG_ENV_VAR)
    
    if not json_str:
        # Use sys.stderr for messages so they don't pollute standard output (which is the .env file content)
        print(f"Info: '{CONFIG_ENV_VAR}' environment variable not found.", file=sys.stderr)
        return
        
    try:
        # 2. Parse the JSON string into a Python dictionary
        config_dict = json.loads(json_str)
        
        # 3. Print the variables in plain KEY=VALUE format to standard output (stdout)
        for key, value in config_dict.items():
            env_key = str(key)
            env_value = str(value)
            
            # Print in the required KEY=VALUE format for .env files
            print(f"{env_key}={env_value}")
            
        print("Successfully generated environment variables for IDE.", file=sys.stderr)
            
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from {CONFIG_ENV_VAR}. Check syntax. Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    populate_env_from_json()