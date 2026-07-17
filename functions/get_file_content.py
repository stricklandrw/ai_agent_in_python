import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_file_path: str, file_path: str) -> str:
    working_dir_abs = os.path.abspath(working_file_path)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    print(f'Result for file {file_path}:')
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_file, 'r') as file:
            content = file.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if file.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    except Exception as e:
        return f'Error: An error occurred while reading file "{file_path}": {str(e)}'

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
        "parameters": {
            "type": "object",
            "properties": {
            "file_path": {
                "type": "string",
                "description": "Path to the file to read, relative to the working directory",
                },
            },
        },
    },
}