import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # print(f'Result for file {file_path}:')
        # Will be True or False
        if os.path.commonpath([working_dir_abs, absolute_file_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not absolute_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", absolute_file_path]
        if args:
            command.extend(args)
        response = subprocess.run(
            command,
            capture_output=True,
            timeout=30,
            check=True,
            text=True,
            cwd=working_dir_abs
        )
        output: list[str] = []
        if response.returncode != 0:
            output.append(f'Process exited with code {response.returncode}\n')
        if not response.stdout and not response.stderr:
            output.append('No output produced')
        if response.stdout:
            output.append(f'STDOUT:\n{response.stdout}')
        if response.stderr:
            output.append(f'STDERR:\n{response.stderr}')
        return '\n'.join(output)
    except Exception as e:
        return f'Error: executing Python file: {e}'

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a specified Python file within the working directory and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of string arguments to pass to the Python script when executing",
                },
            },
            "required": ["file_path"],
        },
    },
}