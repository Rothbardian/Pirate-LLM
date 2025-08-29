import os

def get_files_info(working_directory, directory="."):
    try:
        # Build the absolute path to the working_directory and target directory
        working_directory_abs = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, directory))

        # Prevent access outside the working_directory
        if not os.path.commonpath([target_path, working_directory_abs]) == working_directory_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if directory is an actual directory
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'

        # Attempt to list and describe directory contents
        entries = []
        for name in sorted(os.listdir(target_path)):
            entry_path = os.path.join(target_path, name)
            try:
                size = os.path.getsize(entry_path)
                is_dir = os.path.isdir(entry_path)
                entries.append(f"- {name}: file_size={size} bytes, is_dir={str(is_dir)}")
            except Exception as e:
                entries.append(f"- {name}: Error: {str(e)}")
        return "\n".join(entries)

    except Exception as e:
        return f"Error: {str(e)}"
