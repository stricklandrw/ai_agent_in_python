import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    # Will be True or False
    print(f'Result for {directory} directory:')
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        return print(f'    Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.exists(target_dir):
        return print(f'Error: "{directory}" is not a directory')
    try:
        for file in os.listdir(target_dir):
            file_path = os.path.join(target_dir, file)
            print(f"  - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
    except Exception as e:
        print(f'Error: An error occurred while listing files in "{directory}": {str(e)}')

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

