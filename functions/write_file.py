import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # Will be True or False
    # print(f'Trying to write to file {file_path}:')
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
    if not valid_target_file:
        return f'Error: Write to "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    try:
        # print(f'Creating file structure {target_file}:')
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        # print(f'Writing contents to {file_path}:')
        with open(target_file, 'w') as file:
            if file.write(content):
                return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: An error occurred while writing content to {file_path}: {str(e)}'
    
schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write content to a file in a specified directory relative to the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
            "file_path": {
                "type": "string",
                "description": "Path to the file to write to, relative to the working directory",
                },
            "content": {
                "type": "string",
                "description": "The content to write to the file",
                },
            },
        },
    },
}