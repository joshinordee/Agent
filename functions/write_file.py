import os

def write_file(working_directory, file_path, content):
   try:
        path = os.path.join(working_directory, file_path)

        # absolute paths
        working_directory_abs_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(path)

        if not target_path.startswith(working_directory_abs_path): # make sure only permitted file_paths ctories are analyzed by the LLM
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(os.path.dirname(target_path)): # if path does not exist create it
            os.makedirs(os.path.dirname(target_path))
            
        with open(target_path, "w") as f: # write to file
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

   except Exception as e:
        return f"Error: {str(e)}"