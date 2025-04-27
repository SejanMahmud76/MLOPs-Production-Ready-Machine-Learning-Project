import os
temp_dir = os.path.join(os.environ.get("TEMP", "C:\\temp"), "test_write")
os.makedirs(temp_dir, exist_ok=True)
test_file = os.path.join(temp_dir, "test.txt")
try:
    with open(test_file, "w") as f:
        f.write("This is a test.")
    print(f"Successfully wrote to: {test_file}")
except Exception as e:
    print(f"Error writing to temporary directory: {e}")
finally:
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)