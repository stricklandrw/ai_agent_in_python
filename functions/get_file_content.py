import os
from config import MAX_CHARS

def get_file_content(working_file_path, file_path):
    working_dir_abs = os.path.abspath(working_file_path)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    print(f'Result for file {file_path}:')
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_target_dir:
        return print(f'    Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(target_file):
        return print(f'    Error: File not found or is not a regular file: "{file_path}"')
    try:
        with open(target_file, 'r') as file:
            content = file.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if file.read(1):
                content += f'    [...File "{file_path}" truncated at {MAX_CHARS} characters]'
            print(content)
    except Exception as e:
        print(f'    Error: An error occurred while reading file "{file_path}": {str(e)}')
