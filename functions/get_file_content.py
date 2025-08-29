# get_file_content.py
import os
from config import CONTENT_CHAR_LIMIT

def get_file_content(working_directory, file_path):
    try:
        # Use absolute paths for security
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Security check: is file_path within working_directory?
        if not abs_file_path.startswith(abs_working_dir + os.sep):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Is it a regular file?
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abs_file_path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        if len(content) > CONTENT_CHAR_LIMIT:
            truncated = content[:CONTENT_CHAR_LIMIT]
            truncated += f'[...File "{file_path}" truncated at {CONTENT_CHAR_LIMIT} characters]'
            return truncated

        return content

    except Exception as e:
        return f'Error: {str(e)}'
