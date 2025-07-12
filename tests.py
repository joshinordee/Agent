# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info, get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


# Tests for get_files_content.py
print(get_files_info("calculator", "."))
print(get_files_info("calculator", "pkg"))
print(get_files_info("calculator", "/bin")) # should return error string /bin is not in calculator directory 
print(get_files_info("calculator", "../")) # should return error string because the agent should not work outside calculator directory

# Tests for get_file_content
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py")) 
print(get_file_content("calculator", "/bin/cat")) # should return error string

# tests for write_file
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

# tests for run_python_file
print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py")) # should return an error
print(run_python_file("calculator", "nonexistent.py")) # should return error (nonexistent.py does not exist)
