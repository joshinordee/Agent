# from subdirectory.filename import function_name
from functions.get_files_info import get_file_content


# Tests for get_files_content.py

#print(get_file_content("calculator", "main.py"))
#print(get_file_content("calculator", "pkg/calculator.py"))
#print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "lorem.txt"))
