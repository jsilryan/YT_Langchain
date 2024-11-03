from imports import *

def ensure_directory_exists(directory_path):
    try:
        directory_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"An error occurred while creating directory: {e}")
 
def construct_folder_path(base_path, *sub_paths):
    try:
        folder_path = base_path.joinpath(*sub_paths)
        ensure_directory_exists(folder_path)
        return folder_path
    except Exception as e:
        print(f"An error occurred while constructing folder path: {e}")
        return None
    
def sanitize_filename(filename):
    # Remove or replace invalid characters
    return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', filename)

desktop_folder = Path(os.getenv('USERPROFILE')) / 'Desktop' 