import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        # Will be True or False
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
#        return f'Success: "{directory}" is within the working directory'
        try:
            files = os.listdir(target_dir)
            file_info = []
            for file in files:
                file_path = os.path.join(target_dir, file)
                file_info.append(f"  - {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
            return "\n".join(file_info)
        except OSError as e:
            return f'Error: {e}'
    except Exception as e:
        return f'Error: {e}'

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}

