import os
import shutil

def organize_files_by_extension(directory):
    """
    Organize files in the given directory into subdirectories based on their file extensions.
    """
    # List all files in directory
    for filename in os.listdir(directory):
        # Get file extension
        file_ext = filename.split('.')[-1]
        
        # Check if this is a file (and not a directory)
        if os.path.isfile(os.path.join(directory, filename)):
            # Check if directory exists for this file extension, if not create one
            ext_dir = os.path.join(directory, file_ext)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)

            # Move file into corresponding directory
            shutil.move(os.path.join(directory, filename), os.path.join(ext_dir, filename))


# Usage:
current_directory = os.getcwd()  # Gets the current directory
organize_files_by_extension(current_directory)
