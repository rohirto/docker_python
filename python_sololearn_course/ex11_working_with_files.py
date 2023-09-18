""" Working with files"""
import os

# Define a file path
FILE_PATH = "/workspaces/docker_python/python_sololearn_course/files/sample.txt"

# Writing to a File
try:
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
except IOError as e:
    print(f"Error writing to the file: {e}")
else:
    print("File write successful.")

# Reading from a File
try:
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
except IOError as e:
    print(f"Error reading the file: {e}")
else:
    print("File read successful:")
    print(content)

# Appending to a File
try:
    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write("Appending new content.\n")
except IOError as e:
    print(f"Error appending to the file: {e}")
else:
    print("File append successful.")

# Reading Lines from a File
try:
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        lines = file.readlines()
except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
except IOError as e:
    print(f"Error reading the file: {e}")
else:
    print("Reading lines from the file:")
    for line in lines:
        print(line.strip())

# Handling Exceptions
try:
    with open("nonexistent.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
except IOError as e:
    print(f"Error reading the file: {e}")
else:
    print("File read successful (should not reach here).")
finally:
    print("File operation completed.")

# Deleting a File
try:
    os.remove(FILE_PATH)
except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
except PermissionError as e:
    print(f"Error deleting the file: {e}")
else:
    print("File deleted successfully.")
    