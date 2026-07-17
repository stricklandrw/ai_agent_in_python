import os
import subprocess
from google.genai import types


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
    # print(f'Result for file {file_path}:')
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, absolute_file_path]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(absolute_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    if not absolute_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    command = ["python", absolute_file_path]
    if args:
        command.extend(args)
    try:
        response = subprocess.run(
            command,
            capture_output=True,
            timeout=30,
            check=True,
            text=True,
            cwd=working_dir_abs
            )
        full_output = ''
        if response.returncode != 0:
            full_output += f'Process exited with code {response.returncode}\n'
        if not response.stdout and not response.stderr:
            full_output += 'No output produced\n'
        else:
            full_output += f'STDOUT: {response.stdout}\nSTDERR: {response.stderr}'
        return full_output
    except Exception as e:
        return f'Error: executing Python file: {e}'

# schema_run_python_file = types.FunctionDeclaration(
#     name="run_python_file",
#     description="Print the contents of a file in a specified directory relative to the working directory.  If the file is larger than the maximum content size, the contents are truncaterd to the character limit {MAX_CHARS}.",
#     parameters=types.Schema(
#         type=types.Type.OBJECT,
#         required=["file_path"],
#         properties={
#             "file_path": types.Schema(
#                 type=types.Type.STRING,
#                 description="Path to the Python file to execute, relative to the working directory",
#             ),
#             "args": types.Schema(
#                 type=types.Type.ARRAY,
#                 items=types.Type.STRING,
#                 description="Optional list of string arguments to pass to the Python script when executing",
#             ),
#         },
#     ),
# )