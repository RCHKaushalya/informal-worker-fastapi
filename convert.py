import json
import os

def convert_json_to_env(json_file='firebase.json', env_file='.env'):
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found!")
        return

    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(env_file, 'w') as f:
        for key, value in data.items():
            # Standardize keys to uppercase for .env convention
            env_key = f"FIREBASE_{key.upper()}"
            # Firebase private keys contain newlines; we must preserve them correctly
            if key == "private_key":
                # Escaping newlines so they stay as literal '\n' in the .env file
                value = value.replace('\n', '\\n')
            
            f.write(f'{env_key}="{value}"\n')
    
    print(f"✅ Success! Created {env_file} with your credentials.")
    print("⚠️  Reminder: Add 'firebase.json' and '.env' to your .gitignore immediately.")

if __name__ == "__main__":
    convert_json_to_env()