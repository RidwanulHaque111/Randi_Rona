import os
import random
import pyperclip

def copy_random_file_content(directory):
    # List all .txt files in the directory
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    if not txt_files:
        print("No .txt files found in the directory.")
        return
    
    # Select a random file
    random_file = random.choice(txt_files)
    
    # Read the content of the random file
    with open(os.path.join(directory, random_file), 'r') as file:
        file_content = file.read()
    
    # Copy content to clipboard
    pyperclip.copy(file_content)
    print("Copied to clipboard from file:", random_file)

# Directory containing .txt files
directory_path = 'E:/Projects/Randi_Rona/aukat'

# Call the function
copy_random_file_content(directory_path)
