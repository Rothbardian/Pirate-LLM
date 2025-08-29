import os

from config import CONTENT_CHAR_LIMIT

def write_file(working_directory, file_path, content):
    try:
        # Resolve absolute paths for security
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Security check: is file_path within working_directory?
        if not abs_file_path.startswith(abs_working_dir + os.sep):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Make parent dirs if necessary
        parent_dir = os.path.dirname(abs_file_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir, exist_ok=True)

        # Write content to file (overwriting or creating)
        with open(abs_file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {str(e)}'
