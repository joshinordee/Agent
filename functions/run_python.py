import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        path = os.path.join(working_directory, file_path)

        # absolute paths
        working_directory_abs_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(path)

        if not target_path.startswith(working_directory_abs_path): # LLM permissions
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
        if not os.path.isfile(target_path): # make sure file path exists
            return f'Error: File "{file_path}" not found.'
    
        if not file_path.endswith(".py"): # ensure a python file is run
            return f'Error: "{file_path}" is not a Python file.'
    
        result = subprocess.run(["python3", target_path], cwd=working_directory, capture_output=True, timeout=30)

        # decode stdout and stderr outputs
        stdout_text = result.stdout.decode()
        stderr_text = result.stderr.decode() 

        if not stdout_text.strip() and not stderr_text.strip(): # incase no output is produced
            return "No output produced."

        if result.returncode != 0: 
            return f'Process exited with code {result.returncode} STDOUT: {stdout_text} STDERR: {stderr_text}'
        
        return f'STDOUT: {stdout_text} STDERR: {stderr_text}'

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
