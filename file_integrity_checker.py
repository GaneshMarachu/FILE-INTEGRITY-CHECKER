import hashlib
import os
import json

# Path to store known hashes
HASH_STORE = "file_hashes.json"

# Function to calculate the SHA256 hash of a file
def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

# Load stored hash values from file
def load_hashes():
    if os.path.exists(HASH_STORE):
        with open(HASH_STORE, "r") as f:
            return json.load(f)
    return {}

# Save updated hash values
def save_hashes(hashes):
    with open(HASH_STORE, "w") as f:
        json.dump(hashes, f, indent=4)

# Monitor file changes
def check_integrity(file_list):
    stored_hashes = load_hashes()
    changed_files = []
    for filepath in file_list:
        current_hash = calculate_hash(filepath)
        if not current_hash:
            print(f"[ERROR] File not found: {filepath}")
            continue

        if filepath not in stored_hashes:
            print(f"[NEW] File not found in hash store: {filepath}")
            stored_hashes[filepath] = current_hash
        elif stored_hashes[filepath] != current_hash:
            print(f"[CHANGED] File has been modified: {filepath}")
            changed_files.append(filepath)
        else:
            print(f"[UNCHANGED] File OK: {filepath}")

    save_hashes(stored_hashes)
    return changed_files

# MAIN FUNCTION
if __name__ == "__main__":
    print("=== FILE INTEGRITY CHECKER ===")
    # Add paths to the files you want to monitor
    files_to_monitor = [
    r"C:\Users\ganes\OneDrive\Desktop\ganesh\cybersecurity intern\example.txt",
    r"C:\Users\ganes\OneDrive\Desktop\ganesh\cybersecurity intern\important_config.ini",
    r"C:\Users\ganes\OneDrive\Desktop\ganesh\cybersecurity intern\my_script.py"
]


    changed = check_integrity(files_to_monitor)

    if changed:
        print("\n The following files have been modified:")
        for f in changed:
            print(f" - {f}")
    else:
        print("\n All monitored files are intact.")
