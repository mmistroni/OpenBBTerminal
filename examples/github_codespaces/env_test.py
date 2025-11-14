import os
import sys


# Change 'fmp_api_key' to any variable you need to test
key = "fmp_api_key" 
value = os.environ.get(key)

if value:
    print(f"SUCCESS: {key} is loaded. Value starts with: {value[:5]}...")
    sys.exit(0)
else:
    print(f"FAILURE: {key} is NOT loaded in the IDE environment.")
    sys.exit(1)