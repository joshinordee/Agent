import os
from functions.config import *


def get_files_info(working_directory, directory=None):
    try:
        if directory is None:
            directory = "."

        full_path = os.path.join(working_directory, directory) # get full path 

        # absolute paths 
        working_directory_abs_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(full_path)

        if not target_path.startswith(working_directory_abs_path): # make sure only permitted directories are analyzed by the LLM
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
        if not os.path.isdir(target_path): # make sure directory exists
            return f'Error: "{directory}" is not a directory'

    
        content_lines = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)
            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path)
            content_lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(content_lines)
    
    except Exception as e:
        return f"Error: {str(e)}"
    
def get_file_content(working_directory, file_path):
    try:
        file_path = os.path.join(working_directory, file_path)

        # absolute paths
        working_directory_abs_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(file_path)

        if not target_path.startswith(working_directory_abs_path): # make sure only permitted file_paths ctories are analyzed by the LLM
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{target_path}"'
    
        with open(target_path, "r") as f:
            file_content_string = f.read(CHARACTER_LIMIT)

        if len(file_content_string) == CHARACTER_LIMIT:
            return f'{file_content_string} [...File "{file_path}" truncated at {CHARACTER_LIMIT} characters]'
        
        return file_content_string
        
    except OSError as e:
        return f"Error: {str(e)}"
    

    

