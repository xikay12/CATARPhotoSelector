import os
import shutil
from tkinter import Tk, filedialog

def select_folder():
    # Hide the root window
    root = Tk()
    root.withdraw()
    
    # Open a folder selection dialog
    folder_selected = filedialog.askdirectory(title="Select Folder")
    return folder_selected

def read_filenames_from_txt(folder_path, txt_filename="text.txt"):
    txt_file_path = os.path.join(folder_path, txt_filename)
    
    if not os.path.exists(txt_file_path):
        print(f"{txt_filename} not found in the selected folder.")
        return []
    
    with open(txt_file_path, 'r') as file:
        filenames = file.read().splitlines()
    
    return filenames

def copy_files_to_result_folder(folder_path, filenames):
    result_folder = os.path.join(folder_path, 'Result')
    
    # Create the Result folder if it doesn't exist
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    
    for filename in filenames:
        raw_file = os.path.join(folder_path, f"{filename}.ARW")
        jpeg_file = os.path.join(folder_path, f"{filename}.JPG")
        
        # Copy the raw file if it exists
        if os.path.exists(raw_file):
            shutil.copy(raw_file, result_folder)
            print(f"Copied {raw_file} to {result_folder}")
        
        # Copy the jpeg file if it exists
        if os.path.exists(jpeg_file):
            shutil.copy(jpeg_file, result_folder)
            print(f"Copied {jpeg_file} to {result_folder}")

if __name__ == "__main__":
    # Step 1: Select the folder
    folder_path = select_folder()
    
    # Step 2: Read filenames from text.txt
    filenames = read_filenames_from_txt(folder_path)
    
    # Step 3: Copy files to Result folder
    if filenames:
        copy_files_to_result_folder(folder_path, filenames)
    else:
        print("No filenames found in text.txt or text.txt does not exist.")
